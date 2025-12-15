import streamlit as st
from dotenv import load_dotenv
from streamlit_app.styles import apply_custom_styles
from streamlit_app.layout import render_app

# 1. Load Env
load_dotenv()

# 2. Page Config -> CHANGE TO "wide"
st.set_page_config(
    page_title="Ad Creator Portal",
    page_icon="🎨",
    layout="wide"  # <--- MUST BE WIDE
)

# 3. Apply Styles & Render
apply_custom_styles()

if __name__ == "__main__":
    render_app()