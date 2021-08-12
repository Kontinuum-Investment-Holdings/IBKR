import global_common

import common
import constants


@common.job("Update code base")
def do() -> None:
    global_common.update_code_base(constants.PROJECT_DIRECTORY + "KIH_API")
    global_common.update_code_base(constants.PROJECT_DIRECTORY + "IBKR")

    if __name__ == "__main__":
        common.kill_all_IBKR_scheduler()

    common.restart_IBKR()


if __name__ == "__main__":
    do()
