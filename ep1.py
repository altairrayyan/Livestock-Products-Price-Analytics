import streamlit as st

pg = st.navigation([
    st.Page("PersProject.py", title="Dashboard"),
    st.Page("perbandingan.py", title="Perbandingan"),
])
pg.run()