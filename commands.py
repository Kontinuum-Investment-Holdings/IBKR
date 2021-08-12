import sys

import global_common

from modules import common

if __name__ == "__main__":
    if sys.argv[1] == "kill":
        global_common.kill_process("scheduler.py", "python3")
    elif sys.argv[1] == "start":
        common.restart_IBKR()
