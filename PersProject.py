import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")
st.markdown("""
    <style>
        h1 { font-size: 48px !important; }
        h2 { font-size: 30px !important; }
        h3 { font-size: 20px !important; }
    </style>
""", unsafe_allow_html=True)

def CV(hargaS):
    ceve1 = np.std(hargaS)/np.mean(hargaS)
    if ceve1 <= 0.1:
        market1 = "Really Safe"
        return market1, ceve1
    elif 0.1 < ceve1 <= 0.25:
        market2 = "Safe"
        return market2, ceve1
    else:
        market3 = "Not Safe"
        return market3, ceve1


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


tahun = sorted(dataframe['Tahun'].unique().tolist())
ternak = dataframe['filter'].unique().tolist()

st.title("Livestock Products Price Analytics Dashboard")

with st.sidebar:
    st.logo("abdullatieff.png", size="large")
    selectbox1 = st.selectbox(label="Tahun", options=tahun, width=100)
    radio1 = st.radio(label="Komoditas", options=ternak, width=100)
    pills1 = st.pills(label="Result Type", options=["Rata-Rata", "Standard Deviation", "Median"], default="Rata-Rata")

bulan_order = ["Januari","Februari","Maret","April","Mei","Juni",
               "Juli","Agustus","September","Oktober","November","Desember"]

dfilter = dataframe[
    (dataframe['filter'] == radio1) &
    (dataframe['Tahun'] == selectbox1)
].copy()
dfilter['Bulan'] = pd.Categorical(dfilter['Bulan'], categories=bulan_order, ordered=True)
dfilter = dfilter.sort_values('Bulan').reset_index(drop=True)
harga = dfilter['Harga'].tolist()
df_grafik = pd.DataFrame({"Bulan": dfilter['Bulan'].tolist(), "Harga": harga})
dtabel = df_grafik.copy()
dtabel["Harga"] = dtabel["Harga"].apply(lambda x: f"Rp{x:,}")

hasilcv, cvvls = CV(harga)
if hasilcv == "Really Safe":
    st.success(f"Harga sangat stabil — aman untuk UMKM | CV: {cvvls*100:.1f}%")
elif hasilcv == "Safe":
    st.warning(f"Harga cukup berfluktuasi — perlu perhatian | CV: {cvvls*100:.1f}%")
else:
    st.error(f"Harga sangat tidak stabil — berisiko bagi UMKM | CV: {cvvls*100:.1f}%")

col1, col2 = st.columns(spec=[0.7, 0.3], gap="small", vertical_alignment="top", border=True, width="stretch")

with col1:
    st.subheader("Data Table:")
    st.dataframe(dtabel)

with col2:
    st.subheader("Mean, Standard Deviation, or Median:")
    if pills1 == "Rata-Rata":
        st.metric(label="Mean", value=f"Rp. {int(np.mean(harga)):,}")
    elif pills1 == "Median":
        st.metric(label="Median", value=f"Rp. {int(np.median(harga)):,}")
    else:
        st.metric(label="Standard Deviation", value=f"Rp. {int(np.std(harga)):,}")

st.subheader("Price Trend Graph")
figure = px.line(df_grafik, x="Bulan", y="Harga", title=f"Harga per Bulan - {selectbox1}")
st.plotly_chart(figure, use_container_width=True)
