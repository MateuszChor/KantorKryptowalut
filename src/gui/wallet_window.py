import tkinter as tk
from src.dirtectory_operator import BG_CHILD_WINDOW, EXIT_BUTTON_IMG, WALLET_BG, BUY_IMG, REFRESH_BUTTON_IMG
from src.gui.child_window import ChildWindow
from src.gui.button_on_hover import change_brightness_on_hover
from src.load_wallet import load_wallet, save_wallet


class WalletWindow(ChildWindow):
    def __init__(self, master_window):
        ChildWindow.__init__(self, master_window)
        background_image = tk.PhotoImage(file=BG_CHILD_WINDOW)
        self.canvas = tk.Canvas(self.child_window, width=400, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=background_image, anchor="nw")

        
        wallet = load_wallet('wallet.pkl')

        print(wallet)

        self.label_owner1 = tk.Label(self.child_window,
                              bg=self.background_color,
                              text=wallet.owner,
                              font="none 10 bold",
                              anchor=tk.CENTER)
        self.label_owner1.place(x=200, y=40)

        self.label_owner = tk.Label(self.child_window,
                                    bg=self.background_color,
                                    text="Właściciel :",
                                    font="none 10 bold",
                                    anchor=tk.CENTER)
        self.label_owner.place(x=50, y=40)

        self.label_PLN1 = tk.Label(self.child_window,
                              bg=self.background_color,
                              text=wallet.PLN_amount,
                              font="none 10 bold",
                              anchor=tk.CENTER)
        self.label_PLN1.place(x=200, y=80)

        self.label_PLN = tk.Label(self.child_window,
                                   bg=self.background_color,
                                   text="ilość PLN :",
                                   font="none 10 bold",
                                   anchor=tk.CENTER)
        self.label_PLN.place(x=50, y=80)

        self.label_EUR1 = tk.Label(self.child_window,
                                  bg=self.background_color,
                                  text=wallet.EUR_amount,
                                  font="none 10 bold",
                                  anchor=tk.CENTER)
        self.label_EUR1.place(x=200, y=120)

        self.label_EUR = tk.Label(self.child_window,
                                   bg=self.background_color,
                                   text="ilość EUR",
                                   font="none 10 bold",
                                   anchor=tk.CENTER)
        self.label_EUR.place(x=50, y=120)

        self.label_BTC = tk.Label(self.child_window,
                                  bg=self.background_color,
                                  text="ilość BTC :",
                                  font="none 10 bold",
                                  anchor=tk.CENTER)
        self.label_BTC.place(x=50, y=160)

        self.label_BTC1 = tk.Label(self.child_window,
                                  bg=self.background_color,
                                  text=wallet.BTC_amount,
                                  font="none 10 bold",
                                  anchor=tk.CENTER)
        self.label_BTC1.place(x=200, y=160)

        self.label_ETH1 = tk.Label(self.child_window,
                                  bg=self.background_color,
                                  text=wallet.ETH_amount,
                                  font="none 10 bold",
                                  anchor=tk.CENTER)
        self.label_ETH1.place(x=200, y=200)

        self.label_ETH = tk.Label(self.child_window,
                                  bg=self.background_color,
                                  text="ilość ETH",
                                  font="none 10 bold",
                                  anchor=tk.CENTER)
        self.label_ETH.place(x=50, y=200)

        refresh_img = tk.PhotoImage(file=REFRESH_BUTTON_IMG)

        self.refresh_button = tk.Button(self.child_window,
                                        image=refresh_img,
                                        bg=self.background_color,
                                        borderwidth=0,
                                        highlightthickness=0,
                                        activebackground=self.background_color,
                                        activeforeground=self.background_color,
                                        command=self.refresh_price)
        self.refresh_button.place(x=50, y=350)

        exit_img = tk.PhotoImage(file=EXIT_BUTTON_IMG)

        self.exit_button = tk.Button(self.child_window,
                                     image=exit_img,
                                     bg=self.background_color,
                                     borderwidth=0,
                                     highlightbackground=self.background_color,
                                     activeforeground=self.background_color,
                                     command=self.exit_window
                                     )

        self.exit_button.place(x=374, y=4)

        buy_img = tk.PhotoImage(file=BUY_IMG)

        self.buy_button = tk.Button(self.child_window,
                                     image=buy_img,
                                     bg=self.background_color,
                                     borderwidth=0,
                                     highlightbackground=self.background_color,
                                     activeforeground=self.background_color,
                                     command=lambda: self.add_PLN(wallet)
                                     )

        self.buy_button.place(x=300, y=350)

        change_brightness_on_hover(widget=self.exit_button, img_path=EXIT_BUTTON_IMG, factor=1.15)

        self.child_window.wait_window()

    def add_PLN(self, wallet):
        wallet.PLN_amount += 5000
        print(wallet)
        save_wallet('wallet.pkl', wallet)

    def refresh_price(self):
        wallet = load_wallet('wallet.pkl')
        pln = wallet.PLN_amount
        eur = wallet.EUR_amount
        btc = wallet.BTC_amount
        eth = wallet.ETH_amount

        self.label_PLN1.config(text=pln)
        self.label_EUR1.config(text=eur)
        self.label_ETH1.config(text=eth)
        self.label_BTC1.config(text=btc)

    def exit_window(self):
        self.child_window.destroy()
