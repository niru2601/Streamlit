import pandas as pd
import streamlit as st
import numpy as np


Login = st.Page("Login.py", title="Login")
Home = st.Page("app.py", title="Home")
Chart = st.Page("Dataframe.py", title="Charts")

pg = st.navigation([Login,Home, Chart])
# st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()