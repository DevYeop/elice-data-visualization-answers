from pathlib import Path
import os

if "__file__" in globals():
    os.chdir(Path(__file__).resolve().parent)

import streamlit as st
import pandas as pd
import plotly.express  as px

# 선택한 자치구의 평균과 시간에 따른 변화를 그립니다.
def bar_chart(*geo):
    bar_df = edited_df[edited_df["선택"]]
    fig = px.bar(bar_df, y="미세먼지", color="지역구",
                 title="서울시 구별 미세먼지", hover_data=["미세먼지"])
    return fig

def line_chart(*geo):
    line_df = df[df["구분"].apply(lambda x: x in geo)]
    fig = px.line(line_df, x="일시", y="초미세먼지(PM2.5)",
                  title="서울시 구별 미세먼지", color="구분",
                  line_group="구분", hover_name="구분")
    return fig


# 페이지 구성
df = pd.read_csv(Path(__file__).resolve().parents[2] / "seoul.csv.gz")
st.title("서울시 미세먼지 분포")

pivot_table = pd.pivot_table(df,index="구분",values=["미세먼지(PM10)","초미세먼지(PM2.5)"],aggfunc="mean")
pivot_table["선택"] = pivot_table["미세먼지(PM10)"].apply(lambda x: False)
pivot_table[["미세먼지","초미세먼지"]] = pivot_table[["미세먼지(PM10)","초미세먼지(PM2.5)"]]
del pivot_table["미세먼지(PM10)"]
del pivot_table["초미세먼지(PM2.5)"]


col1, col2 = st.columns([0.5,0.5])




with col1:
    st.write("\n\n")
    edited_df = st.data_editor(pivot_table)

edited_df["지역구"] = edited_df.index
select = list(edited_df[edited_df["선택"]]["지역구"])


with col2:
    tab1,tab2 = st.tabs(["Bar chart","Line chart"])

    with tab1:
        st.plotly_chart(bar_chart(*select))

    with tab2:
        st.plotly_chart(line_chart(*select))
