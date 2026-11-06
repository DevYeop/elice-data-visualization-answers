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

# %%
fig = go.Figure()
fig.add_trace(go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.show()

# %%
df = px.data.iris()
# 🦁 print(df)

# 🦁 color="species"는 색상 자체를 지정하는 것이 아니라,
# 🦁 species 컬럼의 값(setosa, versicolor, virginica)에 따라
# 🦁 데이터 포인트의 색상을 자동으로 구분하는 역할을 한다.
# 🦁 즉, color="red"처럼 특정 색상을 지정하는 것과는 다르다.
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Using The add_trace() method With A Plotly Express Figure")

fig.add_trace(
    go.Scatter(
        x=[2, 4],
        y=[4, 8],
        mode="lines",
        line=go.scatter.Line(color="red"),
        showlegend=False)
)
fig.show()

# %%
# 데이터 생성
data = {
    "x": [1, 2, 3],
    "y": [1, 3, 2]
}

# 그래프 생성
fig = px.bar(data, x="x", y="y", title="A Figure Specified By Plotly Express")

# 각 막대 위를 점으로 이어주는 선 추가
fig.add_scatter(x=data["x"], y=data["y"], mode="lines+markers", name="Line Over Bars")
# 라인을 빼면 실제로 산점도가 추가된 것처럼 보인다. 메서드명이 이상한게 아니다 🦁
# fig.add_scatter(x=data["x"], y=data["y"], mode="markers", name="Line Over Bars")

# 그래프 표시
fig.show()

# %%
fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.update_layout(title_text="Using update_layout() With Graph Object Figures", title_font_size=30)
# _를 활용하여 속성을 보다 짧게 표현함
# 원래는 아래와 같이 써야한다 💀
# fig.update_layout(
#     title=dict(
#         text="그래프 제목",
#         font=dict(size=30)
#     )
# )
##############

"""
fig.update_layout(
    title=dict(
        text="Using update_layout() With Graph Object Figures",
        font=dict(size=30)
 )
)
"""

fig.show()

# %%
# _ 가 .대신에 붙었다고 생각하면 된다. 즉, title_text는 title.text를 의미하고, title_font_size는 title.font.size를 의미한다.

fig.update_layout(title_text="update_layout() Syntax Example",
                  title_font_size=30)

fig.update_layout(title_text="update_layout() Syntax Example",
                  title_font=dict(size=30))


fig.update_layout(title=dict(text="update_layout() Syntax Example"),
                             font=dict(size=30))

fig.update_layout({"title": {"text": "update_layout() Syntax Example",
                             "font": {"size": 30}}})

fig.update_layout(title=go.layout.Title(text="update_layout() Syntax Example",
                                        font=go.layout.title.Font(size=30)))

# %%
from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Scatter(y=[4, 2, 1], mode="lines"), row=1, col=2) # 🦁뒤에는 포지션, 바꿔주면 표시위치가 바뀐다
fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=1)
fig.show()

# %%
df = px.data.iris()

# 🦁 facet_col을 사용하여 species별로 서브플롯을 생성하고, 각 서브플롯에 산점도를 그린다.
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", facet_col="species",
                 title="Adding Traces To Subplots Witin A Plotly Express Figure")

# 🦁 각 서브플롯에 동일한 참조선을 추가하기 위해 go.Scatter 객체를 생성한다.
reference_line = go.Scatter(x=[2, 4],
                            y=[4, 8],
                            mode="lines",
                            line=go.scatter.Line(color="gray"),
                            showlegend=False)

# 🦁 그리고 포지션을 지정하여 각 서브플롯에 참조선을 추가한다.
fig.add_trace(reference_line, row=1, col=1)
fig.add_trace(reference_line, row=1, col=2)
fig.add_trace(reference_line, row=1, col=3)

fig.show()

# %%
fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

fig.show()

# %%
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

# 🦁 이 업데이트를 통해 전부 RoyalBlue로 바뀌게 된다.
fig.update_traces(marker=dict(color="RoyalBlue"))

"""
fig.update_traces(marker_color="RoyalBlue",
                  selector=dict(marker_color="MediumPurple"))
"""

"""
fig.update_traces(marker=dict(color="RoyalBlue"),
                  col=2)
"""


fig.show()

# %%
fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

fig.update_traces(marker=dict(color="RoyalBlue"),
                  col=2)

fig.show()

# %%
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Conditionally Updating Traces In A Plotly Express Figure With for_each_trace()")

fig.for_each_trace(
    lambda trace: trace.update(marker_symbol="square") if trace.name == "setosa" else (),
)

fig.show()

# %%
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 facet_col="species", title="Using update_xaxes() With A Plotly Express Figure")

fig.update_xaxes(showgrid=False)

fig.show()
