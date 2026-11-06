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

gb_mon = df.groupby("월")

df_mon = gb_mon.mean(numeric_only=True)
df_mon

plt.title("서울대공원 입장객 분석", fontsize=20)
plt.plot(df_mon["어른"], label="어른")
plt.plot(df_mon["어린이"], label="어린이")
plt.plot(df_mon["청소년"], label="청소년")
plt.xlabel("월", fontsize=15)
plt.ylabel("입장객수", fontsize=15)
plt.legend()
plt.show()

plt.plot(df_mon["어른"], label="어른")
plt.plot(df_mon["어린이"], label="어린이")
plt.plot(df_mon["청소년"], label="청소년")
plt.xlabel("월", fontsize=15)
plt.ylabel("입장객수", fontsize=15)
plt.legend()
plt.xticks([mon for mon in range(1, 13)])
plt.show()

plt.plot(df_mon["어른"], marker=".", label="어른")
plt.plot(df_mon["어린이"],marker="o", label="어린이")
plt.plot(df_mon["청소년"],marker="^", label="청소년")
plt.xticks([mon for mon in range(1, 13)])
plt.legend()
plt.show()

plt.plot(df_mon["어른"], marker=".", label="어른", linestyle="-")
plt.plot(df_mon["어린이"], marker="o", label="어린이", linestyle="--")
plt.plot(df_mon["청소년"], marker="^", label="청소년", linestyle=":")
plt.xticks([mon for mon in range(1, 13)])
plt.legend()
plt.show()

plt.plot(df_mon["어른"], marker=".", label="어른", linestyle="-", color= "b")
plt.plot(df_mon["어린이"], marker="o", label="어린이", linestyle="--", color= "k")
plt.plot(df_mon["청소년"], marker="^", label="청소년", linestyle=":", color = "r")
plt.xticks([mon for mon in range(1, 13)])
plt.legend()
plt.show()

x = [1, 2, 3]
y = [6, 9, 4]

plt.plot(x, y)
plt.xticks(x)

plt.grid(True)
if plt.get_fignums():
    plt.show()

plt.title("서울대공원 입장객 분석", fontsize=20)
plt.plot(df_mon["어른"], marker=".", label="어른", linestyle="-", color= "b")
plt.plot(df_mon["어린이"], marker="o", label="어린이", linestyle="--", color= "k")
plt.plot(df_mon["청소년"], marker="^", label="청소년", linestyle=":", color = "r")
plt.xlabel("월", fontsize=15)
plt.ylabel("입장객수", fontsize=15)
plt.legend()
plt.xticks([mon for mon in range(1, 13)])

plt.grid(True, axis="x")
plt.show()

sns.lineplot(data=df, x="월", y="어른", errorbar=None)
sns.lineplot(data=df, x="월", y="어린이", errorbar=None)
sns.lineplot(data=df, x="월", y="청소년", errorbar=None)
if plt.get_fignums():
    plt.show()

sns.lineplot(data=df, x="월", y="어른", label="어른", marker="o", errorbar=None)
sns.lineplot(data=df, x="월", y="어린이", label="어린이", marker="^", errorbar=None)
sns.lineplot(data=df, x="월", y="청소년", label="청소년", marker=".", errorbar=None)
plt.ylabel("입장객수")
plt.xticks([mon for mon in range(1, 13)])
plt.show()

df_week = df.groupby("요일").mean(numeric_only=True)
df_week = df_week.reset_index()
df_week

plt.title("서울대공원 청소년 입장객 분석", fontsize=20)
plt.bar(df_week["요일"], df_week["청소년"])
plt.xlabel("요일", fontsize=15)
plt.ylabel("청소년 입장객수", fontsize=15)
if plt.get_fignums():
    plt.show()

plt.title("서울대공원 청소년 입장객 분석", fontsize=20)
plt.barh(df_week["요일"], df_week["청소년"])
plt.xlabel("청소년 입장객수", fontsize=15)
plt.ylabel("요일", fontsize=15)
if plt.get_fignums():
    plt.show()

df_sorted = df_week.sort_values(by="청소년", ascending=False)

plt.title("서울대공원 청소년 입장객 분석", fontsize=20)
plt.bar(df_sorted["요일"], df_sorted["청소년"])
plt.xlabel("요일", fontsize=15)
plt.ylabel("청소년 입장객수", fontsize=15)
if plt.get_fignums():
    plt.show()

sns.barplot(data=df, x="요일", y="청소년")
if plt.get_fignums():
    plt.show()

sns.barplot(data=df, x="요일", y="청소년", errorbar=None)
plt.show()

sns.barplot(data=df, x="날씨", y="어린이", errorbar=None)
plt.show()

sns.barplot(data=df, x="날씨", y="어린이", errorbar=None, hue="공휴일")
plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)

sns.lineplot(data=df, x="연", y="매출액", errorbar=None, marker="o", color="r", ax=ax1)
ax1.set_title("연도별 매출액")

sns.barplot(data=df, x="연", y="매출액", hue="공휴일", errorbar=None, ax=ax2)
ax2.set_title("공휴일 여부에 따른 매출액")
plt.show()
