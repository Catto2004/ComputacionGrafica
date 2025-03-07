# Computación Grafica: Taller N.#: ##### en Python by JDRB
import os
import random

# ############ Variables Globales
Cabecera = """
\033[1;33m    Computación Gráfica:\033[0m\033[33m Taller N.#: ##### en Python. \033[0m
\033[3m    By Juan Diego Ruiz B. \033[0m
"""
Gato = """\033[93m             ^~^  ,
            ('Y') )
            /   \/
           (\|||/)\033[0m  
"""
Mensajes = [
    "¡Adios!",
    "さようなら!",
    "Good Bye!",
    "Tschüss!",
    "Ciao!",
    "Au Revoir!",
    "Увидимся!",
    "안녕히 가세요!",
    "再见!",
    "Γεια σου!",
    "Sometimes goodbye is a second chance!",
    "Auf Wiedersehen!",
    "Hurrengo arte!",
    "Feliz Jueves!"
]

# ############ Funciones Varias
def Adios():
    os.system("cls")
    print("")
    print("\033[1m")
    print(f"           {random.choice(Mensajes)}\033[0m")
    print("        -----v------------")
    print(Gato)
    print("\n\n\n\n\n")
    exit()

def Error():
    print("\n\033[1;31m    Error: Opción no válida.\a\033[0m")
    input("\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

# ############ Función Menú
def Menu():
    Salida = False
    while not Salida:

        os.system("cls")
        print(Cabecera)
        print(Gato)

        print("Opciones:")
        print("\033[1;33m1.\033[0m #####.")
        print("\033[1;31m4.\033[0m Salir.")
        opt = int(input("\n Ingrese una opción: "))

        if opt == 1:
            pass
        elif opt == 4:
            Salida = True
            Adios()
        else:
            Error()


# ############ Ejecución
Menu()