import streamlit as st
import google.generativeai as genai
import os

# 1. Lấy API Key ẩn danh từ Biến môi trường
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Khởi tạo mô hình
model = genai.GenerativeModel('gemini-1.5-flash') # Hoặc mô hình thầy đã dùng

# 2. Tạo giao diện Web
st.title("Trợ lý AI của Thầy Thủy")
user_input = st.text_input("Nhập câu hỏi của bạn:")

if st.button("Gửi"):
    if user_input:
        response = model.generate_content(user_input)
        st.write(response.text)
    else:
        st.warning("Vui lòng nhập câu hỏi.")
