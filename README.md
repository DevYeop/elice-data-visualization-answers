# Python 데이터 시각화 실습 2~8 정답 코드

교육생이 실습 결과를 확인하고 직접 실행할 수 있도록 정답을 채운 Jupyter 노트북, Python 코드, Streamlit 앱과 실습 데이터를 모았습니다.

| 실습 | 내용 |
| --- | --- |
| [02. 데이터 시각화](02_data_visualization/) | Matplotlib·Seaborn 실습 6개와 서울시 아파트 시각화 미션 |
| [03. 대화형 시각화](03_interactive_visualization/) | Plotly 그래프 생성, 스타일 수정, 차트 유형, 추가 기능 |
| [04. 공공데이터 분석](04_public_data_analysis/) | 공항기상관측(AMOS), 종관기상관측(ASOS), 강수량·기온 비교 |
| [05. 데이터 분석 프로젝트](05_analysis_projects/) | 코로나19, 지하철, 자동차 리콜, 주유소 유가 분석 |
| [06. Streamlit 데이터 분석](06_streamlit_analysis/) | 테이블, 차트, 제주 지도와 북한 행정구역 지도 |
| [07. 공공데이터 웹 앱](07_public_data_web_apps/) | 서울시 미세먼지 전처리, 차트, 캐시, 지역별 지도 |
| [08. Streamlit CSV 차트](08_streamlit_csv_차트_실습/) | CSV 차트 4개와 비품 현황 편집 앱 |

## 실행 방법

저장소를 내려받고 최상위 폴더에서 Python 3.11 환경을 설치합니다. 아래 명령은 Windows PowerShell 기준입니다.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
```

- **Jupyter**는 `start_jupyter.bat`로 실행합니다. 실습 폴더에서 `.ipynb`를 열고 **Python 3** 커널로 위에서부터 실행하세요. 2~5장에는 같은 로직의 `.py`와 주석을 뺀 `_clean.py`도 있습니다. 지도와 표 등 셀의 출력은 노트북에서 확인할 수 있습니다.
- **Streamlit**은 원하는 앱의 `.py` 파일을 `start_streamlit.bat`에 끌어다 놓으면 실행됩니다. 터미널에서 실행할 때는 아래 명령을 사용하세요. 8장의 CSV 업로드와 편집 순서는 [8장 안내](08_streamlit_csv_차트_실습/README.md)에 있습니다.

```powershell
.\.venv\Scripts\python.exe -m streamlit run '08_streamlit_csv_차트_실습/01_품목별_막대그래프.py'
```

## 자료 출처

- 실습 구성과 원본 예제는 엘리스 Python 데이터 시각화 강의 자료를 바탕으로 합니다. 공개본에는 완성된 코드와 실습 설명을 담았습니다. 퀴즈 답은 노트북의 **정답 확인** 셀에서 볼 수 있습니다.
- 코로나19 실습은 일자·지역별 확진자 집계를 사용합니다. 제주 지도는 장소 이름과 좌표를 사용합니다.
- 미세먼지 데이터는 서울특별시 자료입니다. 7장은 2008~2022년 시간별 자료를 읽고 2014년 이후 데이터를 공용 입력인 `seoul.csv.gz`로 저장합니다. [서울시 시간별 (초)미세먼지 정보](https://data.seoul.go.kr/dataList/OA-22234/F/1/datasetView.do)
- 북한 행정구역은 World Food Programme과 OCHA ROAP의 경계 데이터를 바탕으로 한 geoBoundaries 자료입니다. CC BY 3.0 IGO 조건을 따릅니다. [geoBoundaries](https://www.geoboundaries.org/), [HDX 원본](https://data.humdata.org/dataset/dpr-korea-administrative-boundaries), [라이선스](https://creativecommons.org/licenses/by/3.0/igo/)
