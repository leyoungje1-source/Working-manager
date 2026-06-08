import streamlit as st
import json
from pathlib import Path
from datetime import date

st.title("➕ 수행평가 추가")

DATA_FILE = Path("data/tasks.json")

if not DATA_FILE.exists():
    DATA_FILE.write_text("[]", encoding="utf-8")

subject = st.selectbox(
    "과목",
    ["국어", "수학", "영어", "과학", "사회", "기타"]
)

task_name = st.text_input("수행평가 이름")

deadline = st.date_input("마감일", min_value=date.today())

expected_hours = st.slider("예상 준비 시간", 1, 20, 5)
daily_hours = st.slider("하루 공부 가능 시간", 1, 10, 2)
progress = st.slider("진행률", 0, 100, 0)

if st.button("저장"):
    tasks = json.loads(DATA_FILE.read_text(encoding="utf-8"))

    tasks.append({
        "subject": subject,
        "task_name": task_name,
        "deadline": str(deadline),
        "expected_hours": expected_hours,
        "daily_hours": daily_hours,
        "progress": progress
    })

    DATA_FILE.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    st.success("저장되었습니다.")
