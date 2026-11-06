from pathlib import Path
import os

os.chdir(Path(__file__).resolve().parent)

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
plt.rcParams["axes.unicode_minus"] = False
plt.rc("font", family="Malgun Gothic")
if plt.get_fignums():
    plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print(sns.__version__)

try:
    import missingno as msno

except:
    import missingno as msno
if plt.get_fignums():
    plt.show()

df = pd.read_csv("./data/한국교통안전공단_자동차결함 리콜현황_20201231.csv", encoding="euc-kr")

df.head()

df.head(10)

df.tail()

df.info()

import matplotlib.font_manager as fm

sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False})
msno.matrix(df)
plt.show()

df.isna().sum()

df[df.duplicated(keep=False)]

print("Before:", len(df))
df = df.drop_duplicates()
print("After:", len(df))

def parse_year(s):
    return int(s[:4])
def parse_month(s):
    return int(s[5:7])
def parse_day(s):
    return int(s[8:])

df['start_year'] = df['생산기간'].apply(parse_year)
df['start_month'] = df['생산기간'].apply(parse_month)
df['start_day'] = df['생산기간'].apply(parse_day)

df['end_year'] = df['생산기간.1'].apply(parse_year)
df['end_month'] = df['생산기간.1'].apply(parse_month)
df['end_day'] = df['생산기간.1'].apply(parse_day)

df['recall_year'] = df['리콜개시일'].apply(parse_year)
df['recall_month'] = df['리콜개시일'].apply(parse_month)
df['recall_day'] = df['리콜개시일'].apply(parse_day)

df.head(3)

df = df.drop(columns=['생산기간', '생산기간.1', '리콜개시일']).rename(columns={'제작자': "manufacturer", "차명": "model", "리콜사유": "cause"})
df.head(3)

df.recall_year.min(), df.recall_year.max()

df = df[df['recall_year']==2020]
len(df)

df.groupby("manufacturer").count()["model"].sort_values(ascending=False)

pd.DataFrame(df.groupby("manufacturer").count()["model"].sort_values(ascending=False)).rename(columns={"model": "count"})

tmp = pd.DataFrame(df.groupby("manufacturer").count()["model"].sort_values(ascending=False)).rename(columns={"model": "count"})

plt.figure(figsize=(20,10))

sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style='darkgrid')
ax = sns.countplot(x="manufacturer", data=df, palette="Set2", order=tmp.index)
plt.xticks(rotation=270)
plt.show()

tmp.index

pd.DataFrame(df.groupby("model").count()["start_year"].sort_values(ascending=False)).rename(columns={"start_year": "count"}).head(10)

tmp = pd.DataFrame(df.groupby("model").count()["manufacturer"].sort_values(ascending=False))
tmp = tmp.rename(columns={"manufacturer": "count"}).iloc[:50]

plt.figure(figsize=(10,5))

sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style='darkgrid')
ax = sns.countplot(x="model", data=df[df.model.isin(tmp.index)], palette="Set2", order=tmp.index)
plt.xticks(rotation=270)
plt.show()

pd.DataFrame(df.groupby("recall_month").count()["start_year"].sort_values(ascending=False)).rename(columns={"start_year": "count"})

plt.figure(figsize=(10,5))

sns.set(style="darkgrid", font="Malgun Gothic")
df['recall_month'] = df['recall_month'].astype('category')
ax = sns.countplot(x="recall_month", data=df)
plt.show()

df.info()

tmp = pd.DataFrame(df.groupby("start_year").count()["model"]).rename(columns={"model": "count"}).reset_index()

plt.figure(figsize=(10,5))

np.float = float
sns.set(style="darkgrid", font="Malgun Gothic")
df['start_year'] = df['start_year'].astype('category')
sns.lineplot(data=tmp, x="start_year", y="count")
plt.show()

tmp

monthly_recalls = df["recall_month"].value_counts().reindex(range(1, 13), fill_value=0)
quiz_1 = int(monthly_recalls.max() - monthly_recalls.min())

df[df.recall_month.isin([10,11,12])].head()

plt.figure(figsize=(20,10))
sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style='darkgrid')
ax = sns.countplot(x="manufacturer", data=df[df.recall_month.isin([10,11,12])], palette="Set2")
plt.xticks(rotation=270)
plt.show()

df['recall_month'] = df['recall_month'].astype('int')

df[df["recall_month"]>=7].head()

plt.figure(figsize=(10,5))
sns.set(style="darkgrid", font="Malgun Gothic")
ax = sns.countplot(x="start_year", data=df[df.recall_month>=7], palette="Set2")
plt.show()

from wordcloud import WordCloud, STOPWORDS

set(STOPWORDS)

spwords = set(["동안", "인하여", "있는", "경우", "있습니다", "가능성이", "않을", "차량의", "가", "에", "될", "이",
               "인해", "수", "중", "시", "또는", "있음", "의", "및", "있으며", "발생할", "이로", "오류로", "해당"])

text = ""

for c in df.cause.drop_duplicates():
    text += c

text[:100]

wc1 = WordCloud(max_font_size=200, stopwords=spwords, font_path='C:/Windows/Fonts/malgun.ttf',
                background_color='white', width=800, height=800)
wc1.generate(text)

plt.figure(figsize=(10, 8))
plt.imshow(wc1)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()

kia_recalls = df.loc[df["manufacturer"].eq("기아자동차(주)")]
latest_kia = kia_recalls.sort_values(["recall_year", "recall_month", "recall_day"], ascending=False)
quiz_2 = latest_kia["model"].iloc[0]

student_answers = {}
student_answers["problem_1"] = int(quiz_1)
student_answers["problem_2"] = str(quiz_2)

print(student_answers)
