import streamlit as st

st.set_page_config(
    page_title="Student Analytics Dashboard",
    page_icon="🎓",
    layout="wide"
)

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title("🎓 Student Data Analysis Dashboard")

st.markdown("""
### Welcome to Student Analytics System

This dashboard helps analyze:

✔ Academic performance  
✔ Attendance impact  
✔ Grade distribution  
✔ Student insights
""")

st.success("Navigate using the sidebar")
