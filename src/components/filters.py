"""Sidebar filter components."""

from typing import Any

import polars as pl
import streamlit as st


def render_filter_sidebar(
    df: pl.DataFrame,
    date_col: str = "date",
    category_col: str | None = "category",
    region_col: str | None = None,
) -> dict[str, Any]:
    """Render standard filters in the sidebar.

    Args:
        df: DataFrame to filter.
        date_col: Name of date column.
        category_col: Optional category column for filtering.
        region_col: Optional region column for filtering.

    Returns:
        Dictionary of filter values.
    """
    filters = {}

    st.sidebar.markdown("### 🔍 Filters")

    if date_col in df.columns:
        date_min = df[date_col].min()
        date_max = df[date_col].max()

        if date_min and date_max:
            col1, col2 = st.sidebar.columns(2)
            with col1:
                start_date = st.date_input(
                    "From",
                    value=date_min,
                    min_value=date_min,
                    max_value=date_max,
                    key="filter_start_date",
                )
            with col2:
                end_date = st.date_input(
                    "To",
                    value=date_max,
                    min_value=date_min,
                    max_value=date_max,
                    key="filter_end_date",
                )
            filters["start_date"] = start_date
            filters["end_date"] = end_date

    if category_col and category_col in df.columns:
        categories = ["All"] + sorted(df[category_col].unique().to_list())
        selected_category = st.sidebar.selectbox(
            "Category",
            options=categories,
            key="filter_category",
        )
        if selected_category != "All":
            filters["category"] = selected_category

    if region_col and region_col in df.columns:
        regions = ["All"] + sorted(df[region_col].unique().to_list())
        selected_region = st.sidebar.selectbox(
            "Region",
            options=regions,
            key="filter_region",
        )
        if selected_region != "All":
            filters["region"] = selected_region

    return filters


def apply_filters(
    df: pl.DataFrame, filters: dict[str, Any], date_col: str = "date"
) -> pl.DataFrame:
    """Apply filters to a DataFrame.

    Args:
        df: DataFrame to filter.
        filters: Dictionary of filter values.
        date_col: Name of date column.

    Returns:
        Filtered DataFrame.
    """
    filtered_df = df

    if "start_date" in filters and date_col in df.columns:
        filtered_df = filtered_df.filter(pl.col(date_col) >= filters["start_date"])

    if "end_date" in filters and date_col in df.columns:
        filtered_df = filtered_df.filter(pl.col(date_col) <= filters["end_date"])

    if "category" in filters and "category" in df.columns:
        filtered_df = filtered_df.filter(pl.col("category") == filters["category"])

    if "region" in filters and "region" in df.columns:
        filtered_df = filtered_df.filter(pl.col("region") == filters["region"])

    return filtered_df


def render_multiselect_filter(
    df: pl.DataFrame,
    column: str,
    label: str,
    default: list | None = None,
) -> list:
    """Render a multiselect filter.

    Args:
        df: DataFrame.
        column: Column name.
        label: Display label.
        default: Default selected values.

    Returns:
        List of selected values.
    """
    if column not in df.columns:
        return []

    options = sorted(df[column].unique().to_list())

    if default is None:
        default = options

    return st.sidebar.multiselect(
        label,
        options=options,
        default=default,
        key=f"multiselect_{column}",
    )


def render_slider_filter(
    df: pl.DataFrame,
    column: str,
    label: str,
) -> tuple:
    """Render a range slider filter for numeric values.

    Args:
        df: DataFrame.
        column: Column name.
        label: Display label.

    Returns:
        Tuple of (min, max) values.
    """
    if column not in df.columns:
        return (None, None)

    min_val = float(df[column].min())
    max_val = float(df[column].max())

    return st.sidebar.slider(
        label,
        min_value=min_val,
        max_value=max_val,
        value=(min_val, max_val),
        key=f"slider_{column}",
    )
