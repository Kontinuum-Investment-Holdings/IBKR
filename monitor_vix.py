from decimal import Decimal

import communication.telegram
from http_requests import ClientErrorException, ServerErrorException
from ibkr.models import Instrument, StockExchanges, InstrumentType

JOB_NAME: str = "Monitor VIX"


def monitor_vix() -> None:
    vix_index: Decimal = Instrument.get("VIX", InstrumentType.INDEX, StockExchanges.CBOE).last_price
    communication.telegram.send_message(communication.telegram.constants.telegram_channel_username_development, f"VIX Index: {str(vix_index)}", False)


if __name__ == "__main__":
    try:
        monitor_vix()
    except ClientErrorException as e:
        message: str = f"<b><u>ERROR</u></b>\n\nJob Name: <i>{JOB_NAME}</i>\nError: <i>Client Error Exception</i>"
        if str(e) != "":
            message = message + f"\nError Message: <i>{str(e)}</i>"
        communication.telegram.send_message(communication.telegram.constants.telegram_channel_username_development, message, True)
    except ServerErrorException as e:
        message = f"<b><u>ERROR</u></b></u>\n\nJob Name: <i>{JOB_NAME}</i>\nError: <i>Server Error Exception</i>"
        if str(e) != "":
            message = message + f"\nError Message: <i>{str(e)}</i>"
        communication.telegram.send_message(communication.telegram.constants.telegram_channel_username_development, message, True)
