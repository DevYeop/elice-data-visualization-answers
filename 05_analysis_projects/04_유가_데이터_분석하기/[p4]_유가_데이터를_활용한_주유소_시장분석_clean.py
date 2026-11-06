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
import seaborn as sns
sns.set_style('darkgrid')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus']=False
if plt.get_fignums():
    plt.show()

f18 = pd.read_csv(f'./data/과거_판매가격(주유소)_2018.csv')

f18.head()

f18 = f18.drop(0)

f18.isna().sum()

f18.describe(include='all')

f18['기간'] = f18['기간'].apply(lambda x:pd.to_datetime(str(int(x))))

region_len = f18['지역'].apply(lambda x: len(x.split()))
print(f"min: {min(region_len)},max: {max(region_len)}")

f18['지역2'] = f18['지역'].apply(lambda x:x.split()[0])
import collections
collections.Counter(f18['지역2'])

f18.loc[f18['휘발유']==0].head(10)

f18.loc[f18['번호']=='A0010629']

f18 = f18.loc[f18['휘발유']!=0,:]

f18.describe(include='all')

unique_count = f18.groupby('번호')[['지역','상표','셀프여부']].nunique()
unique_count.head()

target = unique_count.loc[(unique_count!=1).sum(axis=1)!=0]
target

f18.loc[f18['번호'].isin(target.index)]

f18 = f18.loc[~f18['번호'].isin(target.index)]

f18 = f18.groupby('번호')\
    .agg({'지역':'first','지역2':'first','상표':'first','셀프여부':'first','휘발유':'mean'})\
    .reset_index()

f18.describe(include='all')

def preprocess(df):
    df_copy=df.copy()

    df = df.drop(0)
    df['기간'] = df['기간'].apply(lambda x:pd.to_datetime(str(int(x))))
    df['지역2'] = df['지역'].apply(lambda x:x.split()[0])
    df = df.loc[df['휘발유']!=0,:]
    unique_count = df.groupby('번호')[['번호','지역','상표','셀프여부']].nunique()
    target = unique_count.loc[(unique_count!=1).sum(axis=1)!=0,:]
    df = df.loc[~df['번호'].isin(target.index),:]
    df = df.groupby('번호')\
        .agg({'지역':'first','지역2':'first','상표':'first','셀프여부':'first','휘발유':'mean'})\
        .reset_index()

    out = set(df_copy['번호']).difference(set(df['번호']))
    return(df,out)

f_dict = dict()
out_all = set()
for year in range(2018,2022):
    df = pd.read_csv(f'./data/과거_판매가격(주유소)_{year}.csv')
    f_dict[year], out = preprocess(df)
    out_all.update(out)

key = list(f_dict[2018].columns)
key.remove('휘발유')
print(key)

m1 = pd.merge(f_dict[2018],f_dict[2019],on=key,how='outer',suffixes=('_2018', '_2019'))
m2 = pd.merge(f_dict[2020],f_dict[2021],on=key,how='outer',suffixes=('_2020', '_2021'))
m = pd.merge(m1,m2,on=key,how='outer')

m.head()

m.groupby('번호').size().sort_values(ascending=False).head()

m.loc[m['번호']=='A0019752']

(m.groupby('번호').size()>1).sum()

key.remove('상표')
key

m1 = pd.merge(f_dict[2018],f_dict[2019],on=key,how='outer',suffixes=('_2018', '_2019'))
m2 = pd.merge(f_dict[2020],f_dict[2021],on=key,how='outer',suffixes=('_2020', '_2021'))
m = pd.merge(m1,m2,on=key,how='outer')

m.head()

size = m.groupby('번호').size().sort_values(ascending=False)
size.head()

target = size[size>1].index
m.loc[m['번호'].isin(target)].sort_values('번호')

m = m.loc[~m['번호'].isin(target)]
m.groupby('번호').size().sort_values(ascending=False).head()

m = m.loc[[x not in out_all for x in m['번호']]]

m.head()

id_dict=dict()
for year in range(2018,2022):
    id_dict[year] = set(m.loc[~m[f'상표_{year}'].isna()]['번호'].unique())

diff_dict=dict()
for year in range(2018,2021):
    opened = len(id_dict[year+1].difference(id_dict[year]))
    closed = len(id_dict[year].difference(id_dict[year+1]))
    diff_dict[f'{year}_{year+1}']=[opened,closed]
diff_df = pd.DataFrame(diff_dict,index=['OPENED','CLOSED'])

diff_df

diff_df.plot()
if plt.get_fignums():
    plt.show()

diff_df.T.plot(color=['r','b'])
if plt.get_fignums():
    plt.show()

opened_2020 = id_dict[2020] - id_dict[2019]
quiz_1 = int(m.loc[m["번호"].isin(opened_2020), "셀프여부"].eq("셀프").sum())

brand_price_dict=dict()
for year in range(2018,2022):
    brand_price_dict[str(year)]=m.groupby(f'상표_{year}')[f'휘발유_{year}'].mean()

brand_price_df = pd.DataFrame(brand_price_dict)
brand_price_df

brand_price_df = brand_price_df.drop('SK가스')
brand_price_df.T.plot(figsize=(10,5))
if plt.get_fignums():
    plt.show()

brand_share_dict=dict()
for year in range(2018,2022):
    brand_share_dict[str(year)]=m.groupby(f'상표_{year}').size()

brand_share_df = pd.DataFrame(brand_share_dict)
brand_share_df

brand_share_df = brand_share_df.drop('SK가스')
brand_ratio_df = brand_share_df.apply(lambda x:x/brand_share_df.sum(),axis=1)
brand_ratio_df = brand_ratio_df.sort_values('2018',ascending=False)

brand_ratio_df

brand_ratio_df.T.plot(kind='bar',stacked=True,rot=0,figsize=(10,5))
plt.legend(bbox_to_anchor=(1, 1))
if plt.get_fignums():
    plt.show()

plt.figure(figsize=(10,5))
sns.heatmap(brand_ratio_df, cmap= 'RdBu_r', linewidths=1, linecolor='black',annot=True)
if plt.get_fignums():
    plt.show()

stations_2019 = m.loc[m["번호"].isin(id_dict[2019]), "셀프여부"]
quiz_2 = round(float(stations_2019.eq("일반").mean()), 2)

sns.boxplot(x=m['휘발유_2021'])
if plt.get_fignums():
    plt.show()

boxplot_order = m.groupby('지역2')['휘발유_2021'].median().sort_values(ascending=False).index
plt.figure(figsize=(15,7))
sns.boxplot(x="지역2", y="휘발유_2021", data=m, orient="v", order=boxplot_order)
if plt.get_fignums():
    plt.show()

student_answers = {}
student_answers["problem_1"] = int(quiz_1)
student_answers["problem_2"] = float(quiz_2)

print(student_answers)
