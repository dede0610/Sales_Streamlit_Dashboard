"""Custom CSS styles - Sunset Analytics Theme."""

CUSTOM_CSS = """
<style>
    /* ===== IMPORTS ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* ===== CSS VARIABLES ===== */
    :root {
        --primary: #7C3AED;
        --primary-dark: #6D28D9;
        --secondary: #EC4899;
        --accent: #F97316;
        --bg-main: #FAFAFA;
        --bg-surface: #F5F3FF;
        --bg-card: #FFFFFF;
        --text-primary: #1E1B4B;
        --text-secondary: #6B7280;
        --border: #E5E7EB;
        --shadow: rgba(124, 58, 237, 0.1);
        --gradient-primary: linear-gradient(135deg, #7C3AED 0%, #EC4899 100%);
        --gradient-accent: linear-gradient(135deg, #F97316 0%, #EC4899 100%);
    }

    /* ===== GLOBAL ===== */
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
    }

    /* ===== HEADER ===== */
    .app-header {
        background: var(--gradient-primary);
        padding: 1.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px var(--shadow);
    }

    .app-header h1 {
        color: white !important;
        font-weight: 700;
        margin: 0;
        font-size: 1.8rem;
    }

    .app-header p {
        color: rgba(255, 255, 255, 0.9);
        margin: 0.5rem 0 0 0;
    }

    /* ===== KPI CARDS ===== */
    [data-testid="stMetric"] {
        background: var(--bg-card);
        border-radius: 16px;
        padding: 1.25rem;
        border: 1px solid var(--border);
        box-shadow: 0 4px 20px var(--shadow);
        transition: all 0.3s ease;
    }

    [data-testid="stMetric"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px var(--shadow);
    }

    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    [data-testid="stMetricLabel"] {
        font-size: 0.875rem;
        font-weight: 500;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    [data-testid="stMetricDelta"] svg {
        display: none;
    }

    [data-testid="stMetricDelta"] > div {
        font-weight: 600;
        padding: 4px 8px;
        border-radius: 6px;
        font-size: 0.8rem;
    }

    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #F5F3FF 0%, #FAFAFA 100%);
        border-right: 1px solid var(--border);
    }

    [data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {
        color: var(--primary);
        font-weight: 600;
    }

    /* Sidebar logo container */
    .sidebar-logo {
        text-align: center;
        padding: 1rem;
        margin-bottom: 1rem;
        border-bottom: 1px solid var(--border);
    }

    .sidebar-logo img {
        max-width: 150px;
        height: auto;
    }

    /* ===== DATAFRAMES ===== */
    [data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid var(--border);
        box-shadow: 0 4px 20px var(--shadow);
    }

    [data-testid="stDataFrame"] [data-testid="glideDataEditor"] {
        border-radius: 12px;
    }

    /* ===== CHARTS ===== */
    .js-plotly-plot {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 20px var(--shadow);
    }

    /* ===== BUTTONS ===== */
    .stButton > button {
        background: var(--gradient-primary);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px var(--shadow);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px var(--shadow);
    }

    .stButton > button:active {
        transform: translateY(0);
    }

    /* Secondary button */
    .stButton > button[kind="secondary"] {
        background: white;
        color: var(--primary);
        border: 2px solid var(--primary);
    }

    /* ===== DOWNLOAD BUTTON ===== */
    .stDownloadButton > button {
        background: var(--gradient-accent);
        border: none;
        color: white;
    }

    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: var(--bg-surface);
        padding: 4px;
        border-radius: 12px;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 12px 24px;
        background: transparent;
        color: var(--text-secondary);
        font-weight: 500;
        transition: all 0.2s ease;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: var(--primary);
        background: rgba(124, 58, 237, 0.1);
    }

    .stTabs [aria-selected="true"] {
        background: var(--gradient-primary) !important;
        color: white !important;
        box-shadow: 0 4px 15px var(--shadow);
    }

    /* ===== EXPANDER ===== */
    .streamlit-expanderHeader {
        background: var(--bg-surface);
        border-radius: 10px;
        font-weight: 500;
        transition: all 0.2s ease;
    }

    .streamlit-expanderHeader:hover {
        background: rgba(124, 58, 237, 0.1);
    }

    /* ===== SELECT BOX ===== */
    .stSelectbox > div > div {
        border-radius: 10px;
        border-color: var(--border);
    }

    .stSelectbox > div > div:focus-within {
        border-color: var(--primary);
        box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.2);
    }

    /* ===== MULTISELECT ===== */
    .stMultiSelect > div > div {
        border-radius: 10px;
    }

    .stMultiSelect [data-baseweb="tag"] {
        background: var(--gradient-primary);
        border-radius: 6px;
    }

    /* ===== DATE INPUT ===== */
    .stDateInput > div > div {
        border-radius: 10px;
    }

    /* ===== SLIDER ===== */
    .stSlider > div > div > div > div {
        background: var(--gradient-primary);
    }

    /* ===== PROGRESS BAR ===== */
    .stProgress > div > div > div {
        background: var(--gradient-primary);
    }

    /* ===== ALERTS / INFO BOXES ===== */
    .stAlert {
        border-radius: 12px;
        border: none;
    }

    /* ===== DIVIDER ===== */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--border), transparent);
        margin: 2rem 0;
    }

    /* ===== FOOTER ===== */
    .app-footer {
        text-align: center;
        padding: 1.5rem;
        margin-top: 3rem;
        border-top: 1px solid var(--border);
        color: var(--text-secondary);
        font-size: 0.875rem;
    }

    .app-footer a {
        color: var(--primary);
        text-decoration: none;
        font-weight: 500;
    }

    /* ===== HIDE STREAMLIT BRANDING ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* ===== ANIMATIONS ===== */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .main .block-container > div {
        animation: fadeIn 0.4s ease-out;
    }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem;
        }

        [data-testid="stMetricValue"] {
            font-size: 1.5rem;
        }
    }
</style>
"""


