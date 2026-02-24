"""Details page - Detailed data exploration."""

import polars as pl
import streamlit as st

from src.components.filters import apply_filters, render_filter_sidebar
from src.components.footer import render_footer
from src.components.header import render_page_header


def main():
    df = st.session_state.get("df")

    if df is None or df.is_empty():
        st.warning("No data available")
        return

    st.markdown("# 📋 Details")
    st.markdown("Explore the detailed data with filters.")

    filters = render_filter_sidebar(df, category_col="category", region_col="region")
    filtered_df = apply_filters(df, filters)

    if filtered_df.is_empty():
        st.warning("No data for selected filters")
        return

    st.markdown(f"**{len(filtered_df):,}** records found")

    render_page_header("Data Table")

    display_cols = ["date", "name", "category", "region", "value", "quantity"]
    available_cols = [c for c in display_cols if c in filtered_df.columns]

    display_df = filtered_df.select(available_cols)

    col_names = {
        "date": "Date",
        "name": "Product",
        "category": "Category",
        "region": "Region",
        "value": "Value",
        "quantity": "Quantity",
    }
    display_df = display_df.rename({k: v for k, v in col_names.items() if k in available_cols})

    st.dataframe(
        display_df.to_pandas(),
        width="stretch",
        hide_index=True,
        column_config={
            "Value": st.column_config.NumberColumn(format="%.2f $"),
            "Quantity": st.column_config.NumberColumn(format="%d"),
        },
    )

    render_page_header("Statistics by Category")

    category_stats = (
        filtered_df.group_by("category")
        .agg(
            [
                pl.col("value").sum().alias("total"),
                pl.col("value").mean().alias("average"),
                pl.len().alias("count"),
            ]
        )
        .sort("total", descending=True)
    )

    category_stats = category_stats.rename(
        {
            "category": "Category",
            "total": "Total",
            "average": "Average",
            "count": "Count",
        }
    )

    st.dataframe(
        category_stats.to_pandas(),
        width="stretch",
        hide_index=True,
        column_config={
            "Total": st.column_config.NumberColumn(format="%.2f $"),
            "Average": st.column_config.NumberColumn(format="%.2f $"),
            "Count": st.column_config.NumberColumn(format="%d"),
        },
    )

    render_page_header("Statistics by Region")

    if "region" in filtered_df.columns:
        region_stats = (
            filtered_df.group_by("region")
            .agg(
                [
                    pl.col("value").sum().alias("total"),
                    pl.col("value").mean().alias("average"),
                    pl.len().alias("count"),
                ]
            )
            .sort("total", descending=True)
        )

        region_stats = region_stats.rename(
            {
                "region": "Region",
                "total": "Total",
                "average": "Average",
                "count": "Number",
            }
        )

        st.dataframe(
            region_stats.to_pandas(),
            width="stretch",
            hide_index=True,
            column_config={
                "Total": st.column_config.NumberColumn(format="%.2f $"),
                "Average": st.column_config.NumberColumn(format="%.2f $"),
                "Number": st.column_config.NumberColumn(format="%d"),
            },
        )

    render_page_header("Export")

    col1, col2, col3 = st.columns(3)

    with col1:
        csv = filtered_df.write_csv()
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="data_export.csv",
            mime="text/csv",
        )

    with col2:
        if st.button("🔄 Reinitialise filters"):
            st.rerun()

    render_footer(data_source="Dummies Data")


if __name__ == "__main__":
    main()
