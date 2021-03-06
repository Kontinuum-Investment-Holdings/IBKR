import time

import communication.telegram
import global_common
import ibkr.common
from ibkr.models import IBKR

import constants


@global_common.threaded
@ibkr.common.job("Check connection status")
def check_connection_status(number_of_tries: int = 0) -> None:
    is_connection_successful: bool = IBKR.is_connection_successful()
    if is_connection_successful:
        communication.telegram.send_message(constants.TELEGRAM_BOT_DEV_USERNAME, f"<b>Connection status: </b> <i>Successful</i>", True)
    else:
        communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, f"<b><u>Connection status: </u></b> <i>Unsuccessful</i>", True)
        time.sleep(60)

        if number_of_tries < 5:
            check_connection_status(number_of_tries + 1)


def do() -> None:
    check_connection_status()


if __name__ == "__main__":
    do()
