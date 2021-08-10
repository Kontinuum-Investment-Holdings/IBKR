import os

import common
import constants


def pull_codebase(working_directory: str) -> None:
    os.chdir(working_directory)
    os.system("git reset --hard origin/main")
    os.system("git pull origin main")


def restart_IBKR() -> None:
    os.chdir(constants.PROJECT_DIRECTORY + "IBKR")
    os.system("source ~/.bash_profile && nohup python3 scheduler.py -m >> logs/ibkr.log 2>&1 &")
    quit()


@common.job("Update code base")
def do() -> None:
    pull_codebase(constants.PROJECT_DIRECTORY + "KIH_API")
    pull_codebase(constants.PROJECT_DIRECTORY + "IBKR")
    restart_IBKR()


if __name__ == "__main__":
    do()
