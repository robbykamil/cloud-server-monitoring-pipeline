import time
import logging

from rules.threshold import CPU_Warning, CPU_Critical, RAM_Warning, DISK_Warning, DISK_Critical
from collectors.cpu import get_cpu_usage
from collectors.disk import get_disk_usage
from collectors.memory import get_memory_usage
from alerts.telegram import send_telegram_alert

# Configure logging to make terminal output structured and readable
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Dictionary storing collector function references
system_status = {
    "CPU": get_cpu_usage,
    "RAM": get_memory_usage,
    "DISK": get_disk_usage
}

validation = {
    "CPU": {"Critical": CPU_Critical, "Warning": CPU_Warning},
    "RAM": {"Warning": RAM_Warning},
    "DISK": {"Critical": DISK_Critical, "Warning": DISK_Warning}
}

def main():
    logging.info("Cloud server monitoring started...")
    try:
        while True:
            for category, func in system_status.items():
                if category in validation:
                    # FIX: Call the collector function to get the actual numeric value
                    current_value = func()
                    threshold = validation[category]
                    
                    if "Critical" in threshold and current_value >= threshold["Critical"]:
                        alert_msg = f"🚨 CRITICAL ALERT: {category} usage is at {current_value}% (Threshold: {threshold['Critical']}%)"
                        logging.warning(alert_msg)
                        send_telegram_alert(alert_msg)

                    elif "Warning" in threshold and current_value >= threshold["Warning"]:
                        alert_msg = f"⚠️ WARNING ALERT: {category} usage is at {current_value}% (Threshold: {threshold['Warning']}%)"
                        logging.warning(alert_msg)
                        send_telegram_alert(alert_msg)

                    else:
                        logging.info(f"OK: {category} usage is at {current_value}%")

            # FIX: Time delay between checks (e.g., every 60 seconds)
            time.sleep(60)

    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")

if __name__ == "__main__":
    main()
