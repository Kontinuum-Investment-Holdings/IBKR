import communication.telegram
import logger

import constants


def log(log: str) -> None:
    if log.endswith(".py"):
        log = log.replace(".py", "")

    logger.info(log)
    communication.telegram.send_message(constants.TELEGRAM_BOT_DEV_USERNAME, f"<i>{log}</i>", True)