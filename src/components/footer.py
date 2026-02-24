"""Footer component with credits."""

from datetime import datetime

import streamlit as st


def render_footer(
    data_source: str | None = None,
    last_update: datetime | None = None,
    author: str | None = None,
) -> None:
    """Render the app footer.

    Args:
        data_source: Name or URL of the data source.
        last_update: Date of last data update.
        author: Author name.
    """
    st.divider()

    cols = st.columns(3)

    with cols[0]:
        if data_source:
            st.caption(f"📁 Data : {data_source}")

    with cols[1]:
        if last_update:
            date_str = last_update.strftime("%d/%m/%Y")
            st.caption(f"🔄 Last Update : {date_str}")
        else:
            st.caption(f"🔄 Last Update : {datetime.now().strftime('%d/%m/%Y')}")

    with cols[2]:
        if author:
            st.caption(f"👤 {author}")
        else:
            st.caption("Made with Streamlit")
