from pathlib import Path
import os


BASE_DIR = Path(__file__).absolute().parent


GUI_IMAGE = os.path.join(BASE_DIR, "gui_img")

#  ---------------------------------------------------------------------------------------------------------------------

ERROR_IMG = os.path.join(GUI_IMAGE, "error.png")

BG_CHILD_WINDOW = os.path.join(GUI_IMAGE, "child_window_bg.png")

OK_BUTTON_IMG = os.path.join(GUI_IMAGE, "OK_button.png")

EXIT_BUTTON_IMG = os.path.join(GUI_IMAGE, "power.png")

EXCHANGE_BUTTON_IMG = os.path.join(GUI_IMAGE, "exchange.png")

REFRESH_BUTTON_IMG = os.path.join(GUI_IMAGE, "refresh.png")

CREATE_BUTTON_IMG = os.path.join(GUI_IMAGE, "create.png")

MAIN_BG_IMG = os.path.join(GUI_IMAGE, "bg_wallet.png")

EXCHANGE_BG = os.path.join(GUI_IMAGE, "bg_exchange.jpg")

WALLET_BG = os.path.join(GUI_IMAGE, "wallet.png")

CREATE_BG = os.path.join(GUI_IMAGE, "create_bg.png")

BUY_IMG = os.path.join(GUI_IMAGE, "buy.png")

BGBG = os.path.join(GUI_IMAGE, "bgbg.png")


print(CREATE_BG)