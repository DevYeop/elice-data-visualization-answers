from pathlib import Path
import os

if "__file__" in globals():
    os.chdir(Path(__file__).resolve().parent)

import streamlit as st
import pandas as pd
from datetime import date

df = pd.read_csv("avocado.csv")
df['date'] = df['date'].apply(lambda x: date.fromisoformat(x))

# 날짜를 달력에서 선택할 수 있는 테이블을 출력합니다.

# 🦁 column_config: 데이터프레임의 컬럼 표시 방식 및 UI 설정
# 🦁 "date": 설정을 적용할 실제 데이터프레임의 컬럼명
# 🦁 DateColumn(): 해당 컬럼을 날짜 형식으로 표시 및 편집
# 🦁 "날짜": Streamlit 화면에 표시할 컬럼 제목 (원본 컬럼명은 변경되지 않음)
new_df = st.data_editor(df,
                        column_config={
                            "date":st.column_config.DateColumn("날짜")
                        })
