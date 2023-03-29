import tkinter

from wallet_schema import Wallet, empty_wallet_data, get_current_price
from datetime import datetime

root = tkinter.Tk()
root.geometry('800x400')

wallet_instance = None


def show_wallet(wallet):
    global wallet_instance
    print("Twój portfel to:")
    print(wallet)

def update_label_value(label, value):
    label.config(text=value)
    value = get_current_price("BTCPLN")
    label.after(2, update_label_value, label, value)

# child windows -------------------------------------------------------------------------------------------------------

def open_child_window_create_wallet():
    child_window = tkinter.Toplevel(root)
    child_window.geometry('400x200')
    child_window.title("Tworzenie portfela")

    owner_entry = tkinter.Entry(child_window, width=10)
    owner_entry.grid(row=0, column=1)

    def create_wallet():
        global wallet_instance
        owner = owner_entry.get()
        print("Stworzono nowy portfel")
        empty_wallet_data['owner'] = owner
        print(empty_wallet_data)
        wallet_instance = Wallet(**empty_wallet_data)

        child_window.destroy()

        return wallet_instance

    exchange_button = tkinter.Button(child_window, text="Stwórz", command=create_wallet)
    exchange_button.grid(row=1, column=0, columnspan=2)


def open_child_window_exchange_currency():
    child_window = tkinter.Toplevel(root)
    child_window.geometry('400x200')
    child_window.title("Wymiana waluty")

    currencies_1 = ["BTC", "ETH", "PLN", "EUR"]
    selected_currency_1 = tkinter.StringVar()
    selected_currency_1.set(currencies_1[0])

    currencies_2 = ["EUR", "PLN", "BTC", "ETH"]
    selected_currency_2 = tkinter.StringVar()
    selected_currency_2.set(currencies_2[0])

    amount_entry = tkinter.Entry(child_window, width=10)
    amount_entry.grid(row=0, column=1)

    crypto_currencies_menu = tkinter.OptionMenu(child_window, selected_currency_1, *currencies_1)
    crypto_currencies_menu.grid(row=0, column=0)

    currencies_menu = tkinter.OptionMenu(child_window, selected_currency_2, *currencies_2)
    currencies_menu.grid(row=0, column=2)

    value_label = tkinter.Label(child_window, text="0")
    value_label.grid(row=1, column=0)

    # update label with acctual btc price
    update_label_value(value_label, get_current_price("BTCPLN"))

    def exchange_currency():
        currency_1 = selected_currency_1.get()
        currency_2 = selected_currency_2.get()
        amount = float(amount_entry.get())
        print(f"Wymiana {amount} {currency_1} na {currency_2}")

        if currency_1 == "BTC" and currency_2 == "PLN":
            # update_label_value(value_label, 0, get_current_price('BTC'))
            Wallet.BTC_to_PLN(wallet_instance, amount)

        if currency_1 == "ETH" and currency_2 == "PLN":
            Wallet.ETH_to_PLN(wallet_instance, amount)
            # update_label_value(value_label, 0, get_current_price('ETH'))

        if currency_1 == "PLN" and currency_2 == "BTC":
            Wallet.PLN_to_BTC(wallet_instance, amount)
            # update_label_value(value_label, 0, get_current_price('BTC'))

        if currency_1 == "PLN" and currency_2 == "ETH":
            Wallet.PLN_to_ETH(wallet_instance, amount)
            # update_label_value(value_label, 0, get_current_price('ETH'))

        child_window.destroy()

    exchange_button = tkinter.Button(child_window, text="Wymień", command=exchange_currency)
    exchange_button.grid(row=1, column=3, columnspan=2)


b1 = tkinter.Button(root, text="Stwórz portfel", command=open_child_window_create_wallet, bd=1, width=10, height=2)
b1.place(x=0, y=0)

b2 = tkinter.Button(root, text="Pokaz portfel", command=lambda: show_wallet(wallet_instance), bd=1, width=10, height=2)
b2.place(x=100, y=0)

b3 = tkinter.Button(root, text="Wymiana na PLN", command=open_child_window_exchange_currency, bd=1, width=10, height=2)
b3.place(x=200, y=0)

root.mainloop()