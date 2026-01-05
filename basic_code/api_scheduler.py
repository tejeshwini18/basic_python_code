import argparse
import time
from datetime import datetime, timedelta
import urllib.request
import logging
import threading
from collections import defaultdict

# Configuration
API_URL = "https://ifconfig.co"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Configure logging
logging.basicConfig(
    filename="api_scheduler.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Function to make the API call
def call_api():
    try:
        request = urllib.request.Request(API_URL, headers=HEADERS)
        with urllib.request.urlopen(request) as response:
            data = response.read().decode("utf-8").strip()
            logging.info(f"API Response: {data}")
            print(f"API Response: {data}")
    except Exception as e:
        logging.error(f"Error calling API: {e}")
        print(f"Error calling API: {e}")

# Function to schedule calls at the exact time
def schedule_calls(timestamps):
    """Schedule API calls based on timestamps."""
    now = datetime.now()
    calls_by_second = defaultdict(list)

    # Group timestamps by second
    for ts in timestamps:
        calls_by_second[ts].append(ts)

    for target_time, _ in sorted(calls_by_second.items()):
        target_time_obj = datetime.strptime(target_time, "%H:%M:%S").replace(
            year=now.year, month=now.month, day=now.day
        )
        sleep_time = (target_time_obj - datetime.now()).total_seconds()

        if sleep_time > 0:
            logging.info(f"Waiting {sleep_time} seconds for {target_time_obj}")
            time.sleep(sleep_time)

        threads = []
        for _ in calls_by_second[target_time]:
            thread = threading.Thread(target=call_api)
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

# Main function
def main():
    parser = argparse.ArgumentParser(
        description="Schedule API calls based on provided timestamps."
    )
    parser.add_argument(
        "--timestamps",
        type=str,
        required=True,
        help="Comma-separated list of timestamps in HH:MM:SS format (e.g., '09:15:25,11:58:23')."
    )
    args = parser.parse_args()

    # Parse timestamps and remove duplicates
    try:
        timestamps = list(set(args.timestamps.split(",")))
        timestamps.sort()  # Ensure timestamps are sorted
        logging.info(f"Scheduling API calls for timestamps: {timestamps}")
        schedule_calls(timestamps)
    except Exception as e:
        logging.error(f"Error parsing timestamps: {e}")
        print(f"Error parsing timestamps: {e}")

if __name__ == "__main__":
    main()
