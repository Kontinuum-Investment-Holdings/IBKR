import os
from typing import Callable, Any

import communication.telegram
import global_common
import logger
from http_requests import ClientErrorException, ServerErrorException

import constants


def log(log: str) -> None:
    if log.endswith(".py"):
        log = log.replace(".py", "")

    logger.info(log)
    communication.telegram.send_message(constants.TELEGRAM_BOT_DEV_USERNAME, f"<i>{log}</i>", True)


def job(job_name: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def exception_handled_func(*args: Any, **kwargs: Any) -> None:
            try:
                log("Running job: " + job_name)
                func(*args, **kwargs)
            except ClientErrorException as e:
                message: str = f"<b><u>ERROR</u></b>\n\nJob Name: <i>{job_name}</i>\nError: <i>Client Error Exception</i>"
                if str(e) != "":
                    message = message + f"\nError Message: <i>{str(e).replace('<', '').replace('>', '')}</i>"
                communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, message, True)
            except ServerErrorException as e:
                message = f"<b><u>ERROR</u></b>\n\nJob Name: <i>{job_name}</i>\nError: <i>Server Error Exception</i>"
                if str(e) != "":
                    message = message + f"\nError Message: <i>{str(e).replace('<', '').replace('>', '')}</i>"
                communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, message, True)
            except Exception as e:
                message = f"<b><u>ERROR</u></b>\n\nJob Name: <i>{job_name}</i>\nError: <i>Unhandled Exception</i>"
                if str(e) != "":
                    message = message + f"\nError Message: <i>{str(e).replace('<', '').replace('>', '')}</i>"
                communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, message, True)

        return exception_handled_func

    return decorator


def restart_IBKR() -> None:
    os.chdir(constants.PROJECT_DIRECTORY + "IBKR")
    global_common.run_command(["nohup python3 scheduler.py -m >> logs/ibkr.log 2>&1 &"], True)
    quit()


def kill_all_IBKR_scheduler() -> None:
    global_common.kill_process("scheduler.py", "python3")


def restart_ibeam():
    os.chdir(constants.PROJECT_DIRECTORY + "ibeam")
    global_common.kill_process("ibeam_starter.py", "python3")
    global_common.run_command(["python3 ibeam/ibeam_starter.py >> logs/ibeam.log 2>&1", "nohup python3 ibeam/ibeam_starter.py -m >> logs/ibeam.log 2>&1 &"])

