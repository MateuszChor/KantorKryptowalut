import tkinter as tk
from src.dirtectory_operator import EXCHANGE_BUTTON_IMG, EXIT_BUTTON_IMG, REFRESH_BUTTON_IMG, EXCHANGE_BG, MAIN_BG_IMG,BGBG,BG_CHILD_WINDOW
from src.gui.child_window import ChildWindow
from src.gui.button_on_hover import change_brightness_on_hover
from src.wallet_schema import Wallet
from src.gui.error_window import ErrorWindow
from src.wallet_schema import get_current_price
from src.load_wallet import load_wallet, save_wallet
import pickle

class ExangeWindow(ChildWindow):

    def __init__(self,master_window, wallet: pickle):
        ChildWindow.__init__(self, master_window)

        background_image = tk.PhotoImage(file=BG_CHILD_WINDOW)
        self.canvas = tk.Canvas(self.child_window, width=400, height=200)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=background_image, anchor="nw")

        currencies_1 = ["BTC", "ETH", "PLN", "EUR"]
        selected_currency_1 = tk.StringVar()
        selected_currency_1.set(currencies_1[0])

        currencies_2 = ["EUR", "PLN", "BTC", "ETH"]
        selected_currency_2 = tk.StringVar()
        selected_currency_2.set(currencies_2[0])

        self.amount_entry = tk.Entry(self.child_window, width=10)
        self.amount_entry.place(x=100, y=50)


        crypto_currencies_menu = tk.OptionMenu(self.child_window, selected_currency_1, *currencies_1)
        crypto_currencies_menu.place(x=20, y=50)

        currencies_menu = tk.OptionMenu(self.child_window, selected_currency_2, *currencies_2)
        currencies_menu.place(x=250, y=50)

        currency_1 = selected_currency_1.get()
        currency_2 = selected_currency_2.get()

        exchange_img = tk.PhotoImage(file=EXCHANGE_BUTTON_IMG)

        self.exchange_button = tk.Button(self.child_window,
                                   image=exchange_img,
                                   bg=self.background_color,
                                   borderwidth=0,
                                   highlightthickness=0,
                                   activebackground=self.background_color,
                                   activeforeground=self.background_color,
                                   command=lambda: self.exchange_currency(wallet, selected_currency_1, selected_currency_2))
        self.exchange_button.place(x=260, y=140)

        exit_img = tk.PhotoImage(file=EXIT_BUTTON_IMG)

        self.exit_button = tk.Button(self.child_window,
                                         image=exit_img,
                                         bg=self.background_color,
                                         borderwidth=0,
                                         highlightthickness=0,
                                         activebackground=self.background_color,
                                         activeforeground=self.background_color,
                                         command=self.exit_window)
        self.exit_button.place(x=374, y=5)

        refresh_img = tk.PhotoImage(file=REFRESH_BUTTON_IMG)

        self.refresh_button = tk.Button(self.child_window,
                                     image=refresh_img,
                                     bg=self.background_color,
                                     borderwidth=0,
                                     highlightthickness=0,
                                     activebackground=self.background_color,
                                     activeforeground=self.background_color,
                                     command=lambda: self.refresh_price(selected_currency_1, selected_currency_2))
        self.refresh_button.place(x=50, y=140)

        self.crypto_name = tk.Label(self.child_window,
                                    bg=self.background_color,
                                    text="",
                                    font="none 10 bold",
                                    anchor=tk.CENTER)
        self.crypto_name.place(x=80, y=240)

        self.price_1 = tk.Label(self.child_window,
                                bg=self.background_color,
                                text="",
                                font="none 10 bold",
                                anchor=tk.CENTER)
        self.price_1.place(x=270, y=240)


        change_brightness_on_hover(widget=self.exchange_button, img_path=EXCHANGE_BUTTON_IMG, factor=1.15)

        self.child_window.wait_window()

    def refresh_price(self,state1, state2):
        currency_1 = state1.get()
        currency_2 = state2.get()

        if currency_1 == currency_2:
            text = "Wybrałeś te same aktywa"
            self.crypto_name.config(text=text)
            self.price_1.config(text="")
            ErrorWindow(text, self.child_window)

        price_1 = currency_1+currency_2
        if price_1 == "PLNEUR" or price_1 == "EURPLN":
            text = "Tylko kryptowaluty !"
            self.crypto_name.config(text=text)
            self.price_1.config(text="")
            ErrorWindow(text, self.child_window)

        else:
            if currency_1 == "PLN" or currency_1 == "EUR":
                price_1 = get_current_price(currency_2 + currency_1)
                price_1 = str(price_1)
                price_1 = price_1 + " " + currency_1
                print("pln eur valid")
                self.price_1.config(text=price_1)
                text = "Aktualny kurs " + currency_2 + " na " + currency_1
                self.crypto_name.config(text=text)

            elif currency_1 == "BTC" and currency_2 == "ETH":
                 price_1 = get_current_price(currency_2+currency_1)
                 price_1 = str(price_1)
                 price_1 = price_1 + " " + currency_2
                 print("btc eth valid")
                 self.price_1.config(text=price_1)
                 text = "Aktualny kurs " + currency_2 + " na " + currency_1
                 self.crypto_name.config(text=text)

            else:
                text = "Aktualny kurs " + currency_1 + " na " + currency_2
                self.crypto_name.config(text=text)
                price_1 = get_current_price(currency_1+currency_2)
                price_1 = str(price_1)
                price_1 = price_1 + " " + currency_2
                self.price_1.config(text=price_1)

        print(currency_1)
        print("___")
        print(currency_2)

    def exchange_currency(self, wallet, state1, state2):

        amount = self.amount_entry.get()

        if amount == "":
            ErrorWindow("Pole wartosci nie moze byc puste ", self.child_window)

        else:
            amount = float(amount)

            wallet_instance = load_wallet(wallet)

            currency_1 = state1.get()
            currency_2 = state2.get()

            if currency_1 != currency_2:

                print(f"Wymiana {amount} {currency_1} na {currency_2}")
                print(currency_1)
                print("___")
                print(currency_2)

                # PLN ----------------------------------------------------------------------------------------------------------

                if currency_1 == "BTC" and currency_2 == "PLN":
                    Wallet.BTC_to_PLN(wallet_instance, amount)
                    save_wallet(wallet, wallet_instance)


                if currency_1 == "ETH" and currency_2 == "PLN":
                    Wallet.ETH_to_PLN(wallet_instance, amount)
                    save_wallet(wallet, wallet_instance)

                if currency_1 == "PLN" and currency_2 == "BTC":
                    Wallet.PLN_to_BTC(wallet_instance, amount)


                if currency_1 == "PLN" and currency_2 == "ETH":
                    Wallet.PLN_to_ETH(wallet_instance, amount)
                    save_wallet(wallet, wallet_instance)

                # EUR ----------------------------------------------------------------------------------------------------------

                if currency_1 == "EUR" and currency_2 == "BTC":
                    Wallet.EUR_to_BTC(wallet_instance, amount)
                    save_wallet(wallet, wallet_instance)

                if currency_1 == "EUR" and currency_2 == "ETH":
                    Wallet.EUR_to_ETH(wallet_instance, amount)
                    save_wallet(wallet, wallet_instance)

                if currency_1 == "BTC" and currency_2 == "EUR":
                    Wallet.BTC_to_EUR(wallet_instance, amount)
                    save_wallet(wallet, wallet_instance)

                if currency_1 == "ETH" and currency_2 == "EUR":
                    Wallet.ETH_to_EUR(wallet_instance, amount)
                    save_wallet(wallet, wallet_instance)

                # crpyto to crypto -------------------------------------------------------------------------------------

                if currency_1 == "ETH" and currency_2 == "BTC":
                    Wallet.ETH_to_BTC(wallet_instance, amount)
                    save_wallet(wallet, wallet_instance)

                if currency_1 == "BTC" and currency_2 == "ETH":
                    Wallet.BTC_to_ETH(wallet_instance, amount)
                    save_wallet(wallet, wallet_instance)

                self.child_window.destroy()

            else:
                print("currency1 == currency2")
    def exit_window(self):
        self.child_window.destroy()





    # def show(self):
    #     return self.click_ok
