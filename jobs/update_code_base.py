import global_common

import common
import constants


@global_common.threaded
@global_common.job("Update code base")
def do() -> None:
    global_common.update_code_base(constants.PROJECT_DIRECTORY + "KIH_API", "main")
    global_common.update_code_base(constants.PROJECT_DIRECTORY + "IBKR", "main")


if __name__ == "__main__":
    common.kill_all_IBKR_scheduler()
    do()
