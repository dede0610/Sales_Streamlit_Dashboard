"""Main Streamlit application entry point."""

import streamlit as st

from src.config import get_settings
from src.data.loader import load_data
from src.styles.custom import inject_custom_css

settings = get_settings()

st.set_page_config(
    page_title=settings.app_title,
    page_icon=settings.app_icon,
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_custom_css()

try:
    df = load_data(settings.data_file)
    st.session_state["df"] = df
except FileNotFoundError:
    st.error("Fichier de données non trouvé. Exécutez `make refresh-data`.")
    st.stop()

pg = st.navigation(
    [
        st.Page("pages/01_overview.py", title="Overview", icon="📊"),
        st.Page("pages/02_details.py", title="Details", icon="📋"),
    ]
)

pg.run()
