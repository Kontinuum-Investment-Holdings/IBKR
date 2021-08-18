import time
from typing import Callable

import schedule

import common
from jobs import monitor_vix, cancel_unfilled_orders, get_account_summary, buy_leveraged_stocks, update_code_base, check_authentication_status


def run_every_week_day(job: Callable, time: str) -> None:
    schedule.every().monday.at(time).do(job)
    schedule.every().tuesday.at(time).do(job)
    schedule.every().wednesday.at(time).do(job)
    schedule.every().thursday.at(time).do(job)
    schedule.every().friday.at(time).do(job)


if __name__ == "__main__":
    common.log("IBKR Jobs Started")

    schedule.every().hour.at(":00").do(check_authentication_status.do)
    schedule.every().hour.at(":10").do(check_authentication_status.do)
    schedule.every().hour.at(":20").do(check_authentication_status.do)
    schedule.every().hour.at(":30").do(check_authentication_status.do)
    schedule.every().hour.at(":40").do(check_authentication_status.do)
    schedule.every().hour.at(":50").do(check_authentication_status.do)

    run_every_week_day(monitor_vix.do, "09:30")
    run_every_week_day(monitor_vix.do, "16:00")

    run_every_week_day(get_account_summary.do, "09:30")
    run_every_week_day(get_account_summary.do, "16:00")

    run_every_week_day(cancel_unfilled_orders.do, "15:55")

    run_every_week_day(buy_leveraged_stocks.do, "09:00")
    run_every_week_day(buy_leveraged_stocks.do, "10:00")
    run_every_week_day(buy_leveraged_stocks.do, "11:00")
    run_every_week_day(buy_leveraged_stocks.do, "12:00")
    run_every_week_day(buy_leveraged_stocks.do, "13:00")
    run_every_week_day(buy_leveraged_stocks.do, "14:00")
    run_every_week_day(buy_leveraged_stocks.do, "15:00")
    run_every_week_day(buy_leveraged_stocks.do, "16:00")

    schedule.every().hour.at(":30").do(update_code_base.do)

    while True:
        schedule.run_pending()
        time.sleep(1)
