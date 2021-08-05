import time
from datetime import datetime
from typing import Callable

import global_common
import pytz
import schedule

from jobs import monitor_vix, common


def run_in_a_new_thread(job: Callable):
    global_common.run_as_separate_thread(job, None)


def get_local_time(time: str) -> str:
    hour: int = int(time.split(":")[0])
    minute: int = int(time.split(":")[1])
    second: int = int(time.split(":")[2])
    return pytz.timezone("America/New_York").localize(datetime.now().replace(hour=hour, minute=minute, second=second)).astimezone().strftime("%H:%M:%S")


if __name__ == "__main__":
    common.log("IBKR Jobs Started")
    schedule.every().day.at(get_local_time("04:57:00")).do(monitor_vix.do)
    print(get_local_time("04:57:00"))

    while True:
        schedule.run_pending()
        time.sleep(1)
