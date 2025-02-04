import pandas as pd
import streamlit as st
import numpy as np




chart_data = pd.DataFrame(np.random.randn(20, 2), columns=["Data_Points", "Data_value"])
st.bar_chart(chart_data)


