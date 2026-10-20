import streamlit as st
import google.generativeai as genai
import os

# 1. Lấy API Key
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# 2. Khởi tạo mô hình chuẩn (phiên bản ổn định nhất hiện tại)
model = genai.GenerativeModel('gemini-pro')

# 3. Giao diện Web
st.title("Trợ lý AI của Thầy Thủy")
user_input = st.text_input("Nhập câu hỏi của bạn:")

if st.button("Gửi"):
    if user_input:
        try:
            response = model.generate_content(user_input)
            st.write(response.text)
        except Exception as e:
            st.error(f"Đã xảy ra lỗi: {e}")
    else:
        st.warning("Vui lòng nhập câu hỏi.")
