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
# 데이터 리스트로 생성
year = [2018, 2019, 2020, 2021, 2022, 2023]
python = [5.8, 8.17, 9.31, 11.87, 15.63, 14.51]
C = [13.59, 14.08, 16.72, 14.32, 12.71, 14.73]
java = [15.78, 15.04, 16.73, 11.23, 10.82, 13.23]
JS = [3.49, 2.51, 2.38, 2.44, 2.12, 2.1]

# %%
plt.plot(year, python)  # x축은 년도, y축은 파이썬의 점유율
plt.show() # 만든 그래프를 화면에 보여주는 함수.(주피터 환경에서는 생략해도 그래프가 나타납니다.)

# %%
plt.title("파이썬의 언어 점유율")  # 그래프의 제목을 설정
plt.plot(year, python)  # x축은 년도, y은 파이썬의 점유율
if plt.get_fignums():
    plt.show()

# %%
plt.title("파이썬의 언어 점유율")
plt.xlabel("연도")  # x축의 레이블을 "연도"로 설정
plt.ylabel("점유율")  # y축의 레이블을 "점유율"로 설정
plt.plot(year, python)
if plt.get_fignums():
    plt.show()

# %%
plt.title("파이썬의 언어 점유율", fontsize=20)  # 제목의 크기를 20으로 설정
plt.xlabel("연도", fontsize=15)  # 레이블의 크기를 15로 설정
plt.ylabel("점유율", fontsize=15)  # 레이블의 크기를 15로 설정
plt.plot(year, python)
if plt.get_fignums():
    plt.show()

# %%
plt.title("프로그래밍 언어 점유율", fontsize=20)
plt.xlabel("연도", fontsize=15)
plt.ylabel("점유율", fontsize=15)
plt.plot(year, python)

# 다른 언어의 그래프를 추가
plt.plot(year, C)
plt.plot(year, java)
plt.plot(year, JS)
if plt.get_fignums():
    plt.show()

# %%
plt.title("프로그래밍 언어 점유율", fontsize=20)
plt.xlabel("연도", fontsize=15)
plt.ylabel("점유율", fontsize=15)

plt.plot(year, python)
plt.plot(year, C)
plt.plot(year, java)
plt.plot(year, JS)

plt.legend(['Python', 'C', 'JAVA', 'Java Script']) # 그래프를 그린 순서대로 이름을 전달
if plt.get_fignums():
    plt.show()

# %%
plt.title("프로그래밍 언어 점유율", fontsize=20)
plt.xlabel("연도", fontsize=15)
plt.ylabel("점유율", fontsize=15)

# 각 그래프의 label을 설정
plt.plot(year, python, label="Python")
plt.plot(year, C, label="C")
plt.plot(year, java, label="JAVA")
plt.plot(year, JS, label="Java Script")

plt.legend()  # 각 그래프의 label이 이미 전달되었으니 따로 전달하지 않고 호출합니다.
if plt.get_fignums():
    plt.show()

# %%
fig1 = plt.figure(1,figsize=(4,3))  # ID가 1인 새로운 figure 객체를 생성하고 선택합니다. 앞으로 호출하는 함수는 fig1에 적용됩니다.
plt.plot(year, python, label="Python")  # 현재 선택된 figure에 선 그래프를 그립니다.
plt.title("fig1")  # 현재 선택된 figure의 제목을 설정합니다.

fig2 = plt.figure(2,figsize=(4,3))  # ID가 2인 새로운 figure 객체를 생성하고 선택합니다. 앞으로 호출하는 함수는 fig2에 적용됩니다.
plt.plot(year, java, label="JAVA")  # 현재 선택된 figure에 선 그래프를 그립니다.
plt.title("fig2")  # 현재 선택된 figure의 제목을 설정합니다.

plt.show()  # 모든 figure를 화면에 그립니다.

# %%
fig2 # fig2의 그래프만 보기

# %%
fig1 = plt.figure(1, figsize=(4, 3))  # ID가 1인 새로운 figure 객체를 생성하고 선택합니다. 앞으로 호출하는 함수는 fig1에 적용됩니다.
plt.plot(year, python, label="Python")  # 현재 선택된 figure에 선 그래프를 그립니다.
plt.title("fig1")  # 현재 선택된 figure의 제목을 설정합니다.

fig2 = plt.figure( 2, figsize=(4, 3))  # ID가 2인 새로운 figure 객체를 생성하고 선택합니다. 앞으로 호출하는 함수는 fig2에 적용됩니다.
plt.title("fig2")  # 현재 선택된 figure의 제목을 설정합니다.

plt.figure(1)  # ID가 1인 figure를 선택합니다.(없으면 새로 만듭니다.)
plt.plot(year, java, label="JAVA")  # 현재 선택된 figure에 선 그래프를 그립니다.

plt.show()

# %%
fig, (ax1, ax2) = plt.subplots(1, 2) # 세로로 1칸, 가로로 2칸 총 2개의 subplot을 생성합니다.
# 생성된 subplot은 각각 ax1과 ax2에 저장됩니다.

ax1.plot(year, python)  # ax1에 파이썬 선 그래프를 그립니다.
ax2.plot(year, java)  # ax1에 자바 선 그래프를 그립니다.

plt.show() # 그래프를 표시합니다.

# %%
fig, (ax1, ax2) = plt.subplots(2, 1)  # 2행 1열로 총 2개의 그래프를 생성.
# 생성된 subplot은 각각 ax1과 ax2에 저장됩니다.

ax1.plot(year, python)  # 현재 선택된 figure에 선 그래프를 그립니다.
ax2.plot(year, java)  # 현재 선택된 figure에 선 그래프를 그립니다.

plt.show()  # 그래프를 표시합니다.

# %%
ax1.set_title("ax1의 제목") # ax1의 제목을 설정
ax2.set_title("ax2의 제목") # ax2의 제목을 설정
fig

# %%
fig, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True)  # constrained_layout=True를 전달
ax1.plot(year, python)  # ax1에 파이썬 선 그래프를 그립니다.
ax1.set_title("ax1의 제목") # ax1의 제목을 설정
ax1.set_xlabel("x라벨") # ax1의 xlabel을 설정

ax2.plot(year, java)  # ax2에 자바 선 그래프를 그립니다.
ax2.set_title("ax2의 제목") # ax2의 제목을 설정

plt.show()  # 그래프를 표시합니다.

# %%
todo_fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)

ax1.plot(year, python)
ax1.set(title="파이썬의 점유율", xlabel="연도", ylabel="점유율")

ax2.plot(year, java)
ax2.set(title="자바의 점유율", xlabel="연도")
plt.show()
