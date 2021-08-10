import os

import common
import constants


def pull_codebase(working_directory: str) -> None:
    os.chdir(working_directory)
    os.system("git reset --hard origin/main")
    os.system("git pull origin main")


@common.job("Update code base")
def do() -> None:
    pull_codebase(constants.PROJECT_DIRECTORY + "IBKR")
    pull_codebase(constants.PROJECT_DIRECTORY + "KIH_API")


if __name__ == "__main__":
    do()
