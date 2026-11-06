from pathlib import Path
import os

os.chdir(Path(__file__).resolve().parent)

import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False
plt.rc("font", family="Malgun Gothic")
if plt.get_fignums():
    plt.show()

df=pd.read_csv("./data/seoul_apart_02.csv")
df.head()

plt.figure()
sns.histplot(data=df["거래금액(만원)"], bins=30)
plt.show()

df.groupby("계약월")["평당금액"].mean()

mon_price=df.groupby("계약월")[["평당금액"]].mean()

plt.title("월별 평당 거래금액(만원)")
plt.plot(mon_price["평당금액"])
plt.show()

plt.figure()
sns.countplot(data=df, x="계약월")
plt.show()

sns.histplot(data=df[df["계약월"]==4]["평당금액"])
if plt.get_fignums():
    plt.show()

plt.figure(figsize=(15,8))
plt.title("지역(구)별 평균 평당금액")
sns.barplot(data=df, x="구", y="평당금액")
plt.ylabel("평당금액(단위: 만원)")
if plt.get_fignums():
    plt.show()

type_ratio=df["유형"].value_counts()
plt.pie(x=type_ratio, labels=type_ratio.index, autopct="%1.1f%%")
if plt.get_fignums():
    plt.show()

plt.figure(figsize=(12, 5))
sns.boxplot(data=df, x="구", y="평당금액")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

q1=df[df["구"]=="성동구"]["평당금액"].quantile(0.25)
q3=df[df["구"]=="성동구"]["평당금액"].quantile(0.75)
boundary=(q3-q1)*1.5

df[(df["구"]=="성동구") & (df["평당금액"]>q3+boundary)]

plt.figure()
sns.scatterplot(data=df, x="전용면적(평)", y="거래금액(만원)")
plt.show()

df_corr=df.corr(numeric_only=True)
sns.heatmap(df_corr, annot=True)
if plt.get_fignums():
    plt.show()
