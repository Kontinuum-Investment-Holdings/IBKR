import communication.telegram
from http_requests import ClientErrorException, ServerErrorException
from ibkr.models import UnfilledOrder, CancelOrderResponse, CancelOrder

JOB_NAME: str = "Cancel Unfilled Orders"


def cancel_unfilled_orders() -> None:
    for unfilled_order in UnfilledOrder.get():
        cancel_order: CancelOrderResponse = CancelOrder(unfilled_order).execute()


if __name__ == "__main__":
    try:
        cancel_unfilled_orders()
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