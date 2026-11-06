# %%
from pathlib import Path
import os

os.chdir(Path(__file__).resolve().parent)

import matplotlib.pyplot as plt

# %%
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False
plt.rc("font", family="Malgun Gothic")
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
df_2018_apr = df[(df["연"] == 2018) & (df["월"] == 4)]
# 2018년 4월의 데이터
df_2018_apr.head()

# %%
plt.boxplot(df_2018_apr["어린이"])
plt.show()

# 🦁순서대로
# 이상치 최대값 75% 50% 25% 최소값

# %%
# plt.boxplot(df_2018_apr["어린이"])

# 🦁 plt 에 여러 인자를 전하면서 한 도화지에 여서 박스 플롯을 그릴 수 있다
plt.boxplot([df_2018_apr["어린이"], df_2018_apr["어른"], df_2018_apr["청소년"]])
plt.xticks([1, 2, 3], labels=["어린이", "어른", "청소년"])
plt.title("2018년 4월의 입장객 수")
plt.show()

# %%
sns.boxplot(data=df_2018_apr, y="어린이")
if plt.get_fignums():
    plt.show()

# %%
df_2018 = df[df["연"] == 2018]
df_2018.head()

# %%
sns.boxplot(data=df_2018, x="월", y="어린이")
if plt.get_fignums():
    plt.show()

# %%
df_2016 = df[df["연"] == 2016]
ax = sns.boxplot(data=df_2016, x="월", y="어른")
ax.set_title("2016년 성인 입장객 수")
plt.show()
