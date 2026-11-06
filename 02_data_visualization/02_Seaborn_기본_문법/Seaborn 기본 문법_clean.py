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

year = [2018, 2019, 2020, 2021, 2022, 2023]
python = [5.8, 8.17, 9.31, 11.87, 15.63, 14.51]
C = [13.59, 14.08, 16.72, 14.32, 12.71, 14.73]
java = [15.78, 15.04, 16.73, 11.23, 10.82, 13.23]
JS = [3.49, 2.51, 2.38, 2.44, 2.12, 2.1]

sns.lineplot(x=year, y=python)
if plt.get_fignums():
    plt.show()

sns.lineplot(x=year, y=python, label="python")
sns.lineplot(x=year, y=java, label="java")
if plt.get_fignums():
    plt.show()

lp= sns.lineplot(x=year, y=python, label="python")

lp.set_xlabel("연도")
lp.set_ylabel("점유율")
if plt.get_fignums():
    plt.show()

sns.set_style("darkgrid", rc={"font.family": "Malgun Gothic"})
lp = sns.lineplot(x=year, y=python, label="python")
if plt.get_fignums():
    plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)

fig = sns.lineplot(x=year, y=python, label="python", ax=ax1)
sns.lineplot(x=year, y=java, label="java", ax=ax2)
if plt.get_fignums():
    plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)
sns.lineplot(x=year, y=C, label="C", ax=ax1)
sns.lineplot(x=year, y=JS, label="JS", ax=ax2)
plt.show()
