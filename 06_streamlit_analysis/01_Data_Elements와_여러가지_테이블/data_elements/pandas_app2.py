from pathlib import Path
import os

if "__file__" in globals():
    os.chdir(Path(__file__).resolve().parent)

import streamlit as st
import pandas as pd
from datetime import date

df = pd.read_csv("avocado.csv")

# 🦁 fromisoformat을 통해 문자열을 날짜 데이터 형식으로 바꿔줍니다.
df['date'] = df['date'].apply(lambda x: date.fromisoformat(x))

# '수정 가능한 테이블'을 출력합니다.
st.data_editor(df)
