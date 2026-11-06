from pathlib import Path
import os

if "__file__" in globals():
    os.chdir(Path(__file__).resolve().parent)

import streamlit as st
import pandas as pd
from datetime import date

df = pd.read_csv("avocado.csv")
df['date'] = df['date'].apply(lambda x: date.fromisoformat(x))

# Boston, California, Los Angeles 에 대한 line chart를 갖는 그래프
plot_table = {
    "geography": [
        "Boston",
        "California",
        "Los Angeles"
    ]
}

line_chart = []

# 지역별 평균 가격을 선 그래프의 값으로 모읍니다.
for i in plot_table["geography"]:
    line_chart.append(list(df[df["geography"] == i]["average_price"]))

plot_table["line"] = line_chart

st.dataframe(plot_table,
             column_config={
                 "line": st.column_config.LineChartColumn(
                     "Average Price",
                     width="medium"
                 )
             })
