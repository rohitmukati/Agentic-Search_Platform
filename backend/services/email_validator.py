import os
import requests
from dotenv import load_dotenv

load_dotenv()

def validate_email(email: str) -> str:
    if not email:
        return "Unknown"

    api_key = os.getenv("MAILBOXLAYER_KEY")
    url = f"http://apilayer.net/api/check?access_key={api_key}&email={email}&smtp=1&format=1"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("smtp_check") and data.get("format_valid"):
            return "Valid"
        elif data.get("format_valid"):
            return "Invalid"
        else:
            return "Unknown"
    except Exception as e:
        print(f"Email validation failed: {e}")
        return "Unknown"
