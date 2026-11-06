from pathlib import Path
import os

os.chdir(Path(__file__).resolve().parent)

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False
plt.rc("font", family="Malgun Gothic")
if plt.get_fignums():
    plt.show()

year = [2018, 2019, 2020, 2021, 2022, 2023]
python = [5.8, 8.17, 9.31, 11.87, 15.63, 14.51]
C = [13.59, 14.08, 16.72, 14.32, 12.71, 14.73]
java = [15.78, 15.04, 16.73, 11.23, 10.82, 13.23]
JS = [3.49, 2.51, 2.38, 2.44, 2.12, 2.1]

plt.plot(year, python)
plt.show()

plt.title("파이썬의 언어 점유율")
plt.plot(year, python)
if plt.get_fignums():
    plt.show()

plt.title("파이썬의 언어 점유율")
plt.xlabel("연도")
plt.ylabel("점유율")
plt.plot(year, python)
if plt.get_fignums():
    plt.show()

plt.title("파이썬의 언어 점유율", fontsize=20)
plt.xlabel("연도", fontsize=15)
plt.ylabel("점유율", fontsize=15)
plt.plot(year, python)
if plt.get_fignums():
    plt.show()

plt.title("프로그래밍 언어 점유율", fontsize=20)
plt.xlabel("연도", fontsize=15)
plt.ylabel("점유율", fontsize=15)
plt.plot(year, python)

plt.plot(year, C)
plt.plot(year, java)
plt.plot(year, JS)
if plt.get_fignums():
    plt.show()

plt.title("프로그래밍 언어 점유율", fontsize=20)
plt.xlabel("연도", fontsize=15)
plt.ylabel("점유율", fontsize=15)

plt.plot(year, python)
plt.plot(year, C)
plt.plot(year, java)
plt.plot(year, JS)

plt.legend(['Python', 'C', 'JAVA', 'Java Script'])
if plt.get_fignums():
    plt.show()

plt.title("프로그래밍 언어 점유율", fontsize=20)
plt.xlabel("연도", fontsize=15)
plt.ylabel("점유율", fontsize=15)

plt.plot(year, python, label="Python")
plt.plot(year, C, label="C")
plt.plot(year, java, label="JAVA")
plt.plot(year, JS, label="Java Script")

plt.legend()
if plt.get_fignums():
    plt.show()

fig1 = plt.figure(1,figsize=(4,3))
plt.plot(year, python, label="Python")
plt.title("fig1")

fig2 = plt.figure(2,figsize=(4,3))
plt.plot(year, java, label="JAVA")
plt.title("fig2")

plt.show()

fig2

fig1 = plt.figure(1, figsize=(4, 3))
plt.plot(year, python, label="Python")
plt.title("fig1")

fig2 = plt.figure( 2, figsize=(4, 3))
plt.title("fig2")

plt.figure(1)
plt.plot(year, java, label="JAVA")

plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(year, python)
ax2.plot(year, java)

plt.show()

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(year, python)
ax2.plot(year, java)

plt.show()

ax1.set_title("ax1의 제목")
ax2.set_title("ax2의 제목")
fig

fig, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True)
ax1.plot(year, python)
ax1.set_title("ax1의 제목")
ax1.set_xlabel("x라벨")

ax2.plot(year, java)
ax2.set_title("ax2의 제목")

plt.show()

todo_fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)

ax1.plot(year, python)
ax1.set(title="파이썬의 점유율", xlabel="연도", ylabel="점유율")

ax2.plot(year, java)
ax2.set(title="자바의 점유율", xlabel="연도")
plt.show()
