from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

# Lấy API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("❌ Chưa thiết lập biến môi trường GEMINI_API_KEY")

# Khởi tạo client Gemini
client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = (
    "Bạn là chatbot hỗ trợ thông tin y tế cơ bản. "
    "KHÔNG chẩn đoán bệnh. "
    "KHÔNG kê đơn thuốc. "
    "Không thay thế ý kiến bác sĩ. "
    "Luôn khuyên người dùng đi khám khi cần thiết."
)


def ask_gemini(question: str) -> str:
    """
    Gửi câu hỏi tới Google Gemini và trả về câu trả lời
    """
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=[
            SYSTEM_PROMPT,
            question
        ]
    )

    return response.text
