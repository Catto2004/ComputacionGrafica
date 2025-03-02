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

# ############ Funciones de la Calculadora

def Sumar(A, B):
    return A + B

def Restar(A,B):
    return A - B

def Multiplicar(A, B):
    return A * B

def Dividir(A, B):
    return A / B

def MenuCalculadora():
    Salida = False
    A, B = None, None

    while not Salida:
        print(Cabecera)
        print("\033[1;32m    Calculadora Básica:\033[0m")


# ############ Funciones de Lista

def FiltrarLista(Lista, Opcion):  # Opcion = 0 -> Pares, Opcion = 1 -> Impares
    ListaFiltrada = []
    for i in Lista:
        if i % 2 == Opcion:
            ListaFiltrada.append(i)
    return ListaFiltrada

def BuscarLista(Lista, Elemento):
    for i in Lista:
        if i == Elemento:
            return True
    return False

def ConversorTemperaturaLista(Lista, Opcion): # Opcion = 0 -> C a F, Opcion = 1 -> F a C
    if Opcion == 0:   # C a F
        ListaConvertida = list(map(lambda c: c * 9/5 + 32, Lista))
    elif Opcion == 1: # F a C
        ListaConvertida = list(map(lambda f: (f - 32) * 5/9, Lista))

    return ListaConvertida

def SistemaCalificaciones(Lista): # A >= 4, B >= 3, C >= 2, D >= 1, F < 0
    ListaLetras = []
    for i in Lista:
        if i >= 90:
            ListaLetras.append("A")
        elif i >= 80:
            print(f"Calificación: {i} -> B")
        elif i >= 70:
            print(f"Calificación: {i} -> C")
        elif i >= 60:
            print(f"Calificación: {i} -> D")
        else:
            print(f"Calificación: {i} -> F")

# ############ Funciones de la Agenda

Contactos = {}

def MostrarContactos():
    if Contactos:
        print("\nLista de contactos:")
        for nombre, telefono in Contactos.items():
            print(f"{nombre}: {telefono}")
    else:
        print("\nNo hay contactos en la agenda.")
    input("Presione Enter para continuar...")

def AgregarContacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    Contactos[nombre] = telefono
    print(f"Contacto {nombre} agregado exitosamente.")
    input("Presione Enter para continuar...")

def BuscarContacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in Contactos:
        print(f"{nombre}: {Contactos[nombre]}")
    else:
        print("Contacto no encontrado.")
    input("Presione Enter para continuar...")

def EliminarContacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in Contactos:
        del Contactos[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado.")
    input("Presione Enter para continuar...")

def MenuAgenda():
    Salida = False
    while not Salida:
        os.system("cls")
        print(Cabecera)
        print("\033[1;32m    Agenda:\033[0m")
        print("\033[1;33m1.\033[0m Mostrar contactos")
        print("\033[1;33m2.\033[0m Agregar contacto")
        print("\033[1;33m3.\033[0m Buscar contacto")
        print("\033[1;33m4.\033[0m Eliminar contacto")
        print("\033[1;31m5.\033[0m Salir")
        try:
            opcion = ValidarEntero()
            if opcion == 1:
                MostrarContactos()
            elif opcion == 2:
                AgregarContacto()
            elif opcion == 3:
                BuscarContacto()
            elif opcion == 4:
                EliminarContacto()
            elif opcion == 5:
                print("Saliendo de la agenda...")
                Salida = True
            else:
                Error()
        except Exception:
            Error()

# ############ Funciones Contador, Validación Parentesis, Ordenamiento Tuplas y Contraseñas

def ContadorLetras(Cadena):
    Cadena = Cadena.lower()
    Palabras = Cadena.split()
    Contador = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
        "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
    }

    for palabra in Palabras:
        Contador[palabra] += 1

    return dict(sorted(Contador.items(), key=lambda item: item[1], reverse=True))

def ValidarParentesis(Cadena):
    contador = 0
    
    for caracter in Cadena:
        if caracter == '(':
            contador += 1
        elif caracter == ')':
            contador -= 1
        if contador < 0:
            return False
    
    return contador == 0

def OrdenarTuplas(ListaTuplas):
    return sorted(ListaTuplas, key=lambda x: x[1])

def GenerarContrasena(Longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    contrasena = ""
    for _ in range(Longitud):
        contrasena += random.choice(caracteres)
    return contrasena

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

def ValidarEntero():
    while True:
        try:
            Numero = int(input())
            return Numero
        except ValueError:
            print("\033[1;31m    Error: Ingrese un número entero.\a\033[0m")

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