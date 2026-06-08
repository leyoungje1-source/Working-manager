import streamlit as st
import json
from pathlib import Path
import pandas as pd

st.title("📊 통계")

DATA_FILE = Path("data/tasks.json")

if not DATA_FILE.exists():
    DATA_FILE.write_text("[]", encoding="utf-8")

tasks = json.loads(DATA_FILE.read_text(encoding="utf-8"))

if not tasks:
    st.warning("데이터가 없습니다.")
else:
    df = pd.DataFrame(tasks)

    st.subheader("과목별 수행 개수")
    st.bar_chart(df["subject"].value_counts())

    st.subheader("전체 데이터")
    st.dataframe(df)
