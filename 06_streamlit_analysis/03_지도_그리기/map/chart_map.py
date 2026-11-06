from pathlib import Path
import os

if "__file__" in globals():
    os.chdir(Path(__file__).resolve().parent)

import streamlit as st
import pandas as pd
from datetime import date

df = pd.read_csv("jeju_place.csv")

st.dataframe(df)

# lat, lon 열에 위도와 경도를 담습니다.
df[["lat", "lon"]] = df[["위도", "경도"]]

# 데이터프레임의 위치를 지도에 표시합니다.
st.map(df)
