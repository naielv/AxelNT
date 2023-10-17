import os
import sys
def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
#clear()
def axelnt():
    print("¡Funciona!")
    input("Pulsa intro para salir.")