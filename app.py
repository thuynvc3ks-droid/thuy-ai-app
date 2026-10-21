import streamlit as st
import google.generativeai as genai
import os

st.title("Trợ lý AI của Thầy Thủy")
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("Lỗi: Chưa tìm thấy API Key trong mục Secrets.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    user_input = st.text_input("Nhập câu hỏi của bạn:")
    
    if st.button("Gửi"):
        if user_input:
            try:
                response = model.generate_content(user_input)
                st.write(response.text)
            except Exception as e:
                st.error(f"Lỗi hệ thống: {e}")
        else:
            st.warning("Vui lòng nhập câu hỏi.")
