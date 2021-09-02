import communication.telegram
import global_common
from ibkr.models import Account, IBKR

import constants


@global_common.threaded
@global_common.job("Getting Account Summary")
def get_account_summary() -> None:
    account: Account = IBKR.request_account_summary()
    communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, f"<b><u>Account Summary</u></b>"
                                                                         f"\n\nCash: <i>${global_common.get_formatted_string_from_decimal(account.cash_balance)}</i>"
                                                                         f"\nMarket value of stocks: <i>${global_common.get_formatted_string_from_decimal(account.stock_market_value)}</i>"
                                                                         f"\nNet Liquidity: <i>${global_common.get_formatted_string_from_decimal(account.cash_balance + account.stock_market_value)}</i>", True)


def do() -> None:
    get_account_summary()


if __name__ == "__main__":
    do()
