import tkinter
import tkinter as tk
from src.gui.child_window import ChildWindow
from src.dirtectory_operator import BG_CHILD_WINDOW, EXIT_BUTTON_IMG, CREATE_BUTTON_IMG, CREATE_BG,MAIN_BG_IMG, BGBG
from src.gui.error_window import ErrorWindow
from src.wallet_schema import Wallet,empty_wallet_data
from src.gui.button_on_hover import change_brightness_on_hover
class Create_wallet_window(ChildWindow):

    wallet_instance = None
    def __init__(self, master_window):
        ChildWindow.__init__(self, master_window)

        background_image = tk.PhotoImage(file=BGBG)
        self.canvas = tk.Canvas(self.child_window, width=512, height=512)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=background_image, anchor="nw")

        self.label = tk.Label(self.child_window,
                              bg="#ffffff",
                              text="Twoje imię to ?",
                              font="none 10 bold",
                              anchor=tk.CENTER)
        self.label.place(x=150, y=20)

        self.owner_entry = tkinter.Entry(self.child_window, width=15)
        self.owner_entry.place(x=150, y=100)

        create_img = tk.PhotoImage(file=CREATE_BUTTON_IMG)

        self.create_button = tk.Button(self.child_window,
                                image=create_img,
                                bg=self.background_color,
                                borderwidth=0,
                                activebackground=self.background_color,
                                activeforeground=self.background_color,
                                command=self.create_wallet_owner
                                )
        self.create_button.place(x=150, y=150,)

        exit_img = tk.PhotoImage(file=EXIT_BUTTON_IMG)

        self.exit_button = tk.Button(self.child_window,
                                     image=exit_img,
                                     bg=self.background_color,
                                     borderwidth=0,
                                     highlightbackground=self.background_color,
                                     activeforeground=self.background_color,
                                     command=self.exit_window
                                     )

        self.exit_button.place(x=372, y=5)

        change_brightness_on_hover(widget=self.create_button, img_path=CREATE_BUTTON_IMG, factor=1.15)
        self.child_window.wait_window()

    def create_wallet_owner(self):

        owner = self.owner_entry.get()

        if owner == "":
            ErrorWindow("Nazwa portfela nie może być pusta", self.child_window)

        else:

            Wallet.create_wallet(self, owner)
            self.child_window.destroy()

    def get_wallet_instance(self):
        return self.wallet_instance

    def exit_window(self):
        self.child_window.destroy()





