from datetime import datetime
from typing import Optional

import requests
from pydantic import BaseModel, validator, ValidationError
import pickle


class NEGATIVEVALUE(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class TYPEVALUEerror(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


def validate_amount(value):
    if value.strip() == '':
        return "EMPTY_STRING"
    try:
        value = float(value)
        return value
    except:
        return "VALUEERROR"


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
                      "owner": "John",
                      "BTC_amount": 1.003,
                      "ETH_amount": 1.4,
                      "PLN_amount": 200500,
                      "EUR_amount": 42000,
                      "history_transaction": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

empty_wallet_data = {"id": 1,
                     "owner": "",
                     "BTC_amount": 0.00,
                     "ETH_amount": 0.0,
                     "PLN_amount": 000,
                     "EUR_amount": 0.0,
                     "history_transaction": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


corupted_wallet_data = {"id": 1,
                        "owner": "",
                        "BTC_amount": "a",
                        "ETH_amount": 0.0,
                        "PLN_amount": -1000,
                        "EUR_amount": True,
                        "history_transaction": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

class Wallet(BaseModel):
    id: Optional[int] = None
    owner: str
    BTC_amount: float
    ETH_amount: float
    PLN_amount: float
    EUR_amount: float
    history_transaction: datetime

    def create_wallet(self, owner):

        print("Created wallet")
        empty_wallet_data["owner"] = owner
        wallet_instance = Wallet(**empty_wallet_data)
        self.wallet_instance = wallet_instance

        with open("wallet.pkl", 'wb') as f:
            pickle.dump(wallet_instance, f)


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
            print("you don't have enough ETH")
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

    def EUR_to_ETH(self, amount):
        course = get_current_price("ETHEUR")

        if amount > self.EUR_amount:
            print("you don't have enough EUR")
        else:
            self.EUR_amount -= amount
            self.ETH_amount += amount / course

    def BTC_to_EUR(self, amount):
        course = get_current_price("BTCEUR")

        if amount > self.BTC_amount:
            print("you don't have enough BTC")
        else:
            self.BTC_amount -= amount
            self.EUR_amount += amount * course

    def EUR_to_BTC(self, amount):
        course = get_current_price("BTCEUR")

        if amount > self.EUR_amount:
            print("you don't have enough EUR")
        else:
            self.EUR_amount -= amount
            self.BTC_amount += amount / course

    def add_PLN(self):
        self.PLN_amount += 25000

