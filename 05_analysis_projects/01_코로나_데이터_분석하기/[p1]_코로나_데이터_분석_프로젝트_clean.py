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
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="folium")

case_counts = pd.read_csv("./data/서울시 코로나19 일자·지역별 집계.csv")

corona_all = case_counts.loc[case_counts.index.repeat(case_counts["확진자수"]), ["확진일", "지역"]].reset_index(drop=True)

corona_all.head()

corona_all.info()

corona_del_col = corona_all.copy()

corona_del_col.info()

corona_del_col['확진일']

month = []
day = []

for data in corona_del_col['확진일']:

    month.append(data.split('.')[0])
    day.append(data.split('.')[1])

corona_del_col['month'] = month
corona_del_col['day'] = day

order = []
for i in range(1,11):
    order.append(str(i))

order

plt.figure(figsize=(10,5))

sns.set(style="darkgrid", font="Malgun Gothic")
ax = sns.countplot(x="month", data=corona_del_col, palette="Set2", order = order)
if plt.get_fignums():
    plt.show()

corona_del_col['month'].value_counts().plot(kind='bar')
if plt.get_fignums():
    plt.show()

corona_del_col['month'].value_counts()

order2 = []
for i in range(1,32):

    order2.append(str(i))

order2

plt.figure(figsize=(20,10))
sns.set(style="darkgrid", font="Malgun Gothic")
ax = sns.countplot(x="day", data=corona_del_col[corona_del_col['month'] == '8'], palette="rocket_r", order = order2)
if plt.get_fignums():
    plt.show()

quiz_1 = float(corona_del_col["month"].eq("8").sum() / 31)

corona_del_col['지역']

import matplotlib.font_manager as fm

plt.figure(figsize=(20,10))

sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style='darkgrid')
ax = sns.countplot(x="지역", data=corona_del_col, palette="Set2")
if plt.get_fignums():
    plt.show()

corona_out_region = corona_del_col.replace({'종랑구':'중랑구', '한국':'기타'})

plt.figure(figsize=(20,10))
sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style='darkgrid')
ax = sns.countplot(x="지역", data=corona_out_region, palette="Set2")
if plt.get_fignums():
    plt.show()

corona_out_region[corona_del_col['month'] == '8']

plt.figure(figsize=(20,10))
sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style='darkgrid')
ax = sns.countplot(x="지역", data=corona_out_region[corona_del_col['month'] == '8'], palette="Set2")
if plt.get_fignums():
    plt.show()

corona_out_region['month'][corona_out_region['지역'] == '관악구']

plt.figure(figsize=(10,5))
sns.set(style="darkgrid", font="Malgun Gothic")
ax = sns.countplot(x="month", data=corona_out_region[corona_out_region['지역'] == '관악구'], palette="Set2", order = order)
if plt.get_fignums():
    plt.show()

import folium

map_osm = folium.Map(location=[37.529622, 126.984307], zoom_start=11)

map_osm

CRS=pd.read_csv("./data/서울시 행정구역 시군구 정보 (좌표계_ WGS1984).csv")

CRS

CRS[CRS['시군구명_한글'] == '중구']

corona_seoul = corona_out_region.drop(corona_out_region[corona_out_region['지역'] == '타시도'].index)
corona_seoul = corona_seoul.drop(corona_out_region[corona_out_region['지역'] == '기타'].index)

map_osm = folium.Map(location=[37.557945, 126.99419], zoom_start=11)

for region in set(corona_seoul['지역']):

    count = len(corona_seoul[corona_seoul['지역'] == region])

    CRS_region = CRS[CRS['시군구명_한글'] == region]

    marker = folium.CircleMarker([CRS_region['위도'], CRS_region['경도']],
                                  radius=count/10 + 10,
                                  color='#3186cc',
                                  fill_color='#3186cc',
                                  popup=' '.join((region, str(count), '명')))

    marker.add_to(map_osm)

map_osm

june_cases = corona_out_region.loc[corona_out_region["month"].eq("6"), "지역"]
quiz_2 = june_cases.value_counts().idxmax()

student_answers = {}
student_answers["problem_1"] = quiz_1
student_answers["problem_2"] = quiz_2

print(student_answers)
