import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send_telegram_alert(message):
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

    if not TOKEN or not CHAT_ID:
        logging.error("Telegram bot token or chat ID is not set. Please check your environment variables.")
        return False

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
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
        status_code = http_err.response.status_code if http_err.response is not None else "unknown"
        error_details = http_err.response.text if http_err.response is not None else "No response body available"
        logging.error(f"Telegram API returned an error status: {status_code} | Details: {error_details}")
    except requests.exceptions.RequestException as req_err:
        safe_err_msg = str(req_err).replace(TOKEN, "[REDACTED_TOKEN]")
        logging.error(f"A general Requests error occurred: {safe_err_msg}")
    except Exception as gen_err:
        logging.error(f"A non-network bug occurred in the script: {gen_err}")

    return False
