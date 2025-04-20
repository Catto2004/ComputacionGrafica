# Computación Grafica: Taller N.3: Uso Basico de Numpy en Python by JDRB
import os
import random
import numpy as np

# ############ Variables Globales
Cabecera = """
\033[1;33m    Computación Gráfica:\033[0m\033[33m Taller N.3: Uso Basico de Numpy en Python. \033[0m
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

# ############ Funciones de Ejercicios

# Ejercicio 1
def Array1D():
    print("\nArray Unidimensional con los números del 1 al 10:")
    # Crear un array unidimensional con los números del 1 al 10.
    Array = np.arange(1, 11)
    # Imprime el array.
    print(f"\n\033[1;33mA\033[0m = \033[33m{Array}\033[0m")
    input("\n\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

# Ejercicio 2
def Array2D():
    print("\nMatriz 2D con 3 filas y 3 columnas:")
    # Crea una matriz 2D con 3 filas y 3 columnas, llenada con números del 1 al 9.
    Array = np.arange(1, 10).reshape(3, 3)
    # Imprime la matriz.
    print(f"\n\033[1;33mA\033[0m = \033[33m{Array}\033[0m")
    input("\n\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

# Ejercicio 3
def SumaArrays():
    print("\nSuma de dos Arrays: ")
    # Creacion de las dos matrices
    ArrayA = np.arange(1, 6)
    print(f"\n\033[1;33mA\033[0m = \033[33m{ArrayA}\033[0m")
    ArrayB = np.arange(1, 6)
    print(f"\n\033[1;33mB\033[0m = \033[33m{ArrayB}\033[0m")
    # Suma de los dos arrays y guardar el resultado en un nuevo array.
    ArrayC = ArrayA + ArrayB
    # Imprimir el resultado.
    print(f"\n\033[1;33mA + B\033[0m = \033[33m{ArrayC}\033[0m")
    input("\n\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

# Ejercicio 4
def ExponencialArray():
    print("\nExponencial de cada elemento del Array:")
    # Creción del array
    Array = np.arange(1, 6)
    print(f"\n\033[1;33mA\033[0m = \033[33m{Array}\033[0m")
    # Se calcula la exponencial de cada elemento
    ArrayExp = np.exp(Array)
    # Imprimir el nuevo array
    print(f"\n\033[1;33mexp(A)\033[0m = \033[33m{ArrayExp}\033[0m")
    input("\n\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

# Ejercicio 5
def ElementosPares():
    # Creación del array
    Array = np.arange(1, 11)
    print("\nElementos Pares del Array:")
    print(f"\n\033[1;33mA\033[0m = \033[33m{Array}\033[0m")
    # Seleccionar los elementos pares del array y guardar el resultado en un nuevo array.
    ArrayPares = np.where(Array % 2 == 0)
    # Imprimir el nuevo array
    print(ArrayPares)
    print(f"\n\033[1;33mA_pares\033[0m = \033[33m{Array}\033[0m")
    input("\n\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

# Ejercicio 6
def ArrayAleatorio():
    # Generar un array de 10 números aleatorios entre 0 y 1.
    Array = np.random.rand(10) # Donde 10 es el largo del array.
    # Imprimir el array.
    print("\nArray de 10 números aleatorios entre 0 y 1:")
    print(f"\n\033[1;33mA\033[0m = \033[33m{Array}\033[0m")
    input("\n\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

# Ejercicio 7
def MediaArray():
    print("\nMedia de los elementos del Array:")
    # Creacion del array
    Array = np.arange(1, 6)
    print(f"\n\033[1;33mA\033[0m = \033[33m{Array}\033[0m")
    # Calcular la media de los elementos del array.
    Media = np.mean(Array)
    # Imprimir la media.
    print(f"\n\033[1;33mMedia:\033[0m {Media}")
    input("\n\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

# Ejercicio 8
def ArrayFabrica():
    print("\nArray de 5 elementos, todos inicializados con el valor 7:")
    # Creación del array
    Array = np.full(5, 7) # Donde 5 es el largo del array y 7 es el valor de los elementos.
    # Imprimir el array.
    print(f"\n\033[1;33mA_7\033[0m = \033[33m{Array}\033[0m")
    input("\n\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

# Ejercicio 9
def Broadcasting():
    print("\nSuma de dos Arrays utilizando Broadcasting:")
    # Creación de los arrays
    ArrayA = np.arange(1, 4)
    print(f"\n\033[1;33mA\033[0m = \033[33m{ArrayA}\033[0m")
    ArrayB = np.arange(4, 7)
    print(f"\n\033[1;33mB\033[0m = \033[33m{ArrayB}\033[0m")
    # Suma de los dos arrays utilizando broadcasting y guardar el resultado en un nuevo array.
    ArrayC = ArrayA + ArrayB
    # Imprimir el nuevo array.
    print(f"\n\033[1;33mA + B\033[0m = \033[33m{ArrayC}\033[0m")
    input("\n\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

# Ejercicio 10
def RedimensionarArray():
    print("\nRedimensionar Array a una matriz 2x3:")
    # Creación del array
    Array = np.arange(1, 7)
    print(f"\n\033[1;33mA\033[0m = \033[33m{Array}\033[0m")
    # Cambiar la forma del array a una matriz 2x3.
    Array2D = Array.reshape(2, 3)
    # Imprimir la matriz.
    print(f"\n\033[1;33mA_redim\033[0m = \033[33m{Array2D}\033[0m")
    input("\n\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

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
        print("\033[1;33m1.\033[0m Creación de un array de 1D.")
        print("\033[1;33m2.\033[0m Creación de una matriz 2D.")
        print("\033[1;33m3.\033[0m Suma de dos arrays.")
        print("\033[1;33m4.\033[0m Exponencial de cada elemento del array.")
        print("\033[1;33m5.\033[0m Elementos pares del array.")
        print("\033[1;33m6.\033[0m Array de números aleatorios.")
        print("\033[1;33m7.\033[0m Media de los elementos del array.")
        print("\033[1;33m8.\033[0m Array de 5 elementos con valor 7.")
        print("\033[1;33m9.\033[0m Broadcasting.")
        print("\033[1;33m10.\033[0m Redimensionar array.")
        print("\033[1;31m11.\033[0m Salir.")
        opt = int(input("\n Ingrese una opción: "))

        if opt == 1:
            Array1D()
        elif opt == 2:
            Array2D()
        elif opt == 3:
            SumaArrays()
        elif opt == 4:
            ExponencialArray()
        elif opt == 5:
            ElementosPares()
        elif opt == 6:
            ArrayAleatorio()
        elif opt == 7:
            MediaArray()
        elif opt == 8:
            ArrayFabrica()
        elif opt == 9:
            Broadcasting()
        elif opt == 10:
            RedimensionarArray()
        elif opt == 11:
            Salida = True
            Adios()
        else:
            Error()


# ############ Ejecución
Menu()