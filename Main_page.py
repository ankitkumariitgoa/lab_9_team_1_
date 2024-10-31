import streamlit as st
from streamlit_option_menu import option_menu
import Home
import snake_ladder
import About_us
# st.set_page_config(layout="wide")
st.set_page_config(
    page_title="Project",
    layout='wide'
)
class MultiApp:
    def __init__(self) -> None:
        self.apps=[]
    def add_app(self,title,func):
        self.apps.append({
            'title':title,
            'function':func
        })
    def run():
        with st.sidebar:
            app=option_menu(
                menu_title='Project',
                options=['Home','snake_ladder','About_us'],
                icons=['house-fill','person-circle','person-circle'],
                default_index=0
            )
        if app=='Home':
            Home.run()
        if app=='snake_ladder':
            snake_ladder.run()
        if app=='About_us':
            About_us.run()
    run()
