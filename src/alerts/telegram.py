import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram_alert(message):
    if not TOKEN or not CHAT_ID:
        return " Configuration Error: TOKEN or CHAT_ID is missing from .env"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}

    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print("[ERROR]")
    except Exception as e:
        print(f"[ERROR] {e}")

