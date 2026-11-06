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
# pd.read_csv를 통하여 종관기상관측(ASOS) 기상청 데이터를 데이터프레임 형태로 읽어옵니다.
asos_all = pd.read_csv("dataset/asos_rawdata.csv")

# %%
# 종관기상관측(ASOS) 상위 5개 데이터를 출력합니다.
asos_all.head()

# %%
asos_all["일시"] = pd.to_datetime(asos_all["일시"])

# 데이터프레임 정보를 요약하여 출력합니다.
asos_all.info()

# %%
unique_time_list = sorted(list(set(asos_all['일시']))) # 측정 일시 종류 확인
print(unique_time_list) # AMOS 측정 일시 데이터 확인
print(len(set(asos_all['일시']))) # 측정 일시 종류 확인

# %%
# asos_all DataFrame 지점명 데이터 확인
print(sorted(list(set(asos_all['지점명'])))) # ASOS 측정 지점명 데이터 확인
print(len(set(asos_all['지점명']))) # 측정 지점명 종류 확인

# %%
# asos_all DataFrame 통계수치 확인
asos_all.describe()

# %%
asos_ulsan = asos_all[asos_all['지점명'] == '울산'] # 울산 지점 데이터만 추출
asos_incheon = asos_all[asos_all['지점명'] == '인천'] # 인천 지점 데이터만 추출

# %%
asos_ulsan

# %%
print(asos_ulsan['지점명'].unique()) # 울산 지점명 데이터 확인
print(asos_incheon['지점명'].unique()) # 인천 지점명 데이터 확인

# %%
# 강수량의 결측치를 0으로 대체
# loc 함수를 이용하여 강수량의 결측치가 있는 데이터의 일강수량 수치를 0으로 대체
asos_ulsan.loc[asos_ulsan['일강수량(mm)'].isnull(), '일강수량(mm)'] = 0
asos_incheon.loc[asos_incheon['일강수량(mm)'].isnull(), '일강수량(mm)'] = 0

# %%
# 결측치 개수 확인
asos_ulsan.isnull().sum()

# %%
asos_incheon.isnull().sum()

# %%
plt.plot(asos_incheon['일시'], asos_incheon['평균기온(°C)'])

plt.show()

# %%
plt.plot(asos_ulsan['일시'], asos_ulsan['평균기온(°C)'])

plt.show()

# %%
# 두 데이터를 같이 그래프로 그리기
plt.plot(asos_incheon['일시'], asos_incheon['평균기온(°C)']) # 두 데이터를 모두 캔버스에 올립니다.
plt.plot(asos_ulsan['일시'], asos_ulsan['평균기온(°C)'])

plt.show() # 캔버스에 올라간 그림을 모두 보여줍니다.

# %%
# 두 데이터의 차이를 계산하기
diff_temp = asos_incheon['평균기온(°C)'] - asos_ulsan['평균기온(°C)']

# %%
diff_temp

# %%
print(asos_incheon.index)
print(asos_ulsan.index)

# %%
asos_incheon.set_index('일시', inplace=True) # 일시 칼럼의 값을 index로 사용한다는 의미입니다.
asos_ulsan.set_index('일시', inplace=True)

diff_temp = asos_incheon['평균기온(°C)'] - asos_ulsan['평균기온(°C)']

# %%
diff_temp

# %%
plt.plot(diff_temp.index, diff_temp)
if plt.get_fignums():
    plt.show()

# %%
abs_diff_temp = abs(diff_temp) # 기온 차이의 절댓값을 계산합니다.

most_diff_temp = abs_diff_temp[abs_diff_temp == abs_diff_temp.max()] # 기온 차이가 가장 큰 데이터를 찾습니다.

most_diff_temp_date = most_diff_temp.index[0] # 해당 데이터의 index (일시) 값을 찾습니다.

# %%
most_diff_temp_date

# %%
precipitation_diff = asos_incheon["일강수량(mm)"] - asos_ulsan["일강수량(mm)"]
most_diff_precipitation_date = precipitation_diff.abs().idxmax()

# %%
incheon_temp_slp_corr = asos_incheon['평균기온(°C)'].corr(asos_incheon['평균 해면기압(hPa)'])
print(incheon_temp_slp_corr)

# %%
ulsan_temp_slp_corr = asos_ulsan['평균기온(°C)'].corr(asos_ulsan['평균 해면기압(hPa)'])
print(ulsan_temp_slp_corr)

# %%
# 두 데이터를 같이 그래프로 그리기
plt.plot(asos_incheon['평균기온(°C)']) # 앞에서 '일시' 데이터를 index로 지정했으므로, '일시' 데이터를 x축으로 사용하지 않아도 됩니다.
plt.plot(asos_incheon['평균 해면기압(hPa)'])

plt.show() # 캔버스에 올라간 그림을 모두 보여줍니다.

# %%
# 산점도 그리기
plt.scatter(asos_incheon['평균기온(°C)'], asos_incheon['평균 해면기압(hPa)'])

plt.show()

# %%
q2_corr = asos_incheon["일강수량(mm)"].corr(asos_incheon["평균 해면기압(hPa)"])

# %%
plt.scatter(asos_incheon["일강수량(mm)"], asos_incheon["평균 해면기압(hPa)"])
plt.xlabel("일강수량(mm)")
plt.ylabel("평균 해면기압(hPa)")
plt.show()

# %%
# pd.read_csv를 통하여 항공기상관측(AMOS) 기상청 데이터를 데이터프레임 형태로 읽어옵니다.
amos_all = pd.read_csv("dataset/amos_rawdata.csv")
amos_all['일시'] = pd.to_datetime(amos_all['일시'])

amos_all

# %%
# AMOS 데이터의 칼럼명 중 '지점명' 을 '지점' 으로 변경
amos_all.rename(columns={'지점명':'지점'}, inplace=True)

# %%
amos_ulsan = amos_all[amos_all['지점'] == '울산공항']
amos_incheon = amos_all[amos_all['지점'] == '인천공항']

amos_ulsan.set_index('일시', inplace=True)
amos_incheon.set_index('일시', inplace=True)

# %%
plt.plot(amos_ulsan['최고기온(°C)']) # 원본 데이터에 평균
plt.plot(amos_incheon['최고기온(°C)'])

plt.show()

# %%
plt.plot(amos_ulsan['최저기온(°C)']) # 원본 데이터에 평균
plt.plot(amos_incheon['최저기온(°C)'])

plt.show()

# %%
plt.plot(amos_ulsan['최고기온(°C)'])
plt.plot(asos_ulsan['최고기온(°C)'])
plt.legend(['AMOS', 'ASOS'])
plt.show()

# %%
ulsan_amos_asos_temp_diff = amos_ulsan['최고기온(°C)'] - asos_ulsan['최고기온(°C)']
plt.plot(ulsan_amos_asos_temp_diff)
plt.show()

# %%
plt.plot(amos_incheon['최고기온(°C)'])
plt.plot(asos_incheon['최고기온(°C)'])
plt.legend(['AMOS', 'ASOS'])
plt.show()

# %%
incheon_amos_asos_temp_diff = amos_incheon['최고기온(°C)'] - asos_incheon['최고기온(°C)']
plt.plot(incheon_amos_asos_temp_diff)
plt.show()

# %%
q3_higher_temp_count = int(incheon_amos_asos_temp_diff.ge(0).sum())

# %%
ans = {
    "퀴즈1": str(most_diff_precipitation_date),
    "퀴즈2": float(q2_corr),
    "퀴즈3": int(q3_higher_temp_count)
}

print(ans)
