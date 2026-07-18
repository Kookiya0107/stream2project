import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("데이터 상관관계 분석 대시보드")

uploaded_file = st.file_uploader("CSV 업로드", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("데이터 미리보기")
    st.dataframe(df.head())
    st.dataframe(df.describe())

    # 숫자형 컬럼만 선택지로 제공
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    selected_columns = st.multiselect(
        "상관분석에 포함할 변수를 선택하세요",
        numeric_cols,
        default=numeric_cols
    )

    if len(selected_columns) >= 2:
        corr_df = df[selected_columns].corr()

        st.subheader("상관계수 표")
        st.dataframe(corr_df.style.background_gradient(cmap="Blues"))

        st.subheader("상관관계 히트맵")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr_df, annot=True, cmap="Blues", fmt=".2f", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("2개 이상의 변수를 선택하세요")
else:
    st.info("CSV 파일을 업로드해주세요")

