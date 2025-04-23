import streamlit as st

# 가짜 사용자 정보 (실제에선 DB나 암호화된 값으로 대체 가능)
USERNAME = "admin"
PASSWORD = "1234"

# 로그인 상태 초기화
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login():
    st.title("🔐 로그인")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.authenticated = True
            st.success("로그인 성공!")
        else:
            st.error("아이디 또는 비밀번호가 틀렸습니다.")

def chatbot_app():
    st.title("💬 나만의 AI 챗봇")
    st.write("여기서 챗봇과 대화가 시작됩니다!")
    user_input = st.text_input("질문을 입력하세요")
    if user_input:
        st.write(f"🤖 답변: {user_input} 에 대한 답변입니다!")  # 실제론 OpenAI API 호출

# 로그인 화면 또는 챗봇 화면 보여주기
if not st.session_state.authenticated:
    login()
else:
    chatbot_app()