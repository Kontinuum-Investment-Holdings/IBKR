from decimal import Decimal

import communication.telegram
import global_common
from ibkr.models import Account, AccountInformation, UnfilledOrder, StockExchanges, Instrument, InstrumentType, PlaceOrderResponse, PlaceOrder, OrderType, OrderSide

import constants


@global_common.job("Checking for unused cash")
@global_common.threaded
def check_for_unused_cash(symbol: str) -> None:
    for account in Account.get_all():
        remaining_cash: Decimal = AccountInformation.get_by_account_id(account.account_id).available_funds - UnfilledOrder.get_all_unfilled_orders_value(StockExchanges.NASDAQ)
        share_price: Decimal = Instrument.get(symbol, InstrumentType.STOCK, StockExchanges.NASDAQ).last_price
        number_of_shares = min(int(remaining_cash / share_price), 499)

        communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, f"<b><u>Checking for unused cash</u></b>"
                                                                             f"\n\nAccount ID: <i>{account.account_id}</i>"
                                                                             f"\nRemaining Cash: <i>${global_common.get_formatted_string_from_decimal(remaining_cash)}</i>"
                                                                             f"\nShares to buy: <i>{symbol}</i>"
                                                                             f"\nNumber of Shares: <i>{number_of_shares}</i>", True)

        if number_of_shares > 0:
            order_response: PlaceOrderResponse = PlaceOrder(symbol, OrderType.MARKET, OrderSide.BUY, number_of_shares, None, account.account_id).execute()


def do() -> None:
    check_for_unused_cash("TQQQ")


if __name__ == "__main__":
    do()
