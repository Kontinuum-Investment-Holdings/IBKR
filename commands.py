import sys

import common

if __name__ == "__main__":
    if sys.argv[1] == "kill":
        common.kill_all_IBKR_scheduler()
    elif sys.argv[1] == "restart":
        common.kill_all_IBKR_scheduler()
        common.restart_IBKR()
    elif sys.argv[1] == "ibeam_restart":
        common.restart_ibeam()
    else:
        raise Exception("Unknown command")
