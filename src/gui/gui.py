import tkinter
from src.dirtectory_operator import ERROR_IMG

from src.wallet_schema import Wallet,\
    empty_wallet_data, get_current_price

from src.gui.error_window import ErrorWindow
from src.gui.exchange_window import ExangeWindow
from src.gui.create_wallet_window import Create_wallet_window
from src.gui.wallet_window import WalletWindow
from src.dirtectory_operator import MAIN_BG_IMG, EXCHANGE_MONEY_IMG, SHOW_WALLET_IMG, CREATE_WALLET_IMG

root = tkinter.Tk()
root.geometry('640x427')
root.title("Kantor Kryptowalut")

background_image = tkinter.PhotoImage(file=MAIN_BG_IMG)
canvas = tkinter.Canvas(root, width=640, height=427)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")


wallet = 'wallet.pkl'

#0000FF



create_wallet_img = tkinter.PhotoImage(file=CREATE_WALLET_IMG)
b1 = tkinter.Button(root,
                    image= create_wallet_img,
                    highlightthickness=0,
                    borderwidth=0,
                    activebackground="#0000FF",
                    activeforeground="#0000FF",
                    command=lambda: Create_wallet_window(root))
b1.place(x=80, y=50)


show_wallet_img = tkinter.PhotoImage(file=SHOW_WALLET_IMG)
b2 = tkinter.Button(root,
                    image=show_wallet_img,
                    highlightthickness=0,
                    borderwidth=0,
                    activebackground="#0000FF",
                    activeforeground="#0000FF",
                    command=lambda: WalletWindow(root),
                    bd=0)
b2.place(x=80, y=150)


exchange_button_img = tkinter.PhotoImage(file=EXCHANGE_MONEY_IMG)
b3 = tkinter.Button(root,
                    image=exchange_button_img,
                    highlightthickness=0,
                    borderwidth=0,
                    activebackground="#0000FF",
                    activeforeground="#0000FF",
                    text="Wymiana", command=lambda: ExangeWindow(root, wallet),
                    bd=1)
b3.place(x=380, y=150)

root.mainloop()