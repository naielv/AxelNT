import os
from axelnt import axelnt
from axelnt_setup import setup
def clear():
    os.system("cls")

def boot_if_installed():
    if os.path.isfile("./UserData/System/setup_ended"):
        axelnt()
    else:
        setup()
print("Version de prueba, falta el codigo base.")
input("Pulsa cualquier tecla para salir.")