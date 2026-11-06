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

amos_all = pd.read_csv("amos_rawdata.csv")

amos_all.head()

amos_all["일시"] = pd.to_datetime(amos_all["일시"])

amos_all.info()

unique_time_list = sorted(list(set(amos_all['일시'])))
print(unique_time_list)
print(len(set(amos_all['일시'])))

print(sorted(list(set(amos_all['지점명']))))
print(len(set(amos_all['지점명'])))

amos_all.describe()

precipitation = amos_all["강수량(mm)"]
precipitation_mean = precipitation.mean()
precipitation_std = precipitation.std()

print("측정 시작일: ", amos_all['일시'].iloc[0])
print("측정 종료일: ", amos_all['일시'].iloc[-1])

amos_gimpo = amos_all[amos_all['지점명'] == '김포공항']

amos_gimpo

amos_gimpo = amos_gimpo.drop(['지점'], axis=1)

amos_gimpo.sort_values(by='일시', inplace=True)

amos_gimpo

amos_gimpo.loc[amos_gimpo['강수량(mm)'].isnull(), '강수량(mm)'] = 0

amos_gimpo.isnull().sum()

def knot_to_ms(knot):
    return knot * 0.514444

amos_gimpo['풍속(m/s)'] = knot_to_ms(amos_gimpo['풍속(KT)'])

yangyang_wind = amos_all.loc[amos_all["지점명"].eq("양양공항"), "풍속(KT)"]
yangyang_wind_speed_mean = knot_to_ms(yangyang_wind).mean()

plt.figure(figsize=(15, 5))

plt.plot(amos_gimpo['일시'], amos_gimpo['풍속(m/s)'])
if plt.get_fignums():
    plt.show()

plt.figure(figsize=(15, 5))

window_size = 120

plt.plot(amos_gimpo['일시'], amos_gimpo['풍속(m/s)'], alpha=0.5)
plt.plot(amos_gimpo['일시'], amos_gimpo['풍속(m/s)'].rolling(window=window_size).mean())
if plt.get_fignums():
    plt.show()

plt.figure(figsize=(15, 5))

plt.plot(amos_gimpo['일시'], amos_gimpo['기온(°C)'])
if plt.get_fignums():
    plt.show()

plt.figure(figsize=(15, 5))

plt.plot(amos_gimpo['일시'], amos_gimpo['기온(°C)'])
plt.plot(amos_gimpo['일시'], amos_gimpo['이슬점온도(°C)'])
if plt.get_fignums():
    plt.show()

plt.figure(figsize=(15, 5))

plt.plot(amos_gimpo['일시'], amos_gimpo['강수량(mm)'])
if plt.get_fignums():
    plt.show()

amos_gimpo['일시(월)'] = amos_gimpo['일시'].dt.month

amos_gimpo_summer = amos_gimpo[(amos_gimpo['일시(월)'] >= 6) & (amos_gimpo['일시(월)'] <= 8)]
amos_gimpo_winter = amos_gimpo[(amos_gimpo['일시(월)'] >= 12) | (amos_gimpo['일시(월)'] <= 2)]

plt.figure(figsize=(15, 5))

plt.hist(amos_gimpo_summer['강수량(mm)'], bins=100, alpha=0.5, label='Summer', color = 'r')
plt.hist(amos_gimpo_winter['강수량(mm)'], bins=100, alpha=0.5, label='Winter', color = 'b')

plt.legend()
if plt.get_fignums():
    plt.show()

amos_gimpo_summer.loc[amos_gimpo_summer['강수량(mm)'] > 0]

plt.figure(figsize=(15, 5))

plt.hist(amos_gimpo_summer.loc[amos_gimpo_summer['강수량(mm)'] > 0]['강수량(mm)'], alpha=0.5, label='Summer', color = 'r',range=(0,30), bins=50)
plt.hist(amos_gimpo_winter.loc[amos_gimpo_winter['강수량(mm)'] > 0]['강수량(mm)'], alpha=0.5, label='Winter', color = 'b',range=(0,30), bins=50)

plt.legend()
if plt.get_fignums():
    plt.show()

rainy_day_count = int(amos_gimpo["강수량(mm)"].gt(0).sum())

summer_precipitation = amos_gimpo_summer["강수량(mm)"]
summer_precipitation_mean = summer_precipitation[summer_precipitation.gt(0)].mean()

ans = {
    "퀴즈1": (float(precipitation_mean), float(precipitation_std)),
    "퀴즈2": float(yangyang_wind_speed_mean),
    "퀴즈3": (float(rainy_day_count), float(summer_precipitation_mean)),
}

print(ans)
