import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.markdown("""
    <style>
        h1 { font-size: 48px !important; }
        h2 { font-size: 30px !important; }
        h3 { font-size: 20px !important; }
    </style>
""", unsafe_allow_html=True)

try:
    dataframe = pd.read_csv('BPNCSV.csv', sep=';')
    dataframe['Harga'] = dataframe['Harga'].str.replace('Rp', '').str.replace('.', '').str.strip()
    dataframe['Harga'] = pd.to_numeric(dataframe['Harga'], errors='coerce')
    dataframe = dataframe.dropna(subset=['Harga'])
    dataframe = dataframe.reset_index(drop=True)
    dataframe['Harga'] = dataframe['Harga'].astype(int)

except FileNotFoundError:
    st.error("File kgk ada")
    st.stop()

with st.sidebar:
    st.logo("abdullatieff.png", size="large")

bulan_order = ["Januari","Februari","Maret","April","Mei","Juni",
               "Juli","Agustus","September","Oktober","November","Desember"]

ternak = dataframe['filter'].unique().tolist()

for komoditas in ternak:
    df_filtered = dataframe[dataframe['filter'] == komoditas].copy()
    df_filtered['Bulan'] = pd.Categorical(df_filtered['Bulan'], categories=bulan_order, ordered=True)
    df_filtered = df_filtered.sort_values(['Tahun', 'Bulan']).reset_index(drop=True)
    df_filtered['Tahun'] = df_filtered['Tahun'].astype(str)
    figure = px.line(df_filtered, x="Bulan", y="Harga", color="Tahun", title=komoditas)
    st.plotly_chart(figure, use_container_width=True)

