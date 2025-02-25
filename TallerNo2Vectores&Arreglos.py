import os
import math
import random
import numpy as np

Cabecera = """
\033[1;33m    Computación Gráfica:\033[0m\033[33m Taller N.2: Uso de Numpy en Python. \033[0m
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

# ############ Funciones de Lista

def FiltrarLista(Lista, Opcion):  # Opcion = 0 -> Pares, Opcion = 1 -> Impares
    ListaFiltrada = []
    for i in Lista:
        if i % 2 == Opcion:
            ListaFiltrada.append(i)
    return ListaFiltrada

def BuscarLista(Lista, Elemento):
    pass

def ConversorTemperaturaLista(Lista, Opcion):
    pass

def SistemaCalificaciones(Lista):
    pass

# ############ Funciones de Tuplas

def OrdenarTupla():
    pass

# ############ Funciones de la Agenda

Contactos = {

}

def MenuAgenda():
    pass

def MostrarContactos():
    pass

def AgregarContacto():
    pass

def BuscarContacto():
    pass

def EliminarContacto():
    pass

# ############ Funciones Contador, Validación Parentesis y Contraseñas

def ContadorLetras():
    pass

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

def MostrarVector(A, Nombre, Color):
    print(f"\033[{Color}m{Nombre}\033[0m = \033[{Color}m{A}\033[0m")

# ############ Menu Principal
def Menu():
    Salida = False
    while not Salida:

        os.system("cls")
        print(Cabecera)
        print(Gato)

        print("Opciones:")
        print("\033[1;33m1.\033[0m Conversor de Unidades.")
        print("\033[1;33m2.\033[0m Física.")
        print("\033[1;33m3.\033[0m Vectores.")
        print("\033[1;31m4.\033[0m Salir.")
        opt = int(input("\n Ingrese una opción: "))

        if opt == 1:
            pass
        elif opt == 2:
            pass
        elif opt == 3:
            pass
        elif opt == 4:
            Salida = True
            Adios()
        else:
            Error()


# ############ Ejecución
Menu()