from pathlib import Path
import os

os.chdir(Path(__file__).resolve().parent)

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
plt.rcParams["axes.unicode_minus"] = False
plt.rc("font", family="Malgun Gothic")
if plt.get_fignums():
    plt.show()

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

fig = px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")

fig

fig = dict({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By Python Dictionary"}}
})

import plotly.io as pio

pio.show(fig)

fig = dict({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By Python Dictionary"}}
})

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=go.Layout(
        title=go.layout.Title(text="A Figure Specified By A Graph Object")
    )
)

fig.show()

import plotly.graph_objects as go

fig = dict({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By Python Dictionary"}}
})

import plotly.io as pio

print(type(fig))

fig = dict({
    "data": [{"type": "bar",
    "x": [1, 2, 3],
    "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By A Graph Object With A Dictionary"}}
})

fig = go.Figure(fig)
fig.show()
print(type(fig))

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

fig = dict({
    "data": [{"type": "bar",
    "x": [1, 2, 3],
    "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By A Graph Object With A Dictionary"}}
})
fig = go.Figure(fig)

fig.layout.template = None

print("Dictionary Representation of A Graph Object:\n\n" + str(fig.to_dict()))

import plotly.express as px

data = {
    "x": [1, 2, 3],
    "y": [1, 3, 2]
}

fig = px.bar(data, x="x", y="y", title="A Figure Specified By Plotly Express")

fig.show()

df = px.data.gapminder().query("year == 2007")
fig = px.scatter(df, x="gdpPercap", y="lifeExp", color="continent", size="pop", hover_name="country", log_x=True)

fig.update_layout(
title="2007년 각 대륙의 GDP 대비 기대수명",
xaxis_title="1인당 GDP (log scale)",
yaxis_title="기대수명",
legend_title="대륙",
title_font_size=20
)

fig.update_traces(marker=dict(line=dict(width=2, color='DarkSlateGrey')))

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
fig.update_layout(plot_bgcolor="LightBlue")

fig.show()
