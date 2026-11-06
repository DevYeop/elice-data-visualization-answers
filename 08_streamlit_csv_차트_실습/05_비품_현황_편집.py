import csv
from inspect import signature
from io import StringIO
import re

import pandas as pd
import streamlit as st


KEY_COLUMNS = ["기준월", "품목코드"]
QUANTITY_COLUMNS = ["보유수량", "기준수량"]
COLUMNS = [*KEY_COLUMNS, "품목명", *QUANTITY_COLUMNS]
MAX_QUANTITY = 999_999_999


def alt_if_supported(widget, description):
    # 이전 Streamlit 버전에는 일부 위젯의 alt 옵션이 없습니다.
    return {"alt": description} if "alt" in signature(widget).parameters else {}


def require_valid_rows(valid, message):
    invalid = ~valid.fillna(False)
    if invalid.any():
        rows = ", ".join(str(index + 1) for index in invalid.index[invalid][:5])
        raise ValueError(f"데이터 행 {rows}번을 확인하세요. {message}")


def validate_quantities(inventory):
    for column in QUANTITY_COLUMNS:
        values = pd.to_numeric(inventory[column], errors="coerce")
        valid = values.between(0, MAX_QUANTITY) & values.mod(1).eq(0)
        require_valid_rows(valid, f"{column}에 0부터 {MAX_QUANTITY:,}까지의 정수를 입력하세요.")
        inventory[column] = values.astype("int64")


def read_inventory(contents):
    try:
        reader = csv.reader(StringIO(contents.decode("utf-8-sig"), newline=""), strict=True)
        header = next(reader, [])
        if len(header) != len(COLUMNS) or set(header) != set(COLUMNS):
            raise ValueError(f"CSV에 다음 다섯 열이 필요합니다. {', '.join(COLUMNS)}")
        records = []
        for number, row in enumerate(reader, start=1):
            if len(row) != len(header):
                raise ValueError(f"데이터 행 {number}번의 열 개수가 제목 행과 다릅니다.")
            records.append([value.strip() for value in row])
    except UnicodeDecodeError as error:
        raise ValueError("UTF-8로 저장한 CSV를 올려 주세요.") from error
    except csv.Error as error:
        raise ValueError(f"CSV 형식을 확인해 주세요. 데이터 행 {max(1, reader.line_num - 1)}번 근처에서 읽을 수 없습니다.") from error

    if not records:
        raise ValueError("CSV에 데이터가 한 행 이상 필요합니다.")

    inventory = pd.DataFrame(records, columns=header)[COLUMNS]
    months = inventory["기준월"].str.fullmatch(r"[0-9]{4}-(0[1-9]|1[0-2])")
    require_valid_rows(months, "기준월을 2026-11처럼 입력하세요.")
    codes = inventory["품목코드"].str.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*")
    require_valid_rows(codes, "품목코드에는 영문, 숫자, 하이픈, 밑줄을 사용할 수 있습니다.")
    names = inventory["품목명"]
    valid_names = names.ne("") & ~names.str.startswith(("=", "+", "-", "@")) & ~names.str.contains(r"[\x00-\x1f]")
    require_valid_rows(valid_names, "품목명에 일반 텍스트를 입력하세요.")
    require_valid_rows(~inventory.duplicated(KEY_COLUMNS, keep=False), "같은 기준월과 품목코드가 중복됐습니다.")
    validate_quantities(inventory)
    return inventory


st.set_page_config(page_title="월별 비품 현황", layout="wide")
st.title("월별 비품 현황")
st.write("최신 CSV를 올려 수량을 수정하고, 팀에 전달할 수정본을 내려받으세요.")

uploaded = st.file_uploader("비품 현황 CSV 올리기", type="csv", max_upload_size=1)
if uploaded is None:
    st.info("처음 실습할 때는 비품현황_v01.csv를 올려 보세요.")
    st.stop()

try:
    inventory = read_inventory(uploaded.getvalue())
except ValueError as error:
    st.error(str(error))
    st.stop()

state = st.session_state
if state.get("inventory_file_id") != uploaded.file_id:
    state.inventory_file_id = uploaded.file_id
    # 검증 전에 편집기가 소수 입력을 정수로 잘라내지 않도록 합니다.
    state.inventory_draft = inventory.astype({column: "float64" for column in QUANTITY_COLUMNS})
    state.inventory_edit_month = None

draft = state.inventory_draft
month = st.selectbox(
    "편집할 월",
    sorted(inventory["기준월"].unique(), reverse=True),
    key=f"inventory_month_{uploaded.file_id}",
)
if state.inventory_edit_month != month:
    state.inventory_edit_month = month
    # 같은 월을 편집하는 동안에는 편집기에 처음 전달한 표를 유지합니다.
    state.inventory_editor_source = draft[draft["기준월"] == month].copy()

st.subheader(f"{month} 수량 수정")
st.caption("보유수량이나 기준수량을 수정하고 Enter를 누르면 아래 차트에 바로 반영됩니다.")
edited = st.data_editor(
    state.inventory_editor_source,
    hide_index=True,
    disabled=["기준월", "품목코드", "품목명"],
    column_config={
        column: st.column_config.NumberColumn(
            column, min_value=0, max_value=MAX_QUANTITY, step=1, required=True
        )
        for column in QUANTITY_COLUMNS
    },
    key=f"inventory_{uploaded.file_id}_{month}",
    **alt_if_supported(st.data_editor, "월별 비품 수량 편집 표"),
)
draft.loc[edited.index, QUANTITY_COLUMNS] = edited[QUANTITY_COLUMNS]
try:
    validate_quantities(edited)
except ValueError as error:
    st.error(str(error))
    st.stop()

st.subheader(f"{month} 현황")
monthly = edited.copy()
monthly["부족수량"] = (monthly["기준수량"] - monthly["보유수량"]).clip(lower=0)
shortages = monthly[monthly["부족수량"] > 0]

with st.container(horizontal=True):
    st.metric("품목 수", len(monthly))
    st.metric("부족 품목", len(shortages))
    st.metric("부족 수량", int(shortages["부족수량"].sum()))

monthly["품목"] = monthly["품목명"] + " (" + monthly["품목코드"] + ")"
st.bar_chart(
    monthly, x="품목", y=QUANTITY_COLUMNS, stack=False,
    **alt_if_supported(st.bar_chart, "품목별 보유수량과 기준수량 비교"),
)
if shortages.empty:
    st.success("선택한 월에 부족한 품목이 없습니다.")
else:
    st.dataframe(
        shortages[["품목코드", "품목명", *QUANTITY_COLUMNS, "부족수량"]],
        hide_index=True,
        **alt_if_supported(st.dataframe, "기준수량보다 부족한 품목 목록"),
    )

st.subheader("수정본 저장")
export_data = draft.copy()
try:
    validate_quantities(export_data)
except ValueError as error:
    st.error(f"다른 월의 수량을 수정한 뒤 내려받을 수 있습니다. {error}")
    st.stop()

version = re.fullmatch(r"비품현황_v([0-9]+)\.csv", uploaded.name)
next_version = int(version[1]) + 1 if version else 1
output_name = f"비품현황_v{next_version:02d}.csv"
st.caption(f"모든 월을 {output_name}에 담습니다. 배포한 수정본을 다음 작업 때 다시 올리세요.")
st.download_button(
    "수정본 CSV 내려받기",
    export_data.to_csv(index=False).encode("utf-8-sig"),
    file_name=output_name,
    mime="text/csv",
    on_click="ignore",
    type="primary",
)
