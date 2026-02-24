"""Tests for data loader module."""

import tempfile
from datetime import date
from pathlib import Path

import polars as pl
import pytest


class TestLoadData:
    """Tests for load_data function."""

    def test_load_data_file_not_found(self):
        """Test loading non-existent file."""
        from src.data.loader import load_data

        with pytest.raises(FileNotFoundError):
            load_data("nonexistent.parquet")

    def test_load_data_success(self):
        """Test loading valid Parquet file."""
        from src.data.loader import load_data

        df = pl.DataFrame(
            {
                "date": [date(2025, 1, 1)],
                "value": [100.0],
            }
        )

        with tempfile.NamedTemporaryFile(suffix=".parquet", delete=False) as f:
            temp_path = f.name
            df.write_parquet(temp_path)

        try:
            loaded = load_data(temp_path)
            assert len(loaded) == 1
            assert "value" in loaded.columns
        finally:
            # Clear Streamlit cache before deleting file (avoids Windows lock)
            load_data.clear()
            Path(temp_path).unlink(missing_ok=True)


class TestComputeSummary:
    """Tests for compute_summary function."""

    def test_compute_summary_basic(self):
        """Test basic summary computation."""
        from src.data.loader import compute_summary

        df = pl.DataFrame(
            {
                "value": [100.0, 200.0, 300.0],
            }
        )

        summary = compute_summary(df)

        assert summary["total"] == 600.0
        assert summary["mean"] == 200.0
        assert summary["count"] == 3

    def test_compute_summary_empty(self):
        """Test with empty DataFrame."""
        from src.data.loader import compute_summary

        df = pl.DataFrame({"value": []})
        summary = compute_summary(df)

        assert summary == {}


class TestAggregateByColumn:
    """Tests for aggregate_by_column function."""

    def test_aggregate_sum(self):
        """Test sum aggregation."""
        from src.data.loader import aggregate_by_column

        df = pl.DataFrame(
            {
                "category": ["A", "B", "A"],
                "value": [100.0, 200.0, 150.0],
            }
        )

        result = aggregate_by_column(df, "category", "value", "sum")

        assert len(result) == 2
        cat_a = result.filter(pl.col("category") == "A")
        assert cat_a["value"].item() == 250.0

    def test_aggregate_empty(self):
        """Test with empty DataFrame."""
        from src.data.loader import aggregate_by_column

        df = pl.DataFrame({"category": [], "value": []})
        result = aggregate_by_column(df, "category")

        assert result.is_empty()
