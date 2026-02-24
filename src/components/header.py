"""Header component with logo and title."""

import streamlit as st

from src.config import get_settings


def render_header(title: str | None = None, subtitle: str | None = None) -> None:
    """Render the app header with logo and title.

    Args:
        title: Optional custom title (uses settings if not provided).
        subtitle: Optional subtitle.
    """
    settings = get_settings()

    if title is None:
        title = settings.app_title

    col1, col2 = st.columns([1, 4])

    with col1:
        if settings.logo_path:
            try:
                st.image(settings.logo_path, width=80)
            except FileNotFoundError:
                st.markdown("📊")
        else:
            st.markdown("# 📊")

    with col2:
        st.markdown(f"# {title}")
        if subtitle:
            st.markdown(f"*{subtitle}*")

    st.divider()


def render_page_header(title: str, description: str | None = None) -> None:
    """Render a page-level header.

    Args:
        title: Page title.
        description: Optional page description.
    """
    st.markdown(f"## {title}")
    if description:
        st.markdown(f"*{description}*")
    st.markdown("")
