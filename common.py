import os

import communication.telegram
import global_common
from logger import logger

import constants


def log(log: str) -> None:
    if log.endswith(".py"):
        log = log.replace(".py", "")

    logger.debug(log)
    communication.telegram.send_message(constants.TELEGRAM_BOT_DEV_USERNAME, f"<i>{log}</i>", True)


def restart_IBKR() -> None:
    os.chdir(constants.PROJECT_DIRECTORY + "IBKR")
    global_common.run_command(["nohup python3 scheduler.py -m >> logs/ibkr.log 2>&1 &"])
    quit()


def kill_all_IBKR_scheduler() -> None:
    global_common.kill_process("scheduler.py", "python3")


def restart_ibeam() -> None:
    os.chdir(constants.PROJECT_DIRECTORY + "ibeam")
    global_common.kill_process("ibeam_starter.py", "python3")
    global_common.run_command(["python3 ibeam/ibeam_starter.py >> logs/ibeam.log 2>&1", "nohup python3 ibeam/ibeam_starter.py -m >> logs/ibeam.log 2>&1 &"])
