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
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])

fig.show()

# %%
fig = go.Figure()
fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16], mode="markers"))

fig.show()

# %%
df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(df, x='year', y='lifeExp', color='country')

fig.show()

# %%
df = px.data.gapminder().query("continent == 'Oceania'")
fig = go.Figure()

# 각 나라별로 데이터를 그룹화하여 라인 추가
for country in df['country'].unique():
    country_data = df[df['country'] == country]
    fig.add_trace(go.Scatter(x=country_data['year'], y=country_data['lifeExp'], mode='lines', name=country))
fig.show()

# %%
animals = ['giraffes', 'orangutans', 'monkeys']
counts = [20, 14, 23]
fig = px.bar(x=animals, y=counts)
fig.show()

# %%
animals=['giraffes', 'orangutans', 'monkeys']
fig = go.Figure([go.Bar(x=animals, y=[20, 14, 23])])
fig.show()

# %%
labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
values = [4500, 2500, 1053, 500]
fig = px.pie(names=labels, values=values)
fig.show()

# %%
labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()

# %%
df = px.data.tips()
fig = px.box(df, y="total_bill")
fig.show()

# %%
df = px.data.tips()
fig = go.Figure(data=[go.Box(y=df['total_bill'])])
fig.show()

# %%
df = px.data.tips()
fig = px.histogram(df, x="total_bill")
fig.show()

# %%
df = px.data.tips()
fig = go.Figure(data=[go.Histogram(x=df['total_bill'])])
fig.show()

# %%
z = [[1, 20, 30],
    [20, 1, 60],
    [30, 60, 1]]
fig = px.imshow(z, color_continuous_scale='Viridis')
fig.show()

# %%
fig = go.Figure(data=go.Heatmap(
                z=[[1, 20, 30],
                [20, 1, 60],
                [30, 60, 1]]))
fig.show()

# %%
df = pd.DataFrame([
dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Resource")
fig.show()

# %%
data = dict(
number=[39, 27.4, 20.6, 11, 2],
stage=["Website visit", "Downloads", "Potential customers", "Requested price", "Invoice sent"])
fig = px.funnel(data, x='number', y='stage')
fig.show()

# %%
fig = go.Figure(go.Funnel(
y = ["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"],
x = [39, 27.4, 20.6, 11, 2]))
fig.show()

# %%
df = px.data.carshare()
fig = px.scatter_map(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
map_style="carto-positron")
fig.show()
