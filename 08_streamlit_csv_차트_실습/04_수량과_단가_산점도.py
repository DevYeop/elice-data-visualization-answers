import pandas as pd
import plotly.express as px
import streamlit as st

st.title("수량과 단가의 관계")
st.write("같은 폴더의 물품_월별_더미.csv를 아래에 끌어다 놓으세요.")

# 1. CSV 파일을 선택하거나 끌어다 놓습니다.
file = st.file_uploader("CSV 파일 올리기", type="csv")

if file is not None:
    try:
        # 2. 파일을 데이터프레임으로 읽습니다.
        df = pd.read_csv(file, encoding="utf-8-sig")
        required = ["월", "품목", "수량", "단가"]
        if not all(column in df.columns for column in required):
            st.error("CSV에 월, 품목, 수량, 단가 열이 필요합니다.")
            st.stop()
        for column in ["월", "수량", "단가"]:
            df[column] = pd.to_numeric(df[column], errors="raise")
        if df.empty or df[required].isna().any().any():
            st.error("데이터가 비어 있거나 빈 칸이 있습니다.")
            st.stop()
        if (df[["수량", "단가"]] < 0).any().any():
            st.error("수량과 단가는 0 이상이어야 합니다.")
            st.stop()
    except (UnicodeDecodeError, pd.errors.ParserError, pd.errors.EmptyDataError, ValueError):
        st.error("CSV 파일의 인코딩과 숫자 데이터를 확인해 주세요. UTF-8 CSV를 사용하세요.")
        st.stop()

    # 3. 원본 데이터를 확인합니다.
    st.subheader("불러온 데이터")
    st.dataframe(df, hide_index=True)

    # 4. 차트에 필요한 데이터를 만들고 화면에 표시합니다.
    fig = px.scatter(df, x="수량", y="단가", color="품목", hover_data=["월"],
                     title="수량과 단가의 관계")
    st.plotly_chart(fig, use_container_width=True)
    st.caption("점 하나는 한 달의 한 품목을 뜻합니다. 단가는 가상의 값입니다.")
