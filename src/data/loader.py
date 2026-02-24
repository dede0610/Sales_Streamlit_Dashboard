"""Data loading module with Streamlit caching."""

import logging
from pathlib import Path

import polars as pl
import streamlit as st

logger = logging.getLogger(__name__)


@st.cache_data(ttl=3600)
def load_data(path: str | Path) -> pl.DataFrame:
    """Load data from Parquet file with Streamlit caching.

    Args:
        path: Path to the Parquet file.

    Returns:
        Polars DataFrame with the data.

    Raises:
        FileNotFoundError: If the file doesn't exist.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    logger.info(f"Loading data from {path}")
    df = pl.read_parquet(path)

    logger.info(f"Loaded {len(df)} rows with columns: {df.columns}")
    return df


@st.cache_data(ttl=3600)
def compute_summary(df: pl.DataFrame, value_col: str = "value") -> dict:
    """Compute summary statistics with caching.

    Args:
        df: Input DataFrame.
        value_col: Name of the value column.

    Returns:
        Dictionary with summary statistics.
    """
    if df.is_empty() or value_col not in df.columns:
        return {}

    return {
        "total": float(df[value_col].sum()),
        "mean": float(df[value_col].mean()),
        "count": len(df),
        "min": float(df[value_col].min()),
        "max": float(df[value_col].max()),
    }


@st.cache_data(ttl=3600)
def aggregate_by_column(
    df: pl.DataFrame,
    group_col: str,
    value_col: str = "value",
    agg: str = "sum",
) -> pl.DataFrame:
    """Aggregate data by a column with caching.

    Args:
        df: Input DataFrame.
        group_col: Column to group by.
        value_col: Column to aggregate.
        agg: Aggregation function.

    Returns:
        Aggregated DataFrame.
    """
    if df.is_empty():
        return pl.DataFrame()

    agg_funcs = {
        "sum": pl.col(value_col).sum(),
        "mean": pl.col(value_col).mean(),
        "count": pl.len(),
    }

    agg_func = agg_funcs.get(agg, agg_funcs["sum"])

    return df.group_by(group_col).agg(agg_func.alias(value_col)).sort(value_col, descending=True)


def get_column_unique_values(df: pl.DataFrame, column: str) -> list:
    """Get unique values from a column.

    Args:
        df: Input DataFrame.
        column: Column name.

    Returns:
        List of unique values.
    """
    if column not in df.columns:
        return []

    return df[column].unique().sort().to_list()