def inject_custom_css() -> None:
    """Inject custom CSS into the Streamlit app."""
    import streamlit as st

    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def render_header(title: str, subtitle: str | None = None) -> None:
    """Render a styled header with gradient background."""
    import streamlit as st

    subtitle_html = f"<p>{subtitle}</p>" if subtitle else ""
    st.markdown(
        f"""
        <div class="app-header">
            <h1>{title}</h1>
            {subtitle_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer(text: str = "Built with Streamlit") -> None:
    """Render a styled footer."""
    import streamlit as st

    st.markdown(
        f"""
        <div class="app-footer">
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_logo(logo_path: str | None = None, width: int = 150) -> None:
    """Render logo in sidebar."""
    from pathlib import Path

    import streamlit as st

    if logo_path and Path(logo_path).exists():
        st.sidebar.markdown(
            f"""
            <div class="sidebar-logo">
                <img src="data:image/png;base64,{_get_base64_image(logo_path)}" width="{width}">
            </div>
            """,
            unsafe_allow_html=True,
        )


def _get_base64_image(image_path: str) -> str:
    """Convert image to base64 string."""
    import base64
    from pathlib import Path

    with open(Path(image_path), "rb") as f:
        return base64.b64encode(f.read()).decode()


# Theme colors for Plotly charts
PLOTLY_COLORS = {
    "primary": "#7C3AED",
    "secondary": "#EC4899",
    "accent": "#F97316",
    "success": "#10B981",
    "warning": "#F59E0B",
    "danger": "#EF4444",
    "palette": ["#7C3AED", "#EC4899", "#F97316", "#10B981", "#06B6D4", "#8B5CF6"],
}


def get_plotly_template() -> dict:
    """Get Plotly template matching the Sunset Analytics theme."""
    return {
        "layout": {
            "font": {"family": "Inter, sans-serif", "color": "#1E1B4B"},
            "paper_bgcolor": "rgba(0,0,0,0)",
            "plot_bgcolor": "rgba(0,0,0,0)",
            "colorway": PLOTLY_COLORS["palette"],
            "title": {"font": {"size": 18, "color": "#1E1B4B"}},
            "xaxis": {
                "gridcolor": "#E5E7EB",
                "linecolor": "#E5E7EB",
                "tickfont": {"color": "#6B7280"},
            },
            "yaxis": {
                "gridcolor": "#E5E7EB",
                "linecolor": "#E5E7EB",
                "tickfont": {"color": "#6B7280"},
            },
            "legend": {"bgcolor": "rgba(0,0,0,0)"},
        }
    }
