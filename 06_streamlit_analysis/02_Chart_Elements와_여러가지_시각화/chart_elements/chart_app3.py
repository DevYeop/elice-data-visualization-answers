from pathlib import Path
import os

if "__file__" in globals():
    os.chdir(Path(__file__).resolve().parent)

import streamlit as st
import pandas as pd
from datetime import date

df = pd.read_csv("avocado.csv")
df['date'] = df['date'].apply(lambda x: date.fromisoformat(x))

plot_table = {
    "geography": [
        "Boston",
        "California",
        "Los Angeles"
    ]
}

# bar chart를 위한 pivot table을 만듭니다.
pivot_df = pd.pivot_table(df, index="date",columns=["geography","type"])

# 지역과 유형을 하나의 열 이름으로 합쳐 Streamlit 차트에 전달합니다.
chart_data = pivot_df["average_price"][plot_table["geography"]]
chart_data.columns = [f"{region} ({kind})" for region, kind in chart_data.columns]
st.bar_chart(chart_data)
