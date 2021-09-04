import global_common
import ibkr.common
from ibkr.models import IBKR


@global_common.threaded
@ibkr.common.job("Cancel Unfilled Orders", True, "QQQ")
def do() -> None:
    IBKR.cancel_all_orders()


if __name__ == "__main__":
    do()
