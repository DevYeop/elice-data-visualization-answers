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
# 🦁[복잡해보이는 코드해설-1] data_2019 = df[df["연"] == 2019][["어른", "청소년", "어린이"]].sum()
# 하나씩 주석을 풀어보며 보면 이해가 쉽다

# 조건설정
df["연"] == 2019

# 조건에 부합하는 데이터 추출
df[df["연"] == 2019]

# 조건에 부합하는 데이터 추출``. 근데 거기서 "어른", "청소년", "어린이" 컬럼만 추출
df[df["연"] == 2019][["어른", "청소년", "어린이"]]

# 조건에 부합하는 데이터 추출. 근데 거기서 "어른", "청소년", "어린이" 컬럼만 추출.... 하는 데 각 합계로 처리
df[df["연"] == 2019][["어른", "청소년", "어린이"]].sum()

# %%
# 2019년의 어른, 청소년, 어린이 입장 분포 보기
data_2019 = df[df["연"] == 2019][["어른", "청소년", "어린이"]].sum()

data_2019
# print(type(data_2019))

# %%
# 🦁 헷갈리는 일반 컬럼과 인덱스 컬럼의 차이 설명

df_tmp = pd.DataFrame({
    "이름": ["철수", "민수", "철수"],
    "나이": [25, 28, 30]
})
print(df_tmp)

df_tmp2 = pd.DataFrame({
    "이름": ["철수", "민수", "철수"],
    "나이": [25, 28, 30]
}, index=["A", "B", "C"])
print(df_tmp2)

df_tmp3 = pd.DataFrame({
    "이름": ["김씨", "이씨", "박씨"],
    "나이": [25, 28, 30]
}, index=[1, 3, 2])
print(df_tmp3.sort_index())  # 인덱스 기준으로 정렬

# %%
labels = data_2019.index
data = data_2019
data
print(data)
print(labels)

# %%
plt.pie(x=data, labels=labels)
plt.legend(title="2019년 입장객 분포", loc="best")
plt.show()

# %%
# 🦁 앞의내용과 같으나, 파이조각별 퍼센테이지를 표시하는 옵션만 다르다.
plt.pie(x=data, labels=labels, autopct="%1.1f%%") # 소수점 1자리까지
# plt.pie(x=data, labels=labels, autopct="%.1f%%") # 축약된 표현.
# plt.pie(x=data, labels=labels, autopct="%.2f%%") # 축약된 표현. 소수점 2자리까지
plt.show()

# %%
df_sat = df[df["요일"] == "토"]  # 토요일 데이터를 df_sat에 저장
df_sat

# 🦁
# bins: 몇개의 구간으로 나눌 것인가 -> 막대기 차트의 갯수를 말한다.
plt.hist(df_sat["어린이"], bins=10, edgecolor="black")
plt.show()

# %%
plt.hist(df_sat["어린이"], histtype="bar")
plt.title("bar")
plt.figure()

plt.hist(df_sat["어린이"], histtype="barstacked")
plt.title("barstacked")
plt.figure()

plt.hist(df_sat["어린이"], histtype="step")
plt.title("step")
plt.figure()

plt.hist(df_sat["어린이"], histtype="stepfilled")
plt.title("stepfilled")
plt.show()

# %%
# plt.hist(df_sat["어린이"], histtype="stepfilled")
# plt.title("stepfilled")
# plt.show()

# 🦁 문법만 대동소이하다.
sns.histplot(data=df_sat, x="어린이")
plt.show()

# %%
df_feb = df[df["월"] == 2]

sns.histplot(data=df_feb, x="어린이", hue="연")
if plt.get_fignums():
    plt.show()

# %%
# 🦁
# bins : 막대의 수, 구간의 수
# bin_range : x축에 표시할 데이터 범위 지정. 지정되지 않은 그외 값은 제외된다
sns.histplot(data=df_feb, x="어린이", hue="연",binrange=(0,1000), bins = 20)
if plt.get_fignums():
    plt.show()

# %%
sns.histplot(
    data=df_feb,
    x="어린이",
    hue="연",
    binrange=(0, 800),
    bins=10,
    # multiple="layer", # 막대를 겹치게 표시
    multiple="dodge", # 막대를 겹치지 않게 표시 🦁
    shrink=0.9, #값이 낮을수록 막대의 폭이 좁아진다 🦁
)
if plt.get_fignums():
    plt.show()

# %%
# 🦁 조건이 2개를 만족시키는 조건을 찾기위해,  &(앰퍼샌드) AND 조건 연산자가 붙는다
df_april2017 = df[(df["연"] == 2017) & (df["월"] == 4)]
todo1 = sns.histplot(data=df_april2017, x="어른", bins=20)
if plt.get_fignums():
    plt.show()
