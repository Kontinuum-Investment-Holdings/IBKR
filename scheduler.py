import time

import communication.telegram
import schedule

import constants
from jobs import update_code_base

if __name__ == "__main__":
    communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, "IBKR Scheduler started", False)
    time.sleep(60)

    schedule.every(60).seconds.do(update_code_base.do)

    while True:
        schedule.run_pending()
        time.sleep(1)
