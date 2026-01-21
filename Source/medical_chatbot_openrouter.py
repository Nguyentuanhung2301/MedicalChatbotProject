from dotenv import load_dotenv
import os
import requests

load_dotenv()

# Lấy API key từ biến môi trường
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise RuntimeError("❌ Chưa thiết lập biến môi trường OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = (
    "Bạn là chatbot hỗ trợ thông tin y tế cơ bản. "
    "KHÔNG chẩn đoán bệnh. "
    "KHÔNG kê đơn thuốc. "
    "Không thay thế bác sĩ. "
    "Luôn khuyên người dùng đi khám nếu triệu chứng nghiêm trọng."
)

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}


def ask_openrouter(question: str) -> str:
    """
    Gửi câu hỏi tới OpenRouter và trả về câu trả lời
    """
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]
    }

    try:
        response = requests.post(
            API_URL,
            headers=HEADERS,
            json=payload,
            timeout=30
        )
    except Exception as e:
        return f"❌ Lỗi kết nối OpenRouter: {e}"

    if response.status_code != 200:
        return f"❌ OpenRouter error: {response.text}"

    data = response.json()
    return data["choices"][0]["message"]["content"]
