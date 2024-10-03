import streamlit as st
from PIL import Image
from pages import page1
from pages import page2
from pages import page3

class MultiApp:
    def __init__(self):
        self.apps = []
        
    def add_app(self, title, func):
        self.apps.append({title: title, "function": func})
        
    def run(self):
        img = Image.open(r"img\techclub_logo.png")
        st.set_page_config(
            page_title="NOVA Tech Club",
            page_icon=img,
            layout="wide"
        )
        
        st.sidebar.markdown("## Main Menu")
        app = st.sidebar.selectbox(
            "Select Page", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")
        app["function"]()

app = MultiApp()

app.add_app("Home Page", page1)
app.add_app("Current Projects", page2)
app.add_app("Achievements", page3)

app.run()