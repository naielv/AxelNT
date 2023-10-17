import os
import sys
import subprocess
from axelnt_installer import start_installer
from getpip import main as install_pip
def install_package(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])

def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
##clear()
def setup():
    print("¡Necesitas una conexion de internet para continuar!")
    input("Pulsa intro para continuar, Ctrl-C para salir.")
    if sys.platform == "win32":
        install_pip()
        install_package("windows-curses")
    start_installer()