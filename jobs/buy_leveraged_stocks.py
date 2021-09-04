import time
from decimal import Decimal

import communication.telegram
import global_common
import ibkr.common
from ibkr.models import IBKR, OrderAction, OrderType, SecurityType

import constants
from jobs import get_account_summary


@global_common.threaded
@ibkr.common.job("Buying stocks leveraged", True, "QQQ")
def buy_leveraged_stocks(symbol: str, leverage: int) -> None:
    IBKR.close_all_positions()
    time.sleep(10)
    cash: Decimal = IBKR.request_account_summary().cash_balance
    number_of_stocks: Decimal = Decimal(int((cash * Decimal(str(leverage))) / IBKR.get_current_ask_price(symbol)))

    if number_of_stocks > 0:
        IBKR.place_order("QQQ", number_of_stocks, None, OrderAction.BUY, OrderType.MARKET, SecurityType.CFD)

    communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, f"<b><u>Buying Leveraged Stocks</u></b>"
                                                                         f"\n\nCash: <i>${global_common.get_formatted_string_from_decimal(cash)}</i>"
                                                                         f"\nShares to buy: <i>{symbol}</i>"
                                                                         f"\nNumber of Shares: <i>{number_of_stocks}</i>", True)

    time.sleep(60)
    get_account_summary.do()


def do() -> None:
    buy_leveraged_stocks("QQQ", 3)


if __name__ == "__main__":
    do()
