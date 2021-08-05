import communication.telegram
import logger

import constants


def log(log: str) -> None:
    logger.info(log)
    communication.telegram.send_message(constants.TELEGRAM_BOT_DEV_USERNAME, log, False)