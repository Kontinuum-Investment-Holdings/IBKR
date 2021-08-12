import sys

import global_common

import common

if __name__ == "__main__":
    if sys.argv[1] == "kill":
        common.kill_all_IBKR_scheduler()
    elif sys.argv[1] == "start":
        common.restart_IBKR()
