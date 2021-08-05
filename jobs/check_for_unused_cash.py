from decimal import Decimal

import communication.telegram
import global_common
import logger
from ibkr.models import Account, AccountInformation, Instrument, StockExchanges, PlaceOrderResponse, PlaceOrder, OrderType, OrderSide, \
    UnfilledOrder, InstrumentType
from http_requests import ClientErrorException, ServerErrorException

import constants

JOB_NAME: str = "Checking for unused cash"


def buy_shares_from_remaining_cash(symbol: str) -> None:
    for account in Account.get_all():
        remaining_cash: Decimal = AccountInformation.get_by_account_id(account.account_id).available_funds - UnfilledOrder.get_all_unfilled_orders_value(StockExchanges.NASDAQ)
        share_price: Decimal = Instrument.get(symbol, InstrumentType.STOCK, StockExchanges.NASDAQ).last_price
        number_of_shares = min(int(remaining_cash / share_price), 499)

        communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, f"<b><u>{JOB_NAME}</u></b>"
                                                                             f"\n\nAccount ID: <i>{account.account_id}</i>"
                                                                             f"\nRemaining Cash: <i>${global_common.get_formatted_string_from_decimal(remaining_cash)}</i>"
                                                                             f"\nShares to buy: <i>{symbol}</i>"
                                                                             f"\nNumber of Shares: <i>{number_of_shares}</i>", True)

        if number_of_shares > 0:
            order_response: PlaceOrderResponse = PlaceOrder(symbol, OrderType.MARKET, OrderSide.BUY, number_of_shares, None, account.account_id).execute()


def do():
    logger.info("Running job: " + str(__file__).split("/")[-1])
    try:
        buy_shares_from_remaining_cash("TQQQ")
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
