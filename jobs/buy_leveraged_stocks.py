from decimal import Decimal

import communication.telegram
import global_common
from http_requests import ClientErrorException, ServerErrorException
from ibkr.models import Account, AccountInformation, UnfilledOrder, StockExchanges, Instrument, InstrumentType, PlaceOrderResponse, PlaceOrder, OrderType, OrderSide, CancelOrder, PortfolioPosition

import constants
from jobs import common

JOB_NAME: str = "Buying stocks leveraged"


def buy_leveraged_stocks(symbol: str, leverage: int) -> None:
    CancelOrder.all_unfilled_orders()
    for account in Account.get_all():
        PortfolioPosition.close_all_by_account_id(account.account_id)
        cash: Decimal = AccountInformation.get_by_account_id(account.account_id).available_funds
        share_price: Decimal = Instrument.get(symbol, InstrumentType.STOCK, StockExchanges.NASDAQ).last_price
        number_of_shares = int(cash * Decimal(str(leverage)) / share_price)

        communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, f"<b><u>{JOB_NAME}</u></b>"
                                                                             f"\n\nAccount ID: <i>{account.account_id}</i>"
                                                                             f"\n\nCash: <i>{cash}</i>"
                                                                             f"\nShares to buy: <i>{symbol}</i>"
                                                                             f"\nNumber of Shares: <i>{number_of_shares}</i>", True)

        if number_of_shares > 0:
            PlaceOrder(symbol, OrderType.MARKET, OrderSide.BUY, number_of_shares, None, account.account_id).execute()


def do() -> None:
    common.log("Running job: " + str(__file__).split("/")[-1])
    try:
        buy_leveraged_stocks("TQQQ", 3)
    except ClientErrorException as e:
        message: str = f"<b><u>ERROR</u></b>\n\nJob Name: <i>{JOB_NAME}</i>\nError: <i>Client Error Exception</i>"
        if str(e) != "":
            message = message + f"\nError Message: <i>{str(e)}</i>"
        communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, message, True)
    except ServerErrorException as e:
        message = f"<b><u>ERROR</u></b></u>\n\nJob Name: <i>{JOB_NAME}</i>\nError: <i>Server Error Exception</i>"
        if str(e) != "":
            message = message + f"\nError Message: <i>{str(e)}</i>"
        communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, message, True)


if __name__ == "__main__":
    do()
