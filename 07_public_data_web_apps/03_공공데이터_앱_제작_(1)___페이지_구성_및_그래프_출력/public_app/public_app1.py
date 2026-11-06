from pathlib import Path
import os

if "__file__" in globals():
    os.chdir(Path(__file__).resolve().parent)

import streamlit as st
import pandas as pd
import plotly.express  as px

# 페이지 구성
df = pd.read_csv(Path(__file__).resolve().parents[2] / "seoul.csv.gz")
st.title("서울시 미세먼지 분포")

pivot_table = pd.pivot_table(df,index="구분",values=["미세먼지(PM10)","초미세먼지(PM2.5)"],aggfunc="mean")
pivot_table["선택"] = pivot_table["미세먼지(PM10)"].apply(lambda x: False)

# 화면을 두 열로 나눕니다.
col1, col2 = st.columns(2)


# 🦁 with: 특정 작업 환경(Context) 안에서 코드를 실행하는 Python 문법
# 🦁 Streamlit에서는 UI 요소를 특정 화면 영역에 배치할 때 사용
# 🦁 with 아래 들여쓰기된 코드들이 해당 영역에 배치됨
with col1:
    edited_df = st.data_editor(pivot_table)

with col2:
    tab1, tab2, tab3 = st.tabs(["Bar chart", "Line chart", "새로운 탭"])
    with tab1:
        st.title("bar")
    with tab2:
        st.title("line")
    with tab3:
        st.title("새로운 탭")
