# %%
from pathlib import Path
import os

os.chdir(Path(__file__).resolve().parent)

import matplotlib.pyplot as plt

# %%
import seaborn as sns

# %%
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False
plt.rc("font", family="Malgun Gothic")
if plt.get_fignums():
    plt.show()

# %%
# 데이터 리스트로 생성
year = [2018, 2019, 2020, 2021, 2022, 2023]
python = [5.8, 8.17, 9.31, 11.87, 15.63, 14.51]
C = [13.59, 14.08, 16.72, 14.32, 12.71, 14.73]
java = [15.78, 15.04, 16.73, 11.23, 10.82, 13.23]
JS = [3.49, 2.51, 2.38, 2.44, 2.12, 2.1]

# %%
sns.lineplot(x=year, y=python)  # 파이썬 그래프를 그리기
if plt.get_fignums():
    plt.show()

# %%
sns.lineplot(x=year, y=python, label="python")  # "python"이라는 레이블 추가
sns.lineplot(x=year, y=java, label="java")  # "java"라는 레이블 추가
if plt.get_fignums():
    plt.show()

# %%
lp= sns.lineplot(x=year, y=python, label="python")

lp.set_xlabel("연도") # x축의 레이블을 설정 (matplotlib의 ax와 같은 방식)
lp.set_ylabel("점유율") # y축의 레이블을 설정
if plt.get_fignums():
    plt.show()

# %%
sns.set_style("darkgrid", rc={"font.family": "Malgun Gothic"})  # 스타일을 darkgrid로 변경
lp = sns.lineplot(x=year, y=python, label="python")  # 그래프 그리기
if plt.get_fignums():
    plt.show()

# %%
fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)  # 1행 2열의 서브플롯을 생성합니다.

fig = sns.lineplot(x=year, y=python, label="python", ax=ax1)  # seaborn을 이용해 그래프 그리기
sns.lineplot(x=year, y=java, label="java", ax=ax2)  # seaborn을 이용해 그래프 그리기
if plt.get_fignums():
    plt.show()

# %%
fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)
sns.lineplot(x=year, y=C, label="C", ax=ax1)
sns.lineplot(x=year, y=JS, label="JS", ax=ax2)
plt.show()
