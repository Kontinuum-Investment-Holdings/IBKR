import time

import communication.telegram

import constants

time.sleep(10)
communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, "This is a test for the scheduler", False)
