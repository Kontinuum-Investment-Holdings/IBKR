import communication.telegram
import global_common
from ibkr import Authentication, ReAuthentication
from logger import logger

import constants


@global_common.threaded
@global_common.job("Checking Authentication Status")
def do() -> None:
    authentication: Authentication = Authentication.call()
    if authentication.authenticated:
        communication.telegram.send_message(constants.TELEGRAM_BOT_DEV_USERNAME, f"Authentication status: <i>True</i>", True)
    else:
        if ReAuthentication.call().authenticated:
            communication.telegram.send_message(constants.TELEGRAM_BOT_DEV_USERNAME, f"Forced Authentication status: <i>True</i>", True)
        else:
            communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, f"Forced Authentication status: <i>False</i>", True)

    logger.info(f"Authentication status: {authentication.authenticated}")


if __name__ == "__main__":
    do()
