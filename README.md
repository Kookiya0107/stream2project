# 상관분석 대시보드 (Correlation Analysis Dashboard)

CSV 파일을 업로드하면 숫자형 변수 간의 상관관계를 표와 히트맵으로 시각화해주는 Streamlit 기반 웹 애플리케이션입니다.

## 주요 기능

- CSV 파일 업로드
- 데이터 미리보기 및 기술통계 확인 (`head()`, `describe()`)
- 상관분석에 포함할 변수를 직접 선택
- 선택한 변수 간 상관계수 표 확인
- Seaborn 히트맵으로 상관관계 시각화

## 사용 기술

- Python
- Streamlit
- pandas
- matplotlib
- seaborn

## 실행 방법

```bash
pip install -r requirements.txt
streamlit run streamtest2.py
```

## 사용 방법

1. 앱 실행 후 CSV 파일을 업로드합니다.
2. 데이터 미리보기와 기술통계를 확인합니다.
3. 상관분석에 포함할 숫자형 변수를 선택합니다.
4. 변수를 2개 이상 선택하면 상관계수 표와 히트맵이 표시됩니다.

## 향후 개선 계획

- 결측치 처리 옵션 추가
- 다양한 통계 그래프(산점도, 박스플롯 등) 추가
- 배포 링크 연결 (Streamlit Community Cloud)