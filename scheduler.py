import time

import schedule

import monitor_vix

if __name__ == "__main__":
    schedule.every(10).seconds.do(monitor_vix.monitor_vix())

    while True:
        schedule.run_pending()
        time.sleep(1)
