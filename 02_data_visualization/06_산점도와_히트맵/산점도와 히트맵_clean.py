from pathlib import Path
import os

os.chdir(Path(__file__).resolve().parent)

import matplotlib.pyplot as plt

import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False
plt.rc("font", family="NanumBarunGothic")
if plt.get_fignums():
    plt.show()

import pandas as pd

df = pd.read_csv("seoul_park.csv")

df.head()

df.tail()

df.info()

plt.scatter(df['어른'], df['청소년'])
plt.show()

sns.scatterplot(data=df, x='어른', y='어린이')
if plt.get_fignums():
    plt.show()

sns.scatterplot(data=df, x='어른', y='어린이')
if plt.get_fignums():
    plt.show()

sns.scatterplot(data=df, x="어른", y="어린이")

plt.ylim(0, 6000)
plt.xlim(0, 35000)
if plt.get_fignums():
    plt.show()

df_corr = df.corr(numeric_only=True)
df_corr

sns.heatmap(df_corr)
if plt.get_fignums():
    plt.show()

sales_corr = df_corr.loc[["어른", "청소년", "어린이"], "매출액"]
todo = sales_corr.abs().sort_values(ascending=False).index.tolist()
print(todo)
