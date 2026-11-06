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

asos_all = pd.read_csv("dataset/asos_rawdata.csv")

asos_all.head()

asos_all["일시"] = pd.to_datetime(asos_all["일시"])

asos_all.info()

unique_time_list = sorted(list(set(asos_all['일시'])))
print(unique_time_list)
print(len(set(asos_all['일시'])))

print(sorted(list(set(asos_all['지점명']))))
print(len(set(asos_all['지점명'])))

asos_all.describe()

asos_ulsan = asos_all[asos_all['지점명'] == '울산']
asos_incheon = asos_all[asos_all['지점명'] == '인천']

asos_ulsan

print(asos_ulsan['지점명'].unique())
print(asos_incheon['지점명'].unique())

asos_ulsan.loc[asos_ulsan['일강수량(mm)'].isnull(), '일강수량(mm)'] = 0
asos_incheon.loc[asos_incheon['일강수량(mm)'].isnull(), '일강수량(mm)'] = 0

asos_ulsan.isnull().sum()

asos_incheon.isnull().sum()

plt.plot(asos_incheon['일시'], asos_incheon['평균기온(°C)'])

plt.show()

plt.plot(asos_ulsan['일시'], asos_ulsan['평균기온(°C)'])

plt.show()

plt.plot(asos_incheon['일시'], asos_incheon['평균기온(°C)'])
plt.plot(asos_ulsan['일시'], asos_ulsan['평균기온(°C)'])

plt.show()

diff_temp = asos_incheon['평균기온(°C)'] - asos_ulsan['평균기온(°C)']

diff_temp

print(asos_incheon.index)
print(asos_ulsan.index)

asos_incheon.set_index('일시', inplace=True)
asos_ulsan.set_index('일시', inplace=True)

diff_temp = asos_incheon['평균기온(°C)'] - asos_ulsan['평균기온(°C)']

diff_temp

plt.plot(diff_temp.index, diff_temp)
if plt.get_fignums():
    plt.show()

abs_diff_temp = abs(diff_temp)

most_diff_temp = abs_diff_temp[abs_diff_temp == abs_diff_temp.max()]

most_diff_temp_date = most_diff_temp.index[0]

most_diff_temp_date

precipitation_diff = asos_incheon["일강수량(mm)"] - asos_ulsan["일강수량(mm)"]
most_diff_precipitation_date = precipitation_diff.abs().idxmax()

incheon_temp_slp_corr = asos_incheon['평균기온(°C)'].corr(asos_incheon['평균 해면기압(hPa)'])
print(incheon_temp_slp_corr)

ulsan_temp_slp_corr = asos_ulsan['평균기온(°C)'].corr(asos_ulsan['평균 해면기압(hPa)'])
print(ulsan_temp_slp_corr)

plt.plot(asos_incheon['평균기온(°C)'])
plt.plot(asos_incheon['평균 해면기압(hPa)'])

plt.show()

plt.scatter(asos_incheon['평균기온(°C)'], asos_incheon['평균 해면기압(hPa)'])

plt.show()

q2_corr = asos_incheon["일강수량(mm)"].corr(asos_incheon["평균 해면기압(hPa)"])

plt.scatter(asos_incheon["일강수량(mm)"], asos_incheon["평균 해면기압(hPa)"])
plt.xlabel("일강수량(mm)")
plt.ylabel("평균 해면기압(hPa)")
plt.show()

amos_all = pd.read_csv("dataset/amos_rawdata.csv")
amos_all['일시'] = pd.to_datetime(amos_all['일시'])

amos_all

amos_all.rename(columns={'지점명':'지점'}, inplace=True)

amos_ulsan = amos_all[amos_all['지점'] == '울산공항']
amos_incheon = amos_all[amos_all['지점'] == '인천공항']

amos_ulsan.set_index('일시', inplace=True)
amos_incheon.set_index('일시', inplace=True)

plt.plot(amos_ulsan['최고기온(°C)'])
plt.plot(amos_incheon['최고기온(°C)'])

plt.show()

plt.plot(amos_ulsan['최저기온(°C)'])
plt.plot(amos_incheon['최저기온(°C)'])

plt.show()

plt.plot(amos_ulsan['최고기온(°C)'])
plt.plot(asos_ulsan['최고기온(°C)'])
plt.legend(['AMOS', 'ASOS'])
plt.show()

ulsan_amos_asos_temp_diff = amos_ulsan['최고기온(°C)'] - asos_ulsan['최고기온(°C)']
plt.plot(ulsan_amos_asos_temp_diff)
plt.show()

plt.plot(amos_incheon['최고기온(°C)'])
plt.plot(asos_incheon['최고기온(°C)'])
plt.legend(['AMOS', 'ASOS'])
plt.show()

incheon_amos_asos_temp_diff = amos_incheon['최고기온(°C)'] - asos_incheon['최고기온(°C)']
plt.plot(incheon_amos_asos_temp_diff)
plt.show()

q3_higher_temp_count = int(incheon_amos_asos_temp_diff.ge(0).sum())

ans = {
    "퀴즈1": str(most_diff_precipitation_date),
    "퀴즈2": float(q2_corr),
    "퀴즈3": int(q3_higher_temp_count)
}

print(ans)
