import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Asthma AI", layout="centered")

# 🎨 Title
st.title("🫁 기도 오가노이드 기반 AI 천식 분석")
st.markdown("### 유전자 발현 데이터를 기반으로 중증도 및 치료제를 예측합니다")
st.markdown("---")

# 📥 입력
st.subheader("🧬 유전자 발현값 입력")

col1, col2 = st.columns(2)

with col1:
    il4 = st.slider("IL4", 0.0, 10.0, 5.0)
    il13 = st.slider("IL13", 0.0, 10.0, 5.0)
    il5 = st.slider("IL5", 0.0, 10.0, 5.0)

with col2:
    postn = st.slider("POSTN", 0.0, 10.0, 5.0)
    muc5ac = st.slider("MUC5AC", 0.0, 10.0, 5.0)
    adrb2 = st.slider("ADRB2", 0.0, 10.0, 5.0)

st.markdown("---")

# 🧠 점수 계산
ass = 0.25*il13 + 0.25*il5 + 0.2*postn + 0.15*il4 + 0.15*muc5ac

if ass < 6:
    severity = "🟢 경증"
elif ass < 8:
    severity = "🟡 중등증"
else:
    severity = "🔴 중증"

# 💊 치료제 추천
treatment = []

if il13 > 7 or il4 > 7:
    treatment.append("항 IgE 치료제 (오말리주맙)")
    treatment.append("흡입형 스테로이드")

if il5 > 7:
    treatment.append("항 IL-5 치료제 (메폴리주맙)")

if adrb2 < 5:
    treatment.append("β2 작용제 반응 저하 가능")

if not treatment:
    treatment.append("흡입형 스테로이드 / 기관지 확장제")

# 📊 결과 출력
st.subheader("📊 분석 결과")

st.metric("천식 중증도 점수 (ASS)", round(ass, 2))
st.write("### 판정:", severity)

st.subheader("💊 추천 치료제")
for t in treatment:
    st.write("✔️", t)

st.markdown("---")

# 📈 유전자 시각화
st.subheader("📊 유전자 발현 시각화")

genes = ["IL4", "IL13", "IL5", "POSTN", "MUC5AC", "ADRB2"]
values = [il4, il13, il5, postn, muc5ac, adrb2]

fig, ax = plt.subplots()
ax.bar(genes, values)

ax.set_ylabel("Expression Level")
ax.set_title("Gene Expression Profile (Simulated Oganloid Data)")

st.pyplot(fig)

st.markdown("---")

# 🧠 해석
st.subheader("🧠 해석 (연구 기반 설명)")

st.info(
    "이 모델은 기도 오가노이드에서 얻어지는 유전자 발현 패턴을 기반으로 설계되었으며, "
    "유전자 수준 정보와 실제 조직 반응을 연결하여 천식 중증도 및 치료 반응성을 예측하는데에 사용될 수 있다."
)

st.markdown("---")

st.caption("Developed for Bioinformatics & Organoid-based Precision Medicine Study")
