from datetime import datetime
from typing import Optional

import requests
from pydantic import BaseModel, validator, ValidationError


class NEGATIVEVALUE(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class TYPEVALUEerror(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


def get_current_price(currency: str):
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    # key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCPLN"
    key = key + currency
    # requesting data from url
    data = requests.get(key)
    data = data.json()
    # print(f"{data['symbol']} price is {data['price']}")
    data = data['price']
    return float(data)


sample_wallet_data = {"id": 1,
                      "BTC_amount": 0.003,
                      "ETH_amount": 0.4,
                      "PLN_amount": 500,
                      "history_transaction": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

empty_wallet_data = {"id": 1,
                     "BTC_amount": 0.00,
                     "ETH_amount": 0.0,
                     "PLN_amount": 000,
                     "history_transaction": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

corupted_wallet_data = {"id": 1,
                        "BTC_amount": "a",
                        "ETH_amount": 0.0,
                        "PLN_amount": -1000,
                        "history_transaction": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


class Wallet(BaseModel):
    id: Optional[int] = None
    BTC_amount: float
    ETH_amount: float
    PLN_amount: float
    history_transaction: datetime

    @validator("BTC_amount")
    def btc_valid(cls, value):
        if value < 0:
            raise NEGATIVEVALUE(message="btc amount can't be negative")
        if type(value) != float:
            raise TYPEVALUEerror(message="btc amount can't be string")
        return value

    def PLN_to_BTC(self, amount):
        course = get_current_price("BTCPLN")

        if amount > self.PLN_amount:
            # raise NEGATIVEVALUE(amount, message="you don't have enough pln")
            print("you don't have enough PLN")
        else:
            self.PLN_amount -= amount
            self.BTC_amount += amount / course

    def BTC_to_PLN(self, amount):
        course = get_current_price("BTCPLN")

        if amount > self.BTC_amount:
            print("you don't have enough BTC")
        else:
            self.BTC_amount -= amount
            self.PLN_amount += amount * course

    def ETH_to_PLN(self, amount):
        course = get_current_price("ETHPLN")

        if amount > self.ETH_amount:
            # raise NEGATIVEVALUE(amount, message="you don't have enough euro")
            print("you don't have enough Euro")
        else:
            self.ETH_amount -= amount
            self.PLN_amount += amount * course

    def PLN_to_ETH(self, amount):
        course = get_current_price("ETHPLN")

        if amount > self.PLN_amount:
            print("you don't have enough PLN")
        else:
            self.PLN_amount -= amount
            self.ETH_amount += amount / course


# try:
#     wallet = Wallet(**sample_wallet_data)
#     empty_wallet = Wallet(**empty_wallet_data)
#     corupted_wallet = Wallet(**corupted_wallet_data)
#
# except ValidationError as error:
#     print(error.json())
#
# print(f"Found a wallet: {wallet}")
#
# wallet.PLN_to_BTC(1000)
# print(f"Wallet after converting 100 PLN to BTC: {wallet}")
#
# wallet.BTC_to_PLN(0.002)
# print(f"Wallet after converting 1 BTC to PLN: {wallet}")
#
# wallet.PLN_to_ETH(100)
# print(f"Wallet after converting 100 PLN to ETH: {wallet}")
#
# wallet.ETH_to_PLN(0.4)
# print(f"Wallet after converting 0.4 ETH to PLN: {wallet}")
