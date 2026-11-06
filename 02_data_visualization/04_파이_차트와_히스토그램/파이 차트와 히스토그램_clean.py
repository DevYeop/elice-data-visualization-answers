from pathlib import Path
import os

os.chdir(Path(__file__).resolve().parent)

import matplotlib.pyplot as plt

import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False
plt.rc("font", family="Malgun Gothic")
if plt.get_fignums():
    plt.show()

import pandas as pd

df = pd.read_csv("seoul_park.csv")

df.head()

df.tail()

df.info()

df["연"] == 2019

df[df["연"] == 2019]

df[df["연"] == 2019][["어른", "청소년", "어린이"]]

df[df["연"] == 2019][["어른", "청소년", "어린이"]].sum()

data_2019 = df[df["연"] == 2019][["어른", "청소년", "어린이"]].sum()

data_2019

df_tmp = pd.DataFrame({
    "이름": ["철수", "민수", "철수"],
    "나이": [25, 28, 30]
})
print(df_tmp)

df_tmp2 = pd.DataFrame({
    "이름": ["철수", "민수", "철수"],
    "나이": [25, 28, 30]
}, index=["A", "B", "C"])
print(df_tmp2)

df_tmp3 = pd.DataFrame({
    "이름": ["김씨", "이씨", "박씨"],
    "나이": [25, 28, 30]
}, index=[1, 3, 2])
print(df_tmp3.sort_index())

labels = data_2019.index
data = data_2019
data
print(data)
print(labels)

plt.pie(x=data, labels=labels)
plt.legend(title="2019년 입장객 분포", loc="best")
plt.show()

plt.pie(x=data, labels=labels, autopct="%1.1f%%")

plt.show()

df_sat = df[df["요일"] == "토"]
df_sat

plt.hist(df_sat["어린이"], bins=10, edgecolor="black")
plt.show()

plt.hist(df_sat["어린이"], histtype="bar")
plt.title("bar")
plt.figure()

plt.hist(df_sat["어린이"], histtype="barstacked")
plt.title("barstacked")
plt.figure()

plt.hist(df_sat["어린이"], histtype="step")
plt.title("step")
plt.figure()

plt.hist(df_sat["어린이"], histtype="stepfilled")
plt.title("stepfilled")
plt.show()

sns.histplot(data=df_sat, x="어린이")
plt.show()

df_feb = df[df["월"] == 2]

sns.histplot(data=df_feb, x="어린이", hue="연")
if plt.get_fignums():
    plt.show()

sns.histplot(data=df_feb, x="어린이", hue="연",binrange=(0,1000), bins = 20)
if plt.get_fignums():
    plt.show()

sns.histplot(
    data=df_feb,
    x="어린이",
    hue="연",
    binrange=(0, 800),
    bins=10,

    multiple="dodge",
    shrink=0.9,
)
if plt.get_fignums():
    plt.show()

df_april2017 = df[(df["연"] == 2017) & (df["월"] == 4)]
todo1 = sns.histplot(data=df_april2017, x="어른", bins=20)
if plt.get_fignums():
    plt.show()
