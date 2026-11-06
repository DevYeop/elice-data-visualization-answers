from pathlib import Path
import os

if "__file__" in globals():
    os.chdir(Path(__file__).resolve().parent)

import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px

df = pd.read_csv("avocado.csv")
df['date'] = df['date'].apply(lambda x: date.fromisoformat(x))




# 그래프를 그릴 지역을 선택합니다.
selected_geography = st.selectbox(label="Geography", options=df["geography"].unique())
submitted = st.button('Submit')

# 선택한 지역의 평균 가격을 Plotly로 표시합니다.
if submitted:
    filtered_avocado = df[df['geography'] == selected_geography]
    line_fig = px.line(filtered_avocado,
                       x="date", y="average_price",
                       color='type',
                       title=f'Avocado Prices in {selected_geography}')
    st.plotly_chart(line_fig)
