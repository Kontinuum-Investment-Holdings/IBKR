from decimal import Decimal

import communication.telegram
from ibkr.models import Account, AccountInformation, StockExchanges, Instrument, InstrumentType, PlaceOrder, OrderType, OrderSide, CancelOrder, PortfolioPosition

import common
import constants


@common.job("Buying stocks leveraged")
def buy_leveraged_stocks(symbol: str, leverage: int) -> None:
    CancelOrder.all_unfilled_orders()
    for account in Account.get_all():
        PortfolioPosition.close_all_by_account_id(account.account_id)
        cash: Decimal = AccountInformation.get_by_account_id(account.account_id).available_funds
        share_price: Decimal = Instrument.get(symbol, InstrumentType.STOCK, StockExchanges.NASDAQ).last_price
        number_of_shares = int(cash * Decimal(str(leverage)) / share_price)

        communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, f"<b><u>Buying Leveraged Stocks</u></b>"
                                                                             f"\n\nAccount ID: <i>{account.account_id}</i>"
                                                                             f"\n\nCash: <i>{cash}</i>"
                                                                             f"\nShares to buy: <i>{symbol}</i>"
                                                                             f"\nNumber of Shares: <i>{number_of_shares}</i>", True)

        if number_of_shares > 0:
            PlaceOrder(symbol, OrderType.MARKET, OrderSide.BUY, number_of_shares, None, account.account_id).execute()


def do() -> None:
    buy_leveraged_stocks("TQQQ", 3)


if __name__ == "__main__":
    do()
