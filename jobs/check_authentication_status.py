import communication.telegram
import logger
from ibkr import Authentication

import constants


def do() -> None:
    authentication: Authentication = Authentication.call()
    if authentication.authenticated:
        communication.telegram.send_message(constants.TELEGRAM_BOT_DEV_USERNAME, f"Authentication status: <i>True</i>", True)
    else:
        communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, f"Authentication status: <i>False</i>", True)

    logger.info(f"Authentication status: {authentication.authenticated}")


if __name__ == "__main__":
    do()
