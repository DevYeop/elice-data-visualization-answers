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
import plotly.express as px
df = px.data.gapminder()
df_2007 = df.query("year==2007")
for template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
    fig = px.scatter(df_2007,
                     x="gdpPercap", y="lifeExp", size="pop", color="continent",
                     log_x=True, size_max=60,
                     template=template, title="Gapminder 2007: '%s' theme" % template)
    fig.show()

# %%
import plotly.io as pio
import plotly.express as px

pio.templates.default = "plotly_white"

df = px.data.gapminder()
df_2007 = df.query("year==2007")

fig = px.scatter(df_2007,
                 x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 log_x=True, size_max=60,
                 title="Gapminder 2007: current default theme")
fig.show()

# %%
import plotly.graph_objects as go

large_rockwell_template = dict(
    layout=go.Layout(title_font=dict(family="Rockwell", size=24))
)

fig = go.Figure()
fig.update_layout(title="Figure Title",
                  template=large_rockwell_template)
fig.show()

# %%
import plotly.graph_objects as go

draft_template = go.layout.Template()
draft_template.layout.annotations = [
    dict(
        name="draft watermark",
        text="Confidential",
        textangle=-30,
        opacity=0.1,
        font=dict(color="black", size=100),
        xref="paper",
        yref="paper",
        x=0.5,
        y=0.5,
        showarrow=False,
    )
]

fig=go.Figure()
fig.update_layout(template=draft_template)
fig.show()

# %%
df = px.data.gapminder()
df_2007 = df.query("year==2007")

fig = px.scatter(df_2007,
                 x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 log_x=True, size_max=60,
                 title="Gapminder 2007: current default theme")
fig.update_layout(template=draft_template)
fig.show()

# %%
# 그래프 한글 사용을 위한 전역 레이아웃 설정 (폰트를 'Malgun Gothic'으로 설정)

pio.templates["custom"] = pio.templates["plotly"] # 기본 템플릿 복사
pio.templates["custom"]["layout"]["font"] = dict(family="Malgun Gothic", size=16)

pio.templates.default = "custom"

# %%
import plotly.graph_objects as go
fig = go.Figure()
config = {'scrollZoom': True}

fig.add_trace(
go.Scatter(
x=[1, 2, 3],
y=[1, 3, 1]))

fig.show(config=config)

# %%
config = {'responsive': False}

fig.show(config=config)

# %%
config = {'staticPlot': False,
          'displayModeBar': True,
          'displaylogo': False,
          'toImageButtonOptions': {
              'format': 'svg', # one of png, svg, jpeg, webp
              'filename': 'custom_image',
              'height': 500, # None :
              'width': 700, # None :
              'scale': 1, # Multiply title/legend/axis/canvas sizes by this factor
          'modeBarButtonsToRemove': ['zoom', 'pan']}
         }
fig.show(config=config)

# %%
fig.show(config={'modeBarButtonsToAdd': ['drawline',
    'drawopenpath',
    'drawclosedpath',
    'drawcircle',
    'drawrect',
    'eraseshape'
]})

# %%
df = px.data.gapminder()
fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
hover_name="country", log_x=True, size_max=60)
fig.show()

# %%
df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
size="pop", color="continent", hover_name="country", facet_col="continent",
log_x=True, size_max=45, range_x=[100,100000], range_y=[25,90])
fig.show()
