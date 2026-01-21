import streamlit as st

from Source.medical_chatbot_openrouter import ask_openrouter
from Source.meidcal_chatbot_gemini import ask_gemini

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Medical Chatbot",
    page_icon="🩺",
    layout="wide"
)

# =========================
# TIÊU ĐỀ
# =========================
st.markdown(
    """
    <h1 style="text-align:center;">🩺 Medical Chatbot</h1>
    <p style="text-align:center; color:gray;">
    Chatbot hỗ trợ kiến thức y tế cơ bản – Không thay thế bác sĩ
    </p>
    """,
    unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.header("⚙️ Cấu hình")

    model_choice = st.radio(
        "Chọn mô hình AI",
        [
            "OpenRouter",
            "Google Gemini",
            "So sánh OpenRouter & Gemini"
        ]
    )

    st.markdown("---")

    st.markdown(
        """
        ⚠️ **Lưu ý y tế**  
        - Chatbot **KHÔNG chẩn đoán bệnh**  
        - Chỉ cung cấp thông tin tham khảo  
        - Luôn hỏi ý kiến bác sĩ khi cần
        """
    )

# =========================
# INPUT NGƯỜI DÙNG
# =========================
user_question = st.text_area(
    "💬 Nhập câu hỏi y tế của bạn:",
    height=120,
    placeholder="Ví dụ: Đau đầu thường xuyên có nguy hiểm không?"
)

ask_button = st.button("🚀 Gửi câu hỏi")

# =========================
# XỬ LÝ HỎI – ĐÁP
# =========================
if ask_button:
    if not user_question.strip():
        st.warning("⚠️ Vui lòng nhập câu hỏi.")
    else:
        with st.spinner("🤖 Đang phân tích câu hỏi..."):

            try:
                # =========================
                # CHỈ OPENROUTER
                # =========================
                if model_choice == "OpenRouter":
                    answer = ask_openrouter(user_question)

                    st.markdown("### 🤖 OpenRouter trả lời")
                    st.write(answer)

                # =========================
                # CHỈ GEMINI
                # =========================
                elif model_choice == "Google Gemini":
                    answer = ask_gemini(user_question)

                    st.markdown("### 🌟 Google Gemini trả lời")
                    st.write(answer)

                # =========================
                # SO SÁNH 2 AI
                # =========================
                else:
                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("### 🤖 OpenRouter")
                        answer_or = ask_openrouter(user_question)
                        st.write(answer_or)

                    with col2:
                        st.markdown("### 🌟 Google Gemini")
                        answer_gm = ask_gemini(user_question)
                        st.write(answer_gm)

            except Exception as e:
                st.error(f"❌ Lỗi: {str(e)}")

# =========================
# FOOTER
# =========================
st.markdown(
    """
    <hr>
    <p style="text-align:center; color:gray; font-size:14px;">
    Medical Chatbot Project from Nguyen Tuan Hung
    </p>
    """,
    unsafe_allow_html=True
)
