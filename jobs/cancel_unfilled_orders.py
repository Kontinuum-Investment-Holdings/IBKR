from ibkr.models import CancelOrder

import common


@common.job("Cancel Unfilled Orders")
def do() -> None:
    CancelOrder.all_unfilled_orders()


if __name__ == "__main__":
    do()
