"""Overview page - Main dashboard view."""

import plotly.express as px
import polars as pl
import streamlit as st

from src.components.filters import apply_filters, render_filter_sidebar
from src.components.footer import render_footer
from src.components.header import render_header, render_page_header
from src.components.kpi_card import render_kpi_grid
from src.data.loader import aggregate_by_column, compute_summary
from src.utils.formatting import format_currency, format_percentage


def main():
    df = st.session_state.get("df")

    if df is None or df.is_empty():
        st.warning("Aucune donnée disponible")
        return

    render_header(subtitle="Sales and Performance Overview")

    filters = render_filter_sidebar(df, category_col="category", region_col="region")
    filtered_df = apply_filters(df, filters)

    if filtered_df.is_empty():
        st.warning("Aucune donnée pour les filtres sélectionnés")
        return

    st.markdown(f"**{len(filtered_df):,}** records found")

    summary = compute_summary(filtered_df)
    summary_total = compute_summary(df)

    growth = None
    if summary_total.get("total") and summary.get("total"):
        prev_total = summary_total["total"]
        curr_total = summary["total"]
        if prev_total > 0:
            growth = (curr_total - prev_total) / prev_total

    kpis = [
        {
            "label": "Total Sales",
            "value": format_currency(summary.get("total", 0), symbol="$"),
            "delta": format_percentage(growth) if growth else None,
            "delta_color": "normal" if growth and growth > 0 else "inverse",
        },
        {
            "label": "Average Value",
            "value": format_currency(summary.get("mean", 0), symbol="$"),
        },
        {
            "label": "Transactions",
            "value": f"{summary.get('count', 0):,}",
        },
        {
            "label": "Maximum Value",
            "value": format_currency(summary.get("max", 0), symbol="$"),
        },
    ]

    render_kpi_grid(kpis, columns=4)

    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:
        render_page_header("Time Series")

        daily = filtered_df.group_by("date").agg(pl.col("value").sum()).sort("date")

        fig_trend = px.line(
            daily.to_pandas(),
            x="date",
            y="value",
            title="",
            markers=True,
        )
        fig_trend.update_layout(
            template="plotly_white",
            margin=dict(l=0, r=0, t=0, b=0),
            showlegend=False,
        )
        fig_trend.update_traces(line_color="#2563EB", line_width=2)
        st.plotly_chart(fig_trend, width="stretch")

    with col2:
        render_page_header("Category Distribution")

        by_category = aggregate_by_column(filtered_df, "category", "value", "sum")

        if not by_category.is_empty():
            fig_pie = px.pie(
                by_category.to_pandas(),
                values="value",
                names="category",
                title="",
            )
            fig_pie.update_layout(
                template="plotly_white",
                margin=dict(l=0, r=0, t=0, b=0),
            )
            fig_pie.update_traces(
                marker_colors=["#2563EB", "#10B981", "#F59E0B", "#EF4444", "#8B5CF6", "#6366F1"]
            )
            st.plotly_chart(fig_pie, width="stretch")

    st.markdown("")

    render_page_header("Top Performers")

    top_items = filtered_df.sort("value", descending=True).head(10)

    col_names = {"name": "Product", "category": "Category", "value": "Value", "region": "Region"}
    display_df = top_items.select(["name", "category", "region", "value"]).rename(col_names)

    st.dataframe(
        display_df.to_pandas(),
        width="stretch",
        hide_index=True,
    )

    render_footer(data_source="Données démo", author="Data Analytics Team")


if __name__ == "__main__":
    main()
