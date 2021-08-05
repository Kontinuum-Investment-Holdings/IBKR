import time

import communication.telegram
import schedule

import constants
from jobs import monitor_vix

if __name__ == "__main__":
    time.sleep(60)

    schedule.every(10).seconds.do(monitor_vix.do)

    while True:
        communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, "IBKR Scheduler started", False)
        schedule.run_pending()
        time.sleep(1)
