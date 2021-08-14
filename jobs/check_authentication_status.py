import communication.telegram
from ibkr import Authentication
from logger import logger

import common
import constants
import global_common


@common.job("Checking Authentication Status")
@global_common.threaded
def do() -> None:
    authentication: Authentication = Authentication.call()
    if authentication.authenticated:
        communication.telegram.send_message(constants.TELEGRAM_BOT_DEV_USERNAME, f"Authentication status: <i>True</i>", True)
    else:
        communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, f"Authentication status: <i>False</i>", True)

    logger.info(f"Authentication status: {authentication.authenticated}")


if __name__ == "__main__":
    do()
