import streamlit as st

# 페이지 설정
st.set_page_config(page_title="퍼스널 컬러 & 데일리 코디", page_icon="✨")

# 1. 앱 제목 및 설명
st.title("🎨 퍼스널 컬러 & 내일의 코디 추천")
st.markdown("""
본인의 성향을 선택하여 **퍼스널 컬러**를 진단하고, 
내일의 **기온에 맞는 최적의 의상**을 추천받으세요!
""")

st.divider()

# 2. 퍼스널 컬러 진단 섹션
st.header("1. 퍼스널 컬러 자가 진단")

col1, col2 = st.columns(2)

with col1:
    q1 = st.radio("피부톤이 대체로 어떤가요?", ("노란기/따뜻함", "붉은기/차가움"))
    q2 = st.radio("잘 어울리는 액세서리는?", ("골드(Gold)", "실버(Silver)"))

with col2:
    q3 = st.radio("햇볕에 타면 피부가?", ("검게 탄다", "빨갛게 익는다"))
    q4 = st.radio("본인의 전반적인 이미지는?", ("밝고 생기있음", "차분하고 깊이있음", "맑고 깨끗함", "강렬하고 선명함"))

# 진단 로직
def diagnose(q1, q2, q3, q4):
    warm_score = 0
    if "노란기" in q1: warm_score += 1
    if "골드" in q2: warm_score += 1
    if "검게" in q3: warm_score += 1
    
    if warm_score >= 2:
        return "봄 웜톤" if q4 in ["밝고 생기있음", "맑고 깨끗함"] else "가을 웜톤"
    else:
        return "여름 쿨톤" if q4 in ["맑고 깨끗함", "밝고 생기있음"] else "겨울 쿨톤"

my_color = diagnose(q1, q2, q3, q4)

if st.button("내 컬러 확인하기"):
    st.balloons()
    st.subheader(f"당신의 타입은: :orange[{my_color}] 입니다! 🎉")

st.divider()

# 3. 날씨 및 의상 추천 섹션
st.header("2. 내일의 코디 추천")

# 기온 입력 (슬라이더)
temp = st.slider("내일의 예상 낮 기온을 설정하세요 (°C)", -10.0, 35.0, 15.0)

# 데이터 정의
color_palettes = {
    "봄 웜톤": {"colors": "복숭아색, 코랄, 옐로우 그린", "hex": ["#ffcba4", "#ff7f50", "#9acd32"]},
    "여름 쿨톤": {"colors": "라벤더, 스카이 블루, 파스텔 핑크", "hex": ["#e6e6fa", "#87ceeb", "#ffb6c1"]},
    "가을 웜톤": {"colors": "머스타드, 테라코타, 카키", "hex": ["#ffdb58", "#e2725b", "#f0e68c"]},
    "겨울 쿨톤": {"colors": "로열 블루, 버건디, 선명한 화이트", "hex": ["#4
