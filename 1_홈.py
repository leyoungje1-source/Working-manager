import streamlit as st
import json
from pathlib import Path
from datetime import date, datetime

st.title("🏠 홈")

DATA_FILE = Path("data/tasks.json")

if not DATA_FILE.exists():
    DATA_FILE.write_text("[]", encoding="utf-8")

tasks = json.loads(DATA_FILE.read_text(encoding="utf-8"))

if not tasks:
    st.warning("등록된 수행평가가 없습니다.")
else:
    for idx, task in enumerate(tasks):
        deadline = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
        remaining_days = (deadline - date.today()).days

        available_time = max(remaining_days, 1) * task["daily_hours"]

        if task["expected_hours"] > available_time:
            risk = "🔴 높음"
        elif task["expected_hours"] > available_time * 0.7:
            risk = "🟡 보통"
        else:
            risk = "🟢 낮음"

        st.markdown("---")
        st.subheader(task["task_name"])
        st.write(f"과목: {task['subject']}")
        st.write(f"D-{remaining_days}")
        st.write(f"위험도: {risk}")
        st.progress(task["progress"] / 100)
