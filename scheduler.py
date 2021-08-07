import time
from datetime import datetime
from typing import Callable

import global_common
import pytz
import schedule

from jobs import monitor_vix, common, cancel_unfilled_orders, get_account_summary, buy_leveraged_stocks


def get_local_time(time: str) -> str:
    hour: int = int(time.split(":")[0])
    minute: int = int(time.split(":")[1])
    second: int = int(time.split(":")[2])
    return pytz.timezone("America/New_York").localize(datetime.now().replace(hour=hour, minute=minute, second=second)).astimezone().strftime("%H:%M:%S")


def run_every_week_day(job: Callable, time: str) -> None:
    schedule.every().monday.at(time).do(global_common.run_as_separate_thread(job))
    schedule.every().tuesday.at(time).do(global_common.run_as_separate_thread(job))
    schedule.every().wednesday.at(time).do(global_common.run_as_separate_thread(job))
    schedule.every().thursday.at(time).do(global_common.run_as_separate_thread(job))
    schedule.every().friday.at(time).do(global_common.run_as_separate_thread(job))


if __name__ == "__main__":
    common.log("IBKR Jobs Started")

    run_every_week_day(monitor_vix.do, get_local_time("09:30:00"))
    run_every_week_day(monitor_vix.do, get_local_time("16:00:00"))

    run_every_week_day(cancel_unfilled_orders.do, get_local_time("15:55:00"))

    run_every_week_day(get_account_summary.do, get_local_time("09:30:00"))
    run_every_week_day(get_account_summary.do, get_local_time("16:00:00"))

    run_every_week_day(buy_leveraged_stocks.do, get_local_time("15:00:00"))

    while True:
        schedule.run_pending()
        time.sleep(1)
