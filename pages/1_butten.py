import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

st.title("📍 부산 지역 히트맵 (Folium)")

# 예시 위경도 + 가중치 데이터 (부산 중심)
data = pd.DataFrame({
    "lat": [35.1796, 35.1800, 35.1766, 35.1811, 35.1750],
    "lon": [129.0756, 129.0800, 129.0720, 129.0785, 129.0690],
    "weight": [1, 3, 7, 2, 5]
})

# 지도 객체 생성
m = folium.Map(location=[35.1796, 129.0756], zoom_start=13)

# 히트맵 추가
HeatMap(data[["lat", "lon", "weight"]]).add_to(m)

# Streamlit에 표시
st_data = st_folium(m, width=700, height=500)
