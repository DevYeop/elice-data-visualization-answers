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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# pd.read_csv를 통하여 공항기상관측(AMOS) 기상청 데이터를 데이터프레임 형태로 읽어옵니다.
amos_all = pd.read_csv("amos_rawdata.csv")

# %%
# 공항기상관측(AMOS) 상위 5개 데이터를 출력합니다.
amos_all.head()

# %%
amos_all["일시"] = pd.to_datetime(amos_all["일시"])

# 데이터프레임 정보를 요약하여 출력합니다.
amos_all.info()

# %%
unique_time_list = sorted(list(set(amos_all['일시']))) # 측정 일시 종류 확인
print(unique_time_list) # AMOS 측정 일시 데이터 확인
print(len(set(amos_all['일시']))) # 측정 일시 종류 확인

# %%
# amos_all DataFrame 지점명 데이터 확인
print(sorted(list(set(amos_all['지점명'])))) # AMOS 측정 지점명 데이터 확인
print(len(set(amos_all['지점명']))) # 측정 지점명 종류 확인

# %%
# amos_all DataFrame 통계수치 확인
amos_all.describe()

# %%
precipitation = amos_all["강수량(mm)"]
precipitation_mean = precipitation.mean()
precipitation_std = precipitation.std()

# %%
print("측정 시작일: ", amos_all['일시'].iloc[0]) # 정렬되어 있으므로 0번째 데이터가 시작일
print("측정 종료일: ", amos_all['일시'].iloc[-1]) # 정렬되어 있으므로 마지막 데이터가 종료일

# %%
amos_gimpo = amos_all[amos_all['지점명'] == '김포공항'] # 김포공항 데이터만 추출

# %%
amos_gimpo

# %%
# 불필요한 지점 컬럼 제거
amos_gimpo = amos_gimpo.drop(['지점'], axis=1)
# 측정 일시에 따라 정렬
amos_gimpo.sort_values(by='일시', inplace=True)

amos_gimpo

# %%
# 강수량의 결측치를 0으로 대체
amos_gimpo.loc[amos_gimpo['강수량(mm)'].isnull(), '강수량(mm)'] = 0

# %%
# 결측치 개수 확인
amos_gimpo.isnull().sum()

# %%
def knot_to_ms(knot):
    return knot * 0.514444

amos_gimpo['풍속(m/s)'] = knot_to_ms(amos_gimpo['풍속(KT)'])

# %%
yangyang_wind = amos_all.loc[amos_all["지점명"].eq("양양공항"), "풍속(KT)"]
yangyang_wind_speed_mean = knot_to_ms(yangyang_wind).mean()

# %%
# 측정 시간에 따른 풍속 변화 확인
plt.figure(figsize=(15, 5))


plt.plot(amos_gimpo['일시'], amos_gimpo['풍속(m/s)'])
if plt.get_fignums():
    plt.show()

# %%
# 측정 시간에 따른 기온 변화 확인 (전체 지점)
# 일반 plot과 이동 평균을 같이 확인

plt.figure(figsize=(15, 5))

window_size = 120 # 5일 치 데이터를 이용하여 이동 평균 계산

plt.plot(amos_gimpo['일시'], amos_gimpo['풍속(m/s)'], alpha=0.5)
plt.plot(amos_gimpo['일시'], amos_gimpo['풍속(m/s)'].rolling(window=window_size).mean())
if plt.get_fignums():
    plt.show()

# %%
# 측정 시간에 따른 기온 변화 확인
plt.figure(figsize=(15, 5))

plt.plot(amos_gimpo['일시'], amos_gimpo['기온(°C)'])
if plt.get_fignums():
    plt.show()

# %%
plt.figure(figsize=(15, 5))

plt.plot(amos_gimpo['일시'], amos_gimpo['기온(°C)'])
plt.plot(amos_gimpo['일시'], amos_gimpo['이슬점온도(°C)'])
if plt.get_fignums():
    plt.show()

# %%
plt.figure(figsize=(15, 5))

plt.plot(amos_gimpo['일시'], amos_gimpo['강수량(mm)'])
if plt.get_fignums():
    plt.show()

# %%
# 여름철 데이터

amos_gimpo['일시(월)'] = amos_gimpo['일시'].dt.month

amos_gimpo_summer = amos_gimpo[(amos_gimpo['일시(월)'] >= 6) & (amos_gimpo['일시(월)'] <= 8)]
amos_gimpo_winter = amos_gimpo[(amos_gimpo['일시(월)'] >= 12) | (amos_gimpo['일시(월)'] <= 2)]

# %%
plt.figure(figsize=(15, 5))

plt.hist(amos_gimpo_summer['강수량(mm)'], bins=100, alpha=0.5, label='Summer', color = 'r')
plt.hist(amos_gimpo_winter['강수량(mm)'], bins=100, alpha=0.5, label='Winter', color = 'b')

plt.legend()
if plt.get_fignums():
    plt.show()

# %%
amos_gimpo_summer.loc[amos_gimpo_summer['강수량(mm)'] > 0]

# %%
plt.figure(figsize=(15, 5))


plt.hist(amos_gimpo_summer.loc[amos_gimpo_summer['강수량(mm)'] > 0]['강수량(mm)'], alpha=0.5, label='Summer', color = 'r',range=(0,30), bins=50)
plt.hist(amos_gimpo_winter.loc[amos_gimpo_winter['강수량(mm)'] > 0]['강수량(mm)'], alpha=0.5, label='Winter', color = 'b',range=(0,30), bins=50)

plt.legend()
if plt.get_fignums():
    plt.show()

# %%
rainy_day_count = int(amos_gimpo["강수량(mm)"].gt(0).sum())

# %%
summer_precipitation = amos_gimpo_summer["강수량(mm)"]
summer_precipitation_mean = summer_precipitation[summer_precipitation.gt(0)].mean()

# %%
ans = {
    "퀴즈1": (float(precipitation_mean), float(precipitation_std)),
    "퀴즈2": float(yangyang_wind_speed_mean),
    "퀴즈3": (float(rainy_day_count), float(summer_precipitation_mean)),
}

print(ans)
