import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 🔐 API 키 로딩
load_dotenv()
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


# 모델 준비
model = genai.GenerativeModel("gemini-2.0-flash-exp")

st.title("🧠 심리상담 AI 센터")

with st.form(key="form1"):
    name = st.text_input("이름 또는 닉네임")
    feeling = st.selectbox("요즘 기분은 어떤가요?", ["기쁨", "슬픔", "화남", "불안", "무기력", "복합적"])
    reason = st.text_area("그 감정을 느끼는 이유는?")
    advice = st.text_area("AI에게 조언받고 싶은 내용이 있다면?")
    submit = st.form_submit_button("AI에게 조언 받기")

if submit:
    with st.spinner("AI가 생각을 정리하는 중입니다..."):
        prompt = f"""
이름: {name}
기분: {feeling}
이유: {reason}
상담 요청: {advice}

위 학생에게 따뜻하고 공감되는 심리 상담 조언을 해주세요.
학생 눈높이에 맞는 말투로 친절하게 작성해주세요.
        """
        try:
            response = model.generate_content(prompt)
            st.success("💬 AI의 조언:")
            st.markdown(f"> {response.text}")
        except Exception as e:
            st.error(f"❌ Gemini 호출 오류: {e}")
