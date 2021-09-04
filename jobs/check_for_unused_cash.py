from decimal import Decimal

import communication.telegram
import global_common
from ibkr.models import OrderType, IBKR, OrderAction, SecurityType
import ibkr.common

import constants


@global_common.threaded
@ibkr.common.job("Checking for unused cash", True, "QQQ")
def check_for_unused_cash(symbol: str) -> None:
    remaining_cash: Decimal = IBKR.request_account_summary().cash_balance
    number_of_shares: Decimal = Decimal(int(remaining_cash / IBKR.get_current_ask_price(symbol)))
    if number_of_shares > 0:
        IBKR.place_order(symbol, number_of_shares, None, OrderAction.BUY, OrderType.MARKET, SecurityType.STOCK)
        communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, f"<b><u>Checking for unused cash</u></b>"
                                                                             f"\nRemaining Cash: <i>${global_common.get_formatted_string_from_decimal(remaining_cash)}</i>"
                                                                             f"\nShares to buy: <i>{symbol}</i>"
                                                                             f"\nNumber of Shares: <i>{number_of_shares}</i>", True)


def do() -> None:
    check_for_unused_cash("TQQQ")


if __name__ == "__main__":
    do()
