import time

import communication

import constants

time.sleep(10)
communication.telegram(constants.TELEGRAM_BOT_USERNAME, "This is a test for the scheduler", False)
