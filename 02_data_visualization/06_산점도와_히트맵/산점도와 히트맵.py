# %%
from pathlib import Path
import os

os.chdir(Path(__file__).resolve().parent)

import matplotlib.pyplot as plt

# %%
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False
plt.rc("font", family="NanumBarunGothic")
if plt.get_fignums():
    plt.show()

# %%
import pandas as pd

# %%
df = pd.read_csv("seoul_park.csv")

# %%
df.head()

# %%
df.tail()

# %%
df.info()

# %%
# 산점도 그래프
plt.scatter(df['어른'], df['청소년'])
plt.show()

# %%
# 어른과 어린이 입장객수의 상관관계 산점도
sns.scatterplot(data=df, x='어른', y='어린이')
if plt.get_fignums():
    plt.show()

# %%
# 어른과 어린이 입장객수의 상관관계 산점도
sns.scatterplot(data=df, x='어른', y='어린이')
if plt.get_fignums():
    plt.show()

# %%
sns.scatterplot(data=df, x="어른", y="어린이")

plt.ylim(0, 6000)  # y축 범위를 0에서 6000으로 제한
plt.xlim(0, 35000)  # x축 범위를 0에서 35000으로 제한
if plt.get_fignums():
    plt.show()

# %%
# 피어슨 상관계수
# 🦁데이터프레임에 있는 숫자형 컬럼들끼리 얼마나 관련이 있는지 계산하기 위해 수행.
# 🦁같은 컬럼끼리 교차하는 걸 보면 정확히 1인걸 볼 수 있다. (자기 자신과의 상관계수는 1)
df_corr = df.corr(numeric_only=True) # corr == Correlation(상관관계) 의 약자
df_corr

# %%
# 히트맵
sns.heatmap(df_corr)
if plt.get_fignums():
    plt.show()

# %%
sales_corr = df_corr.loc[["어른", "청소년", "어린이"], "매출액"]
todo = sales_corr.abs().sort_values(ascending=False).index.tolist()
print(todo)
