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
import seaborn as sns
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="folium")

# %%
case_counts = pd.read_csv("./data/서울시 코로나19 일자·지역별 집계.csv")
# countplot에서 집계 건수를 반영하도록 일자·지역 행을 건수만큼 반복합니다.
corona_all = case_counts.loc[case_counts.index.repeat(case_counts["확진자수"]), ["확진일", "지역"]].reset_index(drop=True)

# %%
# 상위 5개 데이터를 출력합니다.
corona_all.head()

# %%
# dataframe 정보를 요약하여 출력합니다.
corona_all.info()

# %%
corona_del_col = corona_all.copy()

# %%
# 정제 처리된 dataframe 정보를 출력합니다.
corona_del_col.info()

# %%
corona_del_col['확진일']

# %%
# dataframe에 추가하기 전, 임시로 데이터를 저장해 둘 list를 선언합니다.
month = []
day = []

for data in corona_del_col['확진일']:
    # split 함수를 사용하여 월, 일을 나누어 list에 저장합니다.
    month.append(data.split('.')[0])
    day.append(data.split('.')[1])

# %%
# corona_del_col에 `month`, `day` column을 생성하며 동시에 list에 임시 저장된 데이터를 입력합니다.
corona_del_col['month'] = month
corona_del_col['day'] = day

# %%
# 그래프에서 x축의 순서를 정리하기 위하여 order list를 생성합니다.
order = []
for i in range(1,11):
    order.append(str(i))

order

# %%
# 그래프의 사이즈를 조절합니다.
plt.figure(figsize=(10,5))

# seaborn의 countplot 함수를 사용하여 출력합니다.
sns.set(style="darkgrid", font="Malgun Gothic")
ax = sns.countplot(x="month", data=corona_del_col, palette="Set2", order = order)
if plt.get_fignums():
    plt.show()

# %%
# series의 plot 함수를 사용한 출력 방법도 있습니다.
corona_del_col['month'].value_counts().plot(kind='bar')
if plt.get_fignums():
    plt.show()

# %%
# value_counts()는 각 데이터를 세어서 내림차순으로 정리하는 함수입니다.
corona_del_col['month'].value_counts()

# %%
# 그래프에서 x축의 순서를 정리하기 위하여 order list를 생성합니다.
order2 = []
for i in range(1,32):

    order2.append(str(i))

order2

# %%
# seaborn의 countplot 함수를 사용하여 출력합니다.
plt.figure(figsize=(20,10))
sns.set(style="darkgrid", font="Malgun Gothic")
ax = sns.countplot(x="day", data=corona_del_col[corona_del_col['month'] == '8'], palette="rocket_r", order = order2)
if plt.get_fignums():
    plt.show()

# %%
quiz_1 = float(corona_del_col["month"].eq("8").sum() / 31)

# %%
corona_del_col['지역']

# %%
import matplotlib.font_manager as fm

# %%
plt.figure(figsize=(20,10))
# 한글 출력을 위해서 폰트 옵션을 설정합니다.
sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style='darkgrid')
ax = sns.countplot(x="지역", data=corona_del_col, palette="Set2")
if plt.get_fignums():
    plt.show()

# %%
# replace 함수를 사용하여 해당 데이터를 변경합니다.
# 이상치가 처리된 데이터이기에 새로운 Dataframe으로 저장합니다.
corona_out_region = corona_del_col.replace({'종랑구':'중랑구', '한국':'기타'})

# %%
# 이상치가 처리된 데이터를 다시 출력해 봅시다.
plt.figure(figsize=(20,10))
sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style='darkgrid')
ax = sns.countplot(x="지역", data=corona_out_region, palette="Set2")
if plt.get_fignums():
    plt.show()

# %%
# 논리연산을 이용한 조건을 다음과 같이 사용하면 해당 조건에 맞는 데이터를 출력할 수 있습니다.
corona_out_region[corona_del_col['month'] == '8']

# %%
# 그래프를 출력합니다.
plt.figure(figsize=(20,10))
sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style='darkgrid')
ax = sns.countplot(x="지역", data=corona_out_region[corona_del_col['month'] == '8'], palette="Set2")
if plt.get_fignums():
    plt.show()

# %%
# 해당 column을 지정하여 series 형태로 출력할 수 있습니다.
corona_out_region['month'][corona_out_region['지역'] == '관악구']

# %%
# 그래프를 출력합니다.
plt.figure(figsize=(10,5))
sns.set(style="darkgrid", font="Malgun Gothic")
ax = sns.countplot(x="month", data=corona_out_region[corona_out_region['지역'] == '관악구'], palette="Set2", order = order)
if plt.get_fignums():
    plt.show()

# %%
# 지도 출력을 위한 라이브러리 folium을 import 합니다.
import folium

# Map 함수를 사용하여 지도를 출력합니다.
map_osm = folium.Map(location=[37.529622, 126.984307], zoom_start=11)

map_osm

# %%
# CRS에 저장합니다.
CRS=pd.read_csv("./data/서울시 행정구역 시군구 정보 (좌표계_ WGS1984).csv")

# %%
# Dataframe을 출력해 봅니다.
CRS

# %%
CRS[CRS['시군구명_한글'] == '중구']

# %%
# corona_out_region의 지역에는 'oo구' 이외로 `타시도`, `기타`에 해당되는 데이터가 존재 합니다.
# 위 데이터에 해당되는 위도, 경도를 찾을 수 없기에 삭제하여 corona_seoul로 저장합니다.
corona_seoul = corona_out_region.drop(corona_out_region[corona_out_region['지역'] == '타시도'].index)
corona_seoul = corona_seoul.drop(corona_out_region[corona_out_region['지역'] == '기타'].index)

# 서울 중심지 중구를 가운데 좌표로 잡아 지도를 출력합니다.
map_osm = folium.Map(location=[37.557945, 126.99419], zoom_start=11)

# 지역 정보를 set 함수를 사용하여 25개 고유의 지역을 뽑아냅니다.
for region in set(corona_seoul['지역']):

    # 해당 지역의 데이터 개수를 count에 저장합니다.
    count = len(corona_seoul[corona_seoul['지역'] == region])
    # 해당 지역의 데이터를 CRS에서 뽑아냅니다.
    CRS_region = CRS[CRS['시군구명_한글'] == region]

    # CircleMarker를 사용하여 지역마다 원형마커를 생성합니다.
    marker = folium.CircleMarker([CRS_region['위도'], CRS_region['경도']], # 위치
                                  radius=count/10 + 10,                 # 범위
                                  color='#3186cc',            # 선 색상
                                  fill_color='#3186cc',       # 면 색상
                                  popup=' '.join((region, str(count), '명'))) # 팝업 설정

    # 생성한 원형마커를 지도에 추가합니다.
    marker.add_to(map_osm)

map_osm

# %%
june_cases = corona_out_region.loc[corona_out_region["month"].eq("6"), "지역"]
quiz_2 = june_cases.value_counts().idxmax()

# %%
student_answers = {}
student_answers["problem_1"] = quiz_1
student_answers["problem_2"] = quiz_2

print(student_answers)
