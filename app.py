import streamlit as st

st.title("🫁 기도 오가노이드 기반 천식 AI 분석 시스템")

il4 = st.number_input("IL4", 0.0, 10.0, 5.0)
il13 = st.number_input("IL13", 0.0, 10.0, 5.0)
il5 = st.number_input("IL5", 0.0, 10.0, 5.0)
postn = st.number_input("POSTN", 0.0, 10.0, 5.0)
muc5ac = st.number_input("MUC5AC", 0.0, 10.0, 5.0)
adrb2 = st.number_input("ADRB2", 0.0, 10.0, 5.0)

ass = 0.25*il13 + 0.25*il5 + 0.2*postn + 0.15*il4 + 0.15*muc5ac

if ass < 6:
    severity = "경증"
elif ass < 8:
    severity = "중등증"
else:
    severity = "중증"

st.subheader("결과")
st.write("중증도:", severity)
