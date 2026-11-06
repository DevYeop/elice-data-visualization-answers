# %%
from pathlib import Path
import os

os.chdir(Path(__file__).resolve().parent)

import matplotlib.pyplot as plt

# %%
import matplotlib.pyplot as plt
plt.rcParams["axes.unicode_minus"] = False
plt.rc("font", family="Malgun Gothic")
if plt.get_fignums():
    plt.show()

# %%
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# %%
fig = px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")
# print(fig)
fig

# %%
# 🦁 plotly는 그래프를 그리기 위해 figure라는 객체를 사용
# - `data` : 그래프의 타입(산점도, 막대그래프 등)을 정의
# - `layout` : 축, 제목, 색상과 같은 그래프의 시각 요소를 설정

fig = dict({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By Python Dictionary"}}
})


# 딕셔너리로 정의된 그래프를 출력하려면, 저수준 plotly.io.show 함수 사용 필요
import plotly.io as pio

pio.show(fig)

# %%
# 이전 코드와 비교 🦁
fig = dict({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By Python Dictionary"}}
})
#################### ############################################################

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=go.Layout(
        title=go.layout.Title(text="A Figure Specified By A Graph Object")
    )
)

# plotly.io.show()를 사용하지 않고, fig.show()로 바로 호출함으로써,
# 보다 간편히 호출이 가능하다.
fig.show()

# %%

import plotly.graph_objects as go

# 이전 코드와 비교 🦁
fig = dict({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By Python Dictionary"}}
})

import plotly.io as pio

# pio.show(fig)
print(type(fig))
# <class 'dict'>
################################################################################

fig = dict({
    "data": [{"type": "bar",
    "x": [1, 2, 3],
    "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By A Graph Object With A Dictionary"}}
})

fig = go.Figure(fig)
fig.show()
print(type(fig))
# <class 'plotly.graph_objects.Figure'>
# Figure 객체는 plotly에서 그래프를 그리기 위해 사용하는 객체로, data와 layout 속성을 포함하고 있다.
# 해당 객체를 사용하면 그래프를 그리기 위한 다양한 설정을 할 수 있으며, plotly의 다양한 기능을 활용할 수 있다.⭐

# %%
fig = dict({
    "data": [{"type": "bar",
    "x": [1, 2, 3],
    "y": [1, 3, 2]}],
    "layout": {"titl": {"text": "A Figure Specified By A Graph Object With A Dictionary"}}
})

try:
    go.Figure(fig)
except ValueError:
    print("Plotly에서 titl은 유효한 속성이 아닙니다. title을 사용하세요.")

# %%
fig = dict({
    "data": [{"type": "bar",
    "x": [1, 2, 3],
    "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By A Graph Object With A Dictionary"}}
})
fig = go.Figure(fig)
#### 위의 코드는 오탈자가 없는 상태로, 정상적으로 그래프 객체로 변환이 가능하다.
#### 위 셀의 오류를 정정하기 위해 추가삽입된 코드 🦁🦁

fig.layout.template = None # 출력  결과 축소하기. 그냥 data외 내용을 지워서 콘솔출력을 줄이려고 적힌 코드

# Figure 객체를 딕셔너리로 변환하면, data와 layout 속성을 포함한 딕셔너리 형태로 변환된다.
print("Dictionary Representation of A Graph Object:\n\n" + str(fig.to_dict()))

# %%
import plotly.express as px

# 데이터 생성
data = {
    "x": [1, 2, 3],
    "y": [1, 3, 2]
}

# 그래프 생성
fig = px.bar(data, x="x", y="y", title="A Figure Specified By Plotly Express")

# 그래프 표시3
fig.show()

# %%
# 1) Plotly Express를 사용하여 기본 산포도 생성
df = px.data.gapminder().query("year == 2007")
fig = px.scatter(df, x="gdpPercap", y="lifeExp", color="continent", size="pop", hover_name="country", log_x=True)

# 2) plotly.graph_objects.Figure 객체를 사용하여 추가 설정 진행
# - 레이아웃 변경
fig.update_layout(
title="2007년 각 대륙의 GDP 대비 기대수명",
xaxis_title="1인당 GDP (log scale)",
yaxis_title="기대수명",
legend_title="대륙",
title_font_size=20
)

# - 각 데이터 포인트(마커)에 테두리 추가
fig.update_traces(marker=dict(line=dict(width=2, color='DarkSlateGrey')))

# - x, y축 눈금 및 레이아웃 배경색 설정
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
fig.update_layout(plot_bgcolor="LightBlue")

# 그래프 출력하기
fig.show()
