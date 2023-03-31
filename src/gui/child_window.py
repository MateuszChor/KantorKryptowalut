import tkinter as tk


class ChildWindow:
    def __init__(self, master_window):
        width = 400
        height = 400
        self.background_color = "gray"
        self.child_window = tk.Toplevel(master_window)
        self.child_window.geometry('{}x{}+{}+{}'.format(width, height, 320, 200))
        self.child_window.resizable(False, False)
        self.child_window.overrideredirect(1)

