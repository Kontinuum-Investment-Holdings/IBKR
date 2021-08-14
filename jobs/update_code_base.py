import global_common

import common
import constants


@common.job("Update code base")
@global_common.threaded
def do() -> None:
    global_common.update_code_base(constants.PROJECT_DIRECTORY + "ibeam", "master")
    common.restart_ibeam()

    global_common.update_code_base(constants.PROJECT_DIRECTORY + "KIH_API", "main")
    global_common.update_code_base(constants.PROJECT_DIRECTORY + "IBKR", "main")
    common.restart_IBKR()


if __name__ == "__main__":
    common.kill_all_IBKR_scheduler()
    do()
