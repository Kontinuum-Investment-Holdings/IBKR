from decimal import Decimal
from typing import List

import communication.telegram
import global_common
from ibkr.models import PortfolioPosition, AccountInformation, Account

import common
import constants


@common.job("Getting Account Summary")
def get_account_summary() -> None:
    net_worth: Decimal = Decimal("0")
    message: str = "<b><u>Account Summary</u></b>\n"
    for account in Account.get_all():
        account_information: AccountInformation = AccountInformation.get_by_account_id(account.account_id)
        net_worth = net_worth + account_information.net_liquidity

        message = message + f"\n<u><i>{account.alias}</i></u>" \
                            f"\nAccount ID: <i>{account.account_id}</i>"

        portfolio_positions: List[PortfolioPosition] = PortfolioPosition.get_by_account_id(account.account_id)
        for portfolio_position in portfolio_positions:
            message = message + f"\nInstrument: <i>{portfolio_position.symbol}</i>" \
                                f"\nPosition: <i>{portfolio_position.position}</i>" \
                                f"\nMarket Price: <i>${global_common.get_formatted_string_from_decimal(portfolio_position.market_price)}</i>" \
                                f"\nMarket Value: <i>${global_common.get_formatted_string_from_decimal(portfolio_position.market_value)}</i>\n"

        message = message + f"\nCash Holdings: <i>${global_common.get_formatted_string_from_decimal(account_information.available_funds)}\n</i>"

    message = message + f"\nTotal Net Worth: <u><i>${global_common.get_formatted_string_from_decimal(net_worth)}</i></u>"
    communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, message, True)


def do() -> None:
    get_account_summary()


if __name__ == "__main__":
    do()
