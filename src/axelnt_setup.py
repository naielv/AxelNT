import os
import sys
import subprocess
import importlib
from getpip import main as install_pip

def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
def install_package(name):
    print("Instalando Dependencia: " + name)
    
    if sys.platform == "win32":
        subprocess.check_call(['Python/Scripts/pip.exe', 'install', name])
    else:
        subprocess.check_call(['pip3', 'install', name])
    clear()
clear()
def setup():
    print("¡Necesitas una conexion de internet para continuar!")
    input("Pulsa intro si tu dispositivo esta conectado al internet\nCtrl-C para salir.\n")
    if sys.platform == "win32":
        clear()
        print("Instalando Dependencia: Pip")
        install_pip()
        clear()
    install_package("pytermgui")
    importlib.__import__("axelnt_installer").start_installer()