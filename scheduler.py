import time
from typing import Callable

import global_common
import schedule

from jobs import monitor_vix, cancel_unfilled_orders, get_account_summary, buy_leveraged_stocks, update_code_base
import common


def run_every_week_day(job: Callable, time: str) -> None:
    schedule.every().monday.at(time).do(global_common.run_as_separate_thread(job))
    schedule.every().tuesday.at(time).do(global_common.run_as_separate_thread(job))
    schedule.every().wednesday.at(time).do(global_common.run_as_separate_thread(job))
    schedule.every().thursday.at(time).do(global_common.run_as_separate_thread(job))
    schedule.every().friday.at(time).do(global_common.run_as_separate_thread(job))


if __name__ == "__main__":
    common.log("IBKR Jobs Started")

    run_every_week_day(monitor_vix.do, "09:30")
    run_every_week_day(monitor_vix.do, "16:00")

    run_every_week_day(get_account_summary.do, "09:30")
    run_every_week_day(get_account_summary.do, "16:00")

    run_every_week_day(buy_leveraged_stocks.do, "15:00")
    run_every_week_day(cancel_unfilled_orders.do, "15:55")

    schedule.every().sunday.at("20:00").do(global_common.run_as_separate_thread(update_code_base.do))

    while True:
        schedule.run_pending()
        time.sleep(1)
