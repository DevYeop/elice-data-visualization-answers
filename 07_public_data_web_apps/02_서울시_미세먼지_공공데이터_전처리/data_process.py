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
import os
import pandas as pd

# %%
data_dir = "Seoul_20221231"
filelist = os.listdir(data_dir)
filelist

# %%
df = pd.DataFrame()
for i in filelist:
    df = pd.concat([df,pd.read_csv(os.path.join(data_dir,i),encoding="euckr")],axis=0)
df

# %%
from datetime import datetime
import re

df["일시"] = df["일시"].apply(lambda x : re.sub(" ([0-9]):"," 0\\1:",x)).apply(datetime.fromisoformat)
df

# %%
df = df.sort_values(by=["일시","구분"])
df

# %%
df.reset_index(inplace=True)
# df.to_csv("서울시 미세먼지.csv",index=False)
del df["index"]
df

# %%
df["초미세먼지(PM2.5)"] = df.where(pd.notnull(df),df['초미세먼지(PM25)'],axis=0)["초미세먼지(PM2.5)"]
del df['초미세먼지(PM25)']
df

# %%
import plotly.express  as px

# 시간이 조금 걸립니다.
fig = px.line(df,x="일시",y="초미세먼지(PM2.5)",
              title="서울시 구별 미세먼지",
              color='구분',
              line_group='구분',
              hover_name="구분")
fig

# %%
df = df[df["일시"]> datetime(2014,1,1)]

fig = px.line(df,x="일시",y="초미세먼지(PM2.5)",
              title="서울시 구별 미세먼지",
              color='구분',
              line_group='구분',
              hover_name="구분")
fig

# %%
pivot_table = pd.pivot_table(df,index="구분",values=["미세먼지(PM10)","초미세먼지(PM2.5)"],aggfunc="mean")

# %%
pivot_table["지역구"] = pivot_table.index

# %%
fig = px.bar(pivot_table, y='미세먼지(PM10)',color="지역구")
fig.show()

# %%
from pathlib import Path

output = Path("../seoul.csv.gz")
temporary_output = output.with_name("seoul.tmp.csv.gz")
df.to_csv(temporary_output, encoding="utf-8-sig", index=False)
temporary_output.replace(output)
