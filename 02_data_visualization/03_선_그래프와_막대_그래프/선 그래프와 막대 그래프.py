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
gb_mon = df.groupby("월")  # 그룹바이를 활용해서 월별로 묶기

# %%
df_mon = gb_mon.mean(numeric_only=True)  # 숫자형 열만 평균을 계산합니다.
df_mon

# %%
# 어른, 어린이, 청소년별 월별 입장객수 선그래프로 보기
plt.title("서울대공원 입장객 분석", fontsize=20)  # 그래프 제목
plt.plot(df_mon["어른"], label="어른")  # 월별 어른 이용객의 수
plt.plot(df_mon["어린이"], label="어린이")  # 월별 어린이 이용객의 수
plt.plot(df_mon["청소년"], label="청소년")  # 월별 청소년 이용객의 수
plt.xlabel("월", fontsize=15)
plt.ylabel("입장객수", fontsize=15)
plt.legend()
plt.show()

# %%
# 어른, 어린이, 청소년별 월별 입장객수 선그래프로 보기
plt.plot(df_mon["어른"], label="어른")
plt.plot(df_mon["어린이"], label="어린이")
plt.plot(df_mon["청소년"], label="청소년")
plt.xlabel("월", fontsize=15)
plt.ylabel("입장객수", fontsize=15)
plt.legend()
plt.xticks([mon for mon in range(1, 13)])  # 1부터 12가 들어있는 리스트를 xticks에 전달
plt.show()

# %%
# 어른, 어린이, 청소년별 월별 입장객수 선그래프로 보기
plt.plot(df_mon["어른"], marker=".", label="어른") # 작은 원 모양의 마커
plt.plot(df_mon["어린이"],marker="o", label="어린이") # 큰 원 모양의 마커
plt.plot(df_mon["청소년"],marker="^", label="청소년") # 삼각형 모양의 마커
plt.xticks([mon for mon in range(1, 13)])  # 1부터 12가 들어있는 리스트를 xticks에 전달
plt.legend()
plt.show()

# %%
# 어른, 어린이, 청소년별 월별 입장객수 선그래프로 보기
plt.plot(df_mon["어른"], marker=".", label="어른", linestyle="-")  # 실선으로 그리기 (기본값)
plt.plot(df_mon["어린이"], marker="o", label="어린이", linestyle="--")  # 대시로 그리기
plt.plot(df_mon["청소년"], marker="^", label="청소년", linestyle=":")  # 점선으로 그리기
plt.xticks([mon for mon in range(1, 13)])  # 1부터 12가 들어있는 리스트를 xticks에 전달
plt.legend()
plt.show()

# %%
# 어른, 어린이, 청소년별 월별 입장객수 선그래프로 보기
plt.plot(df_mon["어른"], marker=".", label="어른", linestyle="-", color= "b")  # 파란색으로 그리기
plt.plot(df_mon["어린이"], marker="o", label="어린이", linestyle="--", color= "k")  # 검은색으로 그리기
plt.plot(df_mon["청소년"], marker="^", label="청소년", linestyle=":", color = "r")  # 빨간색으로 그리기
plt.xticks([mon for mon in range(1, 13)])  # 1부터 12가 들어있는 리스트를 xticks에 전달
plt.legend()
plt.show()

# %%
# 예시 데이터
x = [1, 2, 3]
y = [6, 9, 4]

plt.plot(x, y)  # 꺽은선 그래프
plt.xticks(x)  # 1, 2, 3에 눈금 표시

plt.grid(True)  # x축, y축 각각 격자가 생성됨
if plt.get_fignums():
    plt.show()

# %%
# 어른, 어린이, 청소년별 월별 입장객수 선그래프로 보기
plt.title("서울대공원 입장객 분석", fontsize=20)  # 그래프 제목
plt.plot(df_mon["어른"], marker=".", label="어른", linestyle="-", color= "b")  # 파란색으로 그리기
plt.plot(df_mon["어린이"], marker="o", label="어린이", linestyle="--", color= "k")  # 검은색으로 그리기
plt.plot(df_mon["청소년"], marker="^", label="청소년", linestyle=":", color = "r")  # 빨간색으로 그리기
plt.xlabel("월", fontsize=15)
plt.ylabel("입장객수", fontsize=15)
plt.legend()
plt.xticks([mon for mon in range(1, 13)])  # 1부터 12가 들어있는 리스트를 xticks에 전달

