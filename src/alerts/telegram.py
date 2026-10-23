import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send_telegram_alert(message):
    payload = {
        "chat_id": CHAT_ID,
        "text": f"⚠️ MONITOR ALERT: {message}",
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status() #if the response code is 4xx or 5xx

        logging.info("Alert sent successfully via Telegram")
        return True 

    except requests.exceptions.Timeout:
        logging.error("Telegram alert failed: The request timed out.")
    except requests.exceptions.ConnectionError:
        logging.error("Telegram alert failed: Network connection or DNS issue.")
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"Telegram API returned an error status: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"A general Requests error occurred: {req_err}")
    except Exception as gen_err:
        logging.error(f"A non-network bug occurred in the script: {gen_err}")

    return False
