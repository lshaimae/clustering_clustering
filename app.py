import streamlit as st
st.set_page_config(page_title="Clustering App", layout="wide",initial_sidebar_state="collapsed",page_icon="eclipse_8880901.png")
from pages.Home import home_page
from pages.clustering import clustering_page
from pages.about import about_page
from pages.contact import contact_page
#delete the sidebar

def go_to(page_name):
   """Change the actual page"""
   st.session_state.current_page = page_name
   st.query_params["page"] = page_name
st.markdown("""
    <style>
        [data-testid="stSidebar"] { display: none; }
        [data-testid="collapsedControl"] { display: none; }
    </style>
""", unsafe_allow_html=True)

if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

query_params=st.query_params
page=query_params.get("page","home")
#render select page 
if page == "home":
    home_page(go_to)
elif page == "clustering":
    clustering_page(go_to)
elif page=="about":
    about_page()
elif page=="contact":
    contact_page()
else:
    st.error("Page not found.")
