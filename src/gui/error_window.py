import tkinter as tk
from src.dirtectory_operator import ERROR_IMG, BG_CHILD_WINDOW, OK_BUTTON_IMG
from src.gui.child_window import ChildWindow
from src.gui.button_on_hover import change_brightness_on_hover


class ErrorWindow(ChildWindow):
    def __init__(self, content: str, master_window):
        ChildWindow.__init__(self, master_window)

        self.click_ok = False
        background_image = tk.PhotoImage(file=BG_CHILD_WINDOW)
        self.canvas = tk.Canvas(self.child_window, width=400, height=200)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=background_image, anchor="nw")

        i = tk.PhotoImage(file=ERROR_IMG)
        self.error_image = tk.Label(self.child_window,
                                    image=i,
                                    bg=self.background_color)
        self.error_image.place(x=20, y=20)

        self.label = tk.Label(self.child_window,
                              bg=self.background_color,
                              text=content,
                              font="none 10 bold",
                              anchor=tk.CENTER)
        self.label.place(x=130, y=40)

        ok_image = tk.PhotoImage(file=OK_BUTTON_IMG)

        self.ok_button = tk.Button(self.child_window,
                                   image=ok_image,
                                   bg=self.background_color,
                                   borderwidth=0,
                                   highlightthickness=0,
                                   activebackground=self.background_color,
                                   activeforeground=self.background_color,
                                   command=self.ok_action)
        self.ok_button.place(x=310, y=140)

        change_brightness_on_hover(widget=self.ok_button, img_path=OK_BUTTON_IMG, factor=1.15)

        self.child_window.wait_window()

    def ok_action(self):
        self.click_ok = True
        self.child_window.destroy()

    def show(self):
        return self.click_ok
