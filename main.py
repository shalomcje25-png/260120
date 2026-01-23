import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="퍼스널 컬러 & 날씨 코디 추천",
    page_icon="🎨",
    layout="centered"
)

# 2. 앱 제목 및 설명
st.title("🎨 퍼스널 컬러 & 내일의 코디")
st.markdown("""
간단한 진단을 통해 **퍼스널 컬러**를 확인하고, 
내일의 **기온에 딱 맞는 의상**을 추천받으세요!
""")

st.divider()

# 3. 퍼스널 컬러 진단 섹션
st.header("1. 퍼스널 컬러 자가 진단")

col1, col2 = st.columns(2)

with col1:
    q1 = st.radio("피부톤이 대체로 어떤가요?", ("노란기/따뜻함", "붉은기/차가움"))
    q2 = st.radio("잘 어울리는 액세서리는?", ("골드(Gold)", "실버(Silver)"))

with col2:
    q3 = st.radio("햇볕에 타면 피부가?", ("검게 탄다", "빨갛게 익는다"))
    q4 = st.radio("본인의 전반적인 이미지는?", ("밝고 생기있음", "차분하고 깊이있음", "맑고 깨끗함", "강렬하고 선명함"))

# 진단 로직 함수
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

if st.button("내 퍼스널 컬러 확인하기"):
    st.balloons()
    st.subheader(f"당신의 타입은: :orange[{my_color}] 입니다! 🎉")

st.divider()

# 4. 날씨 및 의상 추천 섹션
st.header("2. 내일의 코디 추천")

# 기온 입력 (슬라이더)
temp = st.slider("내일의 예상 낮 기온을 설정하세요 (°C)", -10.0, 35.0, 15.0)

# 데이터 정의 (에러 수정 완료된 딕셔너리)
color_palettes = {
    "봄 웜톤": {"colors": "복숭아색, 코랄, 옐로우 그린", "hex": ["#ffcba4", "#ff7f50", "#9acd32"]},
    "여름 쿨톤": {"colors": "라벤더, 스카이 블루, 파스텔 핑크", "hex": ["#e6e6fa", "#87ceeb", "#ffb6c1"]},
    "가을 웜톤": {"colors": "머스타드, 테라코타, 카키", "hex": ["#ffdb58", "#e2725b", "#f0e68c"]},
    "겨울 쿨톤": {"colors": "로열 블루, 버건디, 선명한 화이트", "hex": ["#4169e1", "#800020", "#ffffff"]}
}

def get_clothes(temp):
    if temp >= 28: return "👕 민소매, 반바지, 린넨 소재 옷"
    elif 23 <= temp: return "👕 반팔, 얇은 셔츠, 면바지"
    elif 17 <= temp: return "🧥 긴팔 티셔츠, 얇은 가디건, 슬랙스"
    elif 12 <= temp: return "🧥 자켓, 셔츠, 가디건, 청바지"
    elif 6 <= temp: return "🧥 코트, 가죽 자켓, 니트, 기모바지"
    else: return "❄️ 패딩, 두꺼운 코트, 목도리, 기모 제품"

# 결과 데이터 매칭
palette = color_palettes[my_color]
clothes = get_clothes(temp)

st.info(f"💡 **{my_color}**에게 추천하는 코디와 색상입니다.")

res_col1, res_col2 = st.columns(2)

with res_col1:
    st.metric("설정 기온", f"{temp} °C")
    st.write(f"**추천 의상:** \n{clothes}")

with res_col2:
    st.write("**추천 컬러 팔레트:**")
    # 컬러 칩 시각화
    color_cols = st.columns(3)
    for i, hex_code in enumerate(palette["hex"]):
        color_cols[i].markdown(
            f'<div style="background-color:{hex_code}; width:100%; height:50px; border-radius:5px; border:1px solid #ddd;"></div>', 
            unsafe_allow_html=True
        )
    st.caption(palette["colors"])

st.success(f"**스타일링 팁:** {palette['colors'].split(',')[0]} 계열의 상의와 {clothes.split()[-1]}를 매치해보세요!")
