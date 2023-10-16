from sys import exit
from random import choice
import os
from time import sleep

# DESKTOP_DIR = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
DESKTOP_DIR = "./dev/desktop"
# INSTALL_DIR = "C:\\AxelNT_2023"
INSTALL_DIR = "./dev/axelnt_2023"
SHORTCUT_PATH = os.path.join(DESKTOP_DIR, "Iniciar AxelNT 2023.lnk")


def clear():
    os.system("cls")


def copy_shorcut():
    with open("InstallerFiles\\shortcut.lnk", "rb") as source:
        with open(SHORTCUT_PATH, "wb") as target:
            target.write(source.read())
    return "Escrito en " + SHORTCUT_PATH


def select_hostname():
    hostname_options = [
        "Alaska-ANT",
        "Ibiza-ANT",
        "Playa-ANT",
        "Desierto-ANT",
        "Texas-ANT",
        "Denver-ANT",
        "Madrid-ANT",
        "Bilbao-ANT",
        "Portugal-ANT",
        "España-ANT",
        "Terminator-ANT",
        "Europa-ANT",
        "Kaka-ANT",
        "Pepe-ANT",
    ]
    hostname_option_1 = choice(hostname_options)
    hostname_options.remove(hostname_option_1)
    hostname_option_2 = choice(hostname_options)
    hostname_options.remove(hostname_option_2)
    hostname_option_3 = choice(hostname_options)
    hostname_options.remove(hostname_option_3)
    options = [hostname_option_1, hostname_option_2, hostname_option_3]
    not_valid = True
    while not_valid:
        try:
            clear()
            option = input(
                "¿Que nombre quieres ponerle al ordenador?\n1) "
                + hostname_option_1
                + "\n2) "
                + hostname_option_2
                + "\n3) "
                + hostname_option_3
                + "\n> "
            )
            option_num = int(option)
            assert option_num < 4
            not_valid = False
        except:
            print("¡El numero no es valido!, ¡Vuelve a intentarlo!")
            sleep(2.5)
    selected = options[option_num - 1]
    print("Has elegido: " + selected)
    return selected

def ask_license():
    print("Introduce tu licencia")
    license = input("> ").lower()
    try:
        if license[0] not in ["a", "d", "g", "j", "m", "p", "s", "y", "1", "2", "4", "8", "9"]:
            return {"status": "invalid", "valid": False, "license": license}
        if license[1] not in ["b", "e", "h", "k", "n", "q", "t", "z", "2", "5", "8", "0"]:
            return {"status": "invalid", "valid": False, "license": license}
        if license[2] not in ["b", "e", "h", "k", "n", "q", "t", "z", "2", "5", "8", "0"]:
            return {"status": "invalid", "valid": False, "license": license}
        if license[3] not in ["a", "b", "c", "d", "f", "1", "2", "4", "5", "7", "8"]:
            return {"status": "invalid", "valid": False, "license": license}
        if license[4] not in ["a", "b", "c", "d", "f", "1", "2", "4", "5", "7", "8"]:
            return {"status": "invalid", "valid": False, "license": license}
        return {"status": "Correct", "valid": True, "license": license}
    except:
        return {"status": "invalid", "valid": False, "license": license}
def installer():
    print(
        f"""
=====================
AxelNT 2023 Installer
El sistema se instalara en {INSTALL_DIR} y dejara un acceso directo en el escritorio

"""
    )
    print(
        f"""
========================
PASO 1: Elegir un nombre
========================
"""
    )
    hostname = select_hostname()
    print(
        f"""
===============================
PASO 2: Introducir una licencia
===============================
"""
    )
    license = ask_license()

    print(license)

installer()