import os
from dotenv import load_dotenv
from litellm import completion

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not API_KEY:
    raise ValueError("❌ DEEPSEEK_API_KEY not found in environment")

API_BASE = "https://api.deepseek.com/v1"
MODEL = "deepseek/deepseek-coder"

def classify_email(email_text: str) -> str:
    system_prompt = (
        "You are an AI compliance assistant. "
        "Classify the following email into one or more of these categories: "
        "Secrecy, Market Manipulation / Misconduct, Market Bribery, "
        "Change in Communication, Complaints, Employee Ethics, or General. "
        "Also assign a priority score from 1 (Low) to 5 (Critical) based on risk. "
        "Respond ONLY in JSON format like: "
        '{"category": "...", "reason": "...", "source_text": "...", "priority": ...}'
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Email content:\n\n{email_text}"}
    ]

    try:
        response = completion(
            model=MODEL,
            messages=messages,
            api_key=API_KEY,
            base_url=API_BASE
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f'{{"error": "Failed to call DeepSeek: {str(e)}"}}'
