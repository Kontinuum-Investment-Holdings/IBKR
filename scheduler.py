import time
from typing import Callable

import schedule

import common
from jobs import buy_leveraged_stocks


def run_every_week_day(job: Callable, time: str) -> None:
    schedule.every().monday.at(time).do(job)
    schedule.every().tuesday.at(time).do(job)
    schedule.every().wednesday.at(time).do(job)
    schedule.every().thursday.at(time).do(job)
    schedule.every().friday.at(time).do(job)


if __name__ == "__main__":
    common.log("IBKR Jobs Started")

    run_every_week_day(buy_leveraged_stocks.do, "09:35")
    run_every_week_day(buy_leveraged_stocks.do, "10:00")
    run_every_week_day(buy_leveraged_stocks.do, "11:00")
    run_every_week_day(buy_leveraged_stocks.do, "12:00")
    run_every_week_day(buy_leveraged_stocks.do, "13:00")
    run_every_week_day(buy_leveraged_stocks.do, "14:00")
    run_every_week_day(buy_leveraged_stocks.do, "15:00")
    run_every_week_day(buy_leveraged_stocks.do, "15:55")

    while True:
        schedule.run_pending()
        time.sleep(1)