plt.grid(True, axis="x")  # x축 격자가 생성됨
plt.show()

# %%
sns.lineplot(data=df, x="월", y="어른", errorbar=None)
sns.lineplot(data=df, x="월", y="어린이", errorbar=None)
sns.lineplot(data=df, x="월", y="청소년", errorbar=None)
if plt.get_fignums():
    plt.show()

# %%
sns.lineplot(data=df, x="월", y="어른", label="어른", marker="o", errorbar=None)
sns.lineplot(data=df, x="월", y="어린이", label="어린이", marker="^", errorbar=None)
sns.lineplot(data=df, x="월", y="청소년", label="청소년", marker=".", errorbar=None)
plt.ylabel("입장객수")
plt.xticks([mon for mon in range(1, 13)])  # 1부터 12가 들어있는 리스트를 xticks에 전달
plt.show()

# %%
df_week = df.groupby("요일").mean(numeric_only=True)
df_week = df_week.reset_index()  # "요일" 열을 다시 데이터프레임의 열로 가져옴
df_week

# %%
plt.title("서울대공원 청소년 입장객 분석", fontsize=20)  # 그래프의 제목
plt.bar(df_week["요일"], df_week["청소년"])  # 가로에는 요일을, 세로에는 청소년 입장객의 수를 표시합니다.
plt.xlabel("요일", fontsize=15)
plt.ylabel("청소년 입장객수", fontsize=15)
if plt.get_fignums():
    plt.show()

# %%
plt.title("서울대공원 청소년 입장객 분석", fontsize=20)
plt.barh(df_week["요일"], df_week["청소년"])  # 가로 막대그래프.
plt.xlabel("청소년 입장객수", fontsize=15) # 가로가 입장객의 수가 되었으니 가로축의 레이블을 바꿔줍니다.
plt.ylabel("요일", fontsize=15) # 이제 세로축은 요일이 되었습니다.
if plt.get_fignums():
    plt.show()

# %%
# 데이터프레임을 입장객 수로 내림차순 정렬합니다.
df_sorted = df_week.sort_values(by="청소년", ascending=False)
# by: 어떤 칼럼으로 정렬할지 선택합니다. ascending: True라면 오름차순, False라면 내림차순입니다.

plt.title("서울대공원 청소년 입장객 분석", fontsize=20)
plt.bar(df_sorted["요일"], df_sorted["청소년"])  # 세로 막대그래프
plt.xlabel("요일", fontsize=15)
plt.ylabel("청소년 입장객수", fontsize=15)
if plt.get_fignums():
    plt.show()

# %%
sns.barplot(data=df, x="요일", y="청소년")  # data에 df를 전달하고 x, y축에 해당하는 칼럼의 이름을 전달
if plt.get_fignums():
    plt.show()

# %%
sns.barplot(data=df, x="요일", y="청소년", errorbar=None) # errorbar=None을 전달하여 오차 막대를 제거함
plt.show()

# %%
sns.barplot(data=df, x="날씨", y="어린이", errorbar=None) # 날씨별로 어린이 입장객의 수를 표현
plt.show()

# %%
sns.barplot(data=df, x="날씨", y="어린이", errorbar=None, hue="공휴일") # "공휴일" 값을 기준으로 그룹을 나눔
plt.show()

# %%
fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)

sns.lineplot(data=df, x="연", y="매출액", errorbar=None, marker="o", color="r", ax=ax1)
ax1.set_title("연도별 매출액")

sns.barplot(data=df, x="연", y="매출액", hue="공휴일", errorbar=None, ax=ax2)
ax2.set_title("공휴일 여부에 따른 매출액")
plt.show()
