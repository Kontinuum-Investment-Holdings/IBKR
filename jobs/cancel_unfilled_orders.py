import communication.telegram
from http_requests import ClientErrorException, ServerErrorException
from ibkr.models import CancelOrder

import constants
from jobs import common

JOB_NAME: str = "Cancel Unfilled Orders"


def do() -> None:
    common.log("Running job: " + str(__file__).split("/")[-1])
    try:
        CancelOrder.all_unfilled_orders()
    except ClientErrorException as e:
        message: str = f"<b><u>ERROR</u></b>\n\nJob Name: <i>{JOB_NAME}</i>\nError: <i>Client Error Exception</i>"
        if str(e) != "":
            message = message + f"\nError Message: <i>{str(e)}</i>"
        communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, message, True)
    except ServerErrorException as e:
        message = f"<b><u>ERROR</u></b></u>\n\nJob Name: <i>{JOB_NAME}</i>\nError: <i>Server Error Exception</i>"
        if str(e) != "":
            message = message + f"\nError Message: <i>{str(e)}</i>"
        communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, message, True)


if __name__ == "__main__":
    do()
