from decimal import Decimal

import communication.telegram
from ibkr.models import Instrument, InstrumentType, StockExchanges

import common
import constants


@common.job("Monitor VIX")
def monitor_vix() -> None:
    vix_index: Decimal = Instrument.get("VIX", InstrumentType.INDEX, StockExchanges.CBOE).last_price
    communication.telegram.send_message(constants.TELEGRAM_BOT_USERNAME, f"VIX Index: {str(vix_index)}", False)


def do() -> None:
    monitor_vix()


if __name__ == "__main__":
    do()
