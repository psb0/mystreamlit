import streamlit as st

x = st.slider('Select a Value')
st.write(x, 'squared is', x*x)
