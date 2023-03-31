import tkinter
from src.dirtectory_operator import ERROR_IMG

from src.wallet_schema import Wallet,\
    empty_wallet_data, get_current_price

from src.gui.error_window import ErrorWindow
from src.gui.exchange_window import ExangeWindow
from src.gui.create_wallet_window import Create_wallet_window
from src.gui.wallet_window import WalletWindow
from src.dirtectory_operator import MAIN_BG_IMG

root = tkinter.Tk()
root.geometry('640x427')

background_image = tkinter.PhotoImage(file=MAIN_BG_IMG)
canvas = tkinter.Canvas(root, width=640, height=427)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")


wallet = 'wallet.pkl'


b1 = tkinter.Button(root, text="Stwórz portfel", command=lambda: Create_wallet_window(root), bd=1, width=10, height=2)
b1.place(x=0, y=0)

b2 = tkinter.Button(root, text="Pokaz portfel", command=lambda: WalletWindow(root), bd=1, width=10, height=2)
b2.place(x=100, y=0)

btc_price =get_current_price("BTCPLN")

b3 = tkinter.Button(root, text="Wymiana", command=lambda: ExangeWindow(root, wallet), bd=1, width=10, height=2)
b3.place(x=200, y=0)

root.mainloop()