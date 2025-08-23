from dotenv import load_dotenv
import os
import time

from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# System message
sysMessage = """
You are a Native Pashto Speaker who converts Roman Pashto into proper Pashto text.
You will be given a Roman Pashto text and you will have to convert it into proper Pashto text.
"""

def _safe_extract_text(response):
    """
    Extract text from Gemini response robustly.
    """
    if hasattr(response, "text") and isinstance(response.text, str) and response.text.strip():
        return response.text.strip()
    return str(response)

def roman_to_pashto(text, max_retries=3, delay=2):
    """
    Convert Roman Pashto text to Proper Pashto using Gemini 2.0-flash.
    """
    prompt = f"""
    Convert the following Roman Pashto text to Proper Pashto.
    ONLY return the converted text. Do NOT provide explanations or additional information.

    Roman Pashto: {text}
    Proper Pashto:
    """.strip()

    prompt_full = sysMessage.strip() + "\n\n" + prompt

    for _ in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt_full
            )
            return _safe_extract_text(response)
        except Exception as e:
            print(f"Error: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= 2

    return "⚠️ Error: Service unavailable. Try again later."