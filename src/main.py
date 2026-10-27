import time
import logging

from rules.threshold import CPU_WARNING, CPU_CRITICAL, RAM_WARNING, DISK_WARNING, DISK_CRITICAL
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
    "CPU": {"Critical": CPU_CRITICAL, "Warning": CPU_WARNING},
    "RAM": {"Warning": RAM_WARNING},
    "DISK": {"Critical": DISK_CRITICAL, "Warning": DISK_WARNING}
}

def main():
    logging.info("Cloud server monitoring started...")
    try:
        if "CPU" in system_status:
            system_status["CPU"]()
    except Exception as e:
        logging.error(f"An error occurred while checking CPU usage: {e}")
    time.sleep(0.5)

    try:
        while True:
            for category, func in system_status.items():
                if category in validation:
                    try:
                        current_value = func()
                        threshold = validation[category]
                    
                        if "Critical" in threshold and current_value >= threshold["Critical"]:
                            alert_msg = f"🚨 CRITICAL ALERT: {category} usage is at {current_value}% (Threshold: {threshold['Critical']}%)"
                            logging.critical(alert_msg)
                            send_telegram_alert(alert_msg)

                        elif "Warning" in threshold and current_value >= threshold["Warning"]:
                            alert_msg = f"⚠️ WARNING ALERT: {category} usage is at {current_value}% (Threshold: {threshold['Warning']}%)"
                            logging.warning(alert_msg)
                            send_telegram_alert(alert_msg)

                        else:
                            logging.info(f"OK: {category} usage is at {current_value}%")

                    except Exception as e:
                        logging.error(f"An eror occurred while checking {category} usage: {e}")
                        continue

            # Time delay between checks (e.g., every 60 seconds)
            time.sleep(60)

    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")

if __name__ == "__main__":
    main()
