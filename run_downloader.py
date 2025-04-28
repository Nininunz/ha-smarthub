import subprocess
import logging
import time
import argparse
import random
from datetime import datetime, timedelta
import paho.mqtt.publish as publish

# === Schedule & Retry Configuration ===
START_HOUR = 8
START_MINUTE = 0
CUTOFF_HOUR = 20
ALERT_HOUR = 12

RETRY_ATTEMPTS = 5
INITIAL_BACKOFF_SECONDS = 5
MAX_BACKOFF_SECONDS = 300  # Max 5 minutes
JITTER_PERCENT = 0.1       # ±10% jitter
CYCLE_DELAY_MINUTES = 15

# === MQTT Configuration ===
MQTT_BROKER = "CHANGE_ME" 
MQTT_PORT = 1883 
MQTT_USERNAME = "CHANGE_ME" 
MQTT_PASSWORD = "CHANGE_ME"
MQTT_TOPIC = "downloader/status"
MQTT_SUCCESS_MESSAGE = "success"
MQTT_FAIL_MESSAGE = "fail"

# === Logging Setup ===
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("downloader.log"),
        logging.StreamHandler()
    ]
)

def send_mqtt_message(payload):
    try:
        publish.single(
            topic=MQTT_TOPIC,
            payload=payload,
            hostname=MQTT_BROKER,
            port=MQTT_PORT,
            auth={"username": MQTT_USERNAME, "password": MQTT_PASSWORD}
        )
        logging.info(f"MQTT message sent: {MQTT_TOPIC} = {payload}")
    except Exception as e:
        logging.error(f"Failed to send MQTT message: {e}")

def run_once():
    binary_path = "./electric-usage-downloader"
    config_path = "./config.yaml"
    args = [binary_path, "--config", config_path, "--debug"]

    logging.debug(f"Running command: {' '.join(args)}")
    found_success = False

    try:
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line, end='')
            logging.debug(line.strip())
            if "Writing data to database..." in line:
                found_success = True

        process.wait()

    except FileNotFoundError:
        logging.critical(f"Binary not found: {binary_path}")
    except Exception as e:
        logging.exception("Unexpected error occurred")

    return found_success

def run_with_retries_until_cutoff():
    while True:
        now = datetime.now()

        if now.hour >= CUTOFF_HOUR:
            logging.warning(f"Reached {CUTOFF_HOUR:02d}:00 cutoff. Will retry tomorrow at {START_HOUR:02d}:{START_MINUTE:02d}.")
            break

        backoff = INITIAL_BACKOFF_SECONDS

        for attempt in range(1, RETRY_ATTEMPTS + 1):
            logging.info(f"Attempt #{attempt}")
            if run_once():
                logging.info("Run successful")
                send_mqtt_message(MQTT_SUCCESS_MESSAGE)
                return
            else:
                logging.warning("Run failed")

                if attempt < RETRY_ATTEMPTS:
                    jitter = backoff * JITTER_PERCENT
                    delay = min(backoff + random.uniform(-jitter, jitter), MAX_BACKOFF_SECONDS)
                    logging.info(f"Retrying in {int(delay)} seconds (exponential backoff with jitter)...")
                    time.sleep(delay)
                    backoff = min(backoff * 2, MAX_BACKOFF_SECONDS)

        logging.warning(f"All {RETRY_ATTEMPTS} attempts failed. Waiting {CYCLE_DELAY_MINUTES} minutes before next cycle...")
        if now.hour >= ALERT_HOUR:
            send_mqtt_message(MQTT_FAIL_MESSAGE)

        time.sleep(CYCLE_DELAY_MINUTES * 60)

def wait_until_start_time():
    now = datetime.now()
    target = now.replace(hour=START_HOUR, minute=START_MINUTE, second=0, microsecond=0)
    if now >= target:
        target += timedelta(days=1)
    wait_seconds = (target - now).total_seconds()
    logging.info(f"Waiting until {START_HOUR:02d}:{START_MINUTE:02d}... sleeping for {int(wait_seconds)} seconds")
    time.sleep(wait_seconds)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--now", action="store_true", help="Run once immediately with retry logic")
    args = parser.parse_args()

    if args.now:
        run_with_retries_until_cutoff()
    else:
        while True:
            wait_until_start_time()
            run_with_retries_until_cutoff()
