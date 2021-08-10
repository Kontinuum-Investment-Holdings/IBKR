import os
import sys

TELEGRAM_BOT_USERNAME: str = os.getenv("TELEGRAM_BOT_USERNAME")
TELEGRAM_BOT_DEV_USERNAME: str = os.getenv("TELEGRAM_BOT_DEV_USERNAME")

PROJECT_DIRECTORY: str = "NOT PROGRAMMED FOR WINDOWS"
if sys.platform == "linux":
    PROJECT_DIRECTORY = os.getenv("HOME") + "/python_projects/"
