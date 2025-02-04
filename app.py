import streamlit as st
import pandas as pd
import numpy as np


name = st.text_input("Enter your name")
st.title(f'Hello, {name}!')
st.subheader("Ready To Explore")
st.write('**Welcome to your first Streamlit app!**')
st.text('check my first streamlit page just for You....')
st.markdown("---")
st.markdown("  - streamlit **_User Interface_**")
st.markdown("click on [Duck](https://duckduckgo.com)")


file = st.file_uploader("Upload a CSV file", type="csv",help="Please upload a CSV file.")
if file:
    df = pd.read_csv(file)
    filter = df[(df['Data_Points']>1400)]
    st.write(filter)

    print(df)


else:
    st.text('Enter correct file')















