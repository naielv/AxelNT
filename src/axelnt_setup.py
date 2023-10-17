import os
import sys
import subprocess
import importlib
from getpip import main as install_pip
def install_package(name):
    subprocess.check_call(['Python/Scripts/pip.exe', 'install', name])

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
    importlib.__import__("axelnt_installer").start_installer()