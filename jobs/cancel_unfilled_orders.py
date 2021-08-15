import global_common
from ibkr.models import CancelOrder


@global_common.threaded
@global_common.job("Cancel Unfilled Orders")
def do() -> None:
    CancelOrder.all_unfilled_orders()


if __name__ == "__main__":
    do()
