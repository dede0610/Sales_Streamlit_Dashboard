"""KPI card component."""

import streamlit as st


def render_kpi_card(
    label: str,
    value: str,
    delta: str | None = None,
    delta_color: str = "normal",
    help_text: str | None = None,
) -> None:
    """Render a single KPI card using st.metric.

    Args:
        label: KPI label.
        value: KPI value.
        delta: Optional delta/change value.
        delta_color: Color for delta ("normal", "inverse", "off").
        help_text: Optional help text.
    """
    st.metric(
        label=label,
        value=value,
        delta=delta,
        delta_color=delta_color,
        help=help_text,
    )


def render_kpi_row(
    kpis: list[dict],
    columns: int = 4,
) -> None:
    """Render a row of KPI cards.

    Args:
        kpis: List of KPI dicts with keys: label, value, delta (optional), delta_color (optional).
        columns: Number of columns.
    """
    cols = st.columns(columns)

    for i, kpi in enumerate(kpis):
        with cols[i % columns]:
            render_kpi_card(
                label=kpi.get("label", ""),
                value=kpi.get("value", "-"),
                delta=kpi.get("delta"),
                delta_color=kpi.get("delta_color", "normal"),
                help_text=kpi.get("help"),
            )


def render_kpi_grid(
    kpis: list[dict],
    columns: int = 4,
) -> None:
    """Render a grid of KPI cards (multiple rows).

    Args:
        kpis: List of KPI dicts.
        columns: Number of columns per row.
    """
    for i in range(0, len(kpis), columns):
        row_kpis = kpis[i : i + columns]
        render_kpi_row(row_kpis, columns=columns)
