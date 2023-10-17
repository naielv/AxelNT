import os
import sys
sys.path.append(os.getcwd())
from axelnt import axelnt
from axelnt_setup import setup
def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
##clear()
def boot_if_installed():
    if os.path.isfile("./UserData/System/setup_ended"):
        axelnt()
    else:
        setup()

boot_if_installed()