from ibkr.models import CancelOrder

import common
import global_common


@common.job("Cancel Unfilled Orders")
@global_common.threaded
def do() -> None:
    CancelOrder.all_unfilled_orders()


if __name__ == "__main__":
    do()
