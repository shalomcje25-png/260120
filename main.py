import streamlit as st
from PIL import Image

# 1. 페이지 설정 (탭 타이틀 및 아이콘)
st.set_page_config(page_title="나의 자기소개 페이지", page_icon="👋")

# 2. 사이드바 구성 (선택 사항)
st.sidebar.title("연락처")
st.sidebar.info("📧 이메일: email@example.com")
st.sidebar.info("🔗 [GitHub](https://github.com)")

# 3. 메인 화면 구성
def main():
    st.title("안녕하세요! 저를 소개합니다 ✨")
    
    # 컬럼 레이아웃 사용 (왼쪽: 사진, 오른쪽: 인사말)
    col1, col2 = st.columns([1, 2])

    with col1:
        # 본인의 사진 파일 경로를 적어주세요 (예: 'profile.jpg')
        # 파일이 없다면 샘플 이미지를 불러옵니다.
        st.image("https://via.placeholder.com/300", caption="나의 프로필 사진", use_container_width=True)

    with col2:
        st.subheader("인사말")
        st.write("""
        안녕하세요! 새로운 도전을 즐기는 **[홍길동]**입니다.
        
        현재 저는 Streamlit을 활용해 데이터를 시각화하거나, 
        간단한 웹 어플리케이션을 만드는 작업에 관심을 가지고 있습니다.
        
        **관심 분야:**
        * 🐍 Python 프로그래밍
        * 📊 데이터 분석 및 시각화
        * 🤖 인공지능 모델링
        """)

    st.divider()

    # 추가 섹션 (경력이나 기술 스택)
    st.subheader("나의 기술 스택")
    st.progress(90, text="Python")
    st.progress(80, text="Streamlit")
    st.progress(70, text="SQL")

if __name__ == "__main__":
    main()
