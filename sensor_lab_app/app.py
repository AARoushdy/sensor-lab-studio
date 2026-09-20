"""Sensor Characterization & Machine-Learning Studio  -  entry point.

Run with:   streamlit run app.py
"""
import streamlit as st

from core import branding, help_ui, viz

st.set_page_config(page_title="Sensor Lab Studio", page_icon=str(branding.ASSETS / "logo_placeholder.png"),
                   layout="wide", initial_sidebar_state="expanded")

try:
    st.logo(str(branding.find_logo()), size="large")
except Exception:                                    # unsupported logo format -> fall back to placeholder
    st.logo(str(branding.ASSETS / "logo_placeholder.png"), size="large")

try:
    NATIVE = st.context.theme.type or "light"         # the theme Streamlit itself is showing (system setting / menu)
except Exception:                                      # noqa: BLE001
    NATIVE = "light"

# Appearance button (sidebar): Auto = follow the computer, or force Light / Dark.
_choice = st.sidebar.segmented_control("Appearance", ["Auto", "Light", "Dark"], default="Auto", key="appearance",
                                       help="Auto follows your computer's light/dark setting. Choose Light or Dark to override it.")
WANT = NATIVE if _choice in (None, "Auto") else _choice.lower()
viz.set_theme(NATIVE)                                  # charts are drawn for the native theme ...
st.markdown(branding.css(NATIVE) + (branding.INVERT_CSS if WANT != NATIVE else ""),   # ... and flipped if you chose the other one
            unsafe_allow_html=True)

pages = [
    st.Page("views/home.py", title="Home", icon=":material/home:", default=True),
    st.Page("views/sensor_lab.py", title="Sensor Lab", icon=":material/sensors:"),
    st.Page("views/ml_studio.py", title="ML Studio", icon=":material/psychology:"),
    st.Page("views/theory.py", title="Theory", icon=":material/menu_book:"),
    st.Page("views/glossary.py", title="Glossary", icon=":material/help:"),
]
APP_VERSION = "2026-09-21 appearance-button"
nav = st.navigation(pages)
help_ui.sidebar_toggle()
st.sidebar.caption(f"Version {APP_VERSION} · showing {WANT}")
nav.run()
