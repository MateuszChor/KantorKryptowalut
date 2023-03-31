from PIL import Image, ImageEnhance, ImageTk
import tkinter as tk
from typing import Union


def change_brightness_on_hover(widget: Union[tk.Button, tk.Canvas], img_path: str = "",
                               bg_color: str = "#4b83d2", factor: float = 1):
    """
    Adjusts tkinter.Button's image brightness.
    By adjusting the factor you can brighten or darken the image.
    factor = 0 -> makes image black
    factor = 1 -> gives original image
    factor > 1 -> brightens the image
    factor < 1 -> darkens the image
    :param widget: tkinter Button
    :param img_path: path to the image for button
    :param bg_color:
    :param factor: brightness factor
    """

    if isinstance(widget, (tk.Button,)) and img_path != "":
        # read the image
        img = Image.open(img_path)

        # create enhancer for the image
        enhancer = ImageEnhance.Brightness(img)

        # enhance the image brightness, by the required factor
        output_img = enhancer.enhance(factor)

        # PhotoImage class is used to add image to widgets
        original_img = ImageTk.PhotoImage(img)
        changed_img = ImageTk.PhotoImage(output_img)

        # set image on entering widget
        widget.bind("<Enter>", func=lambda f: widget.config(image=changed_img))

        # set image on leaving widget
        widget.bind("<Leave>", func=lambda f: widget.config(image=original_img))

    elif isinstance(widget, (tk.Canvas,)) and img_path == "":
        widget.config(bg=bg_color)