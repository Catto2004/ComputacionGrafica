# Computación Grafica: Taller N.1: Fisica Computacional en Python by JDRB
import math
import os
import random

# ############ Variables Globales
Altura    = 0
Gravedad  = 0
Tiempo    = 0
Velocidad = 0
Angulo    = 0
Distancia = 0

Cabecera = """
\033[1;33m    Computación Gráfica:\033[0m\033[33m Taller N.1: Física Computacional en Python. \033[0m
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

# ############ Gráficos
GraficoAngulo = """
            \033[1;33mRadianes\033[0m \033[1;31m<\033[0m------------\033[1;31m>\033[1;33m Grados\033[0m
"""
GraficoVelocidad = """
                 \033[1;33mm/s\033[0m \033[1;31m<\033[0m------------\033[1;31m>\033[1;33m km/h\033[0m
"""
GraficoCaida = f"""
"""
GraficoDesplazamiento = f"""
"""
GraficoProyectil = f"""
"""
GraficoVectores = """
              \033[1;31mA →
             ^
            /   
           /    
          /     
         /      
        \033[0m*\033[1;34m--------> 
                  B →\033[0m
"""

# ############ Funciones Conversoras
def ConvertirAngulos(Angulo, opt):
    if opt == 1: return math.radians(Angulo)
    else: return math.degrees(Angulo)

def ConvertirVelocidad(Velocidad, opt):
    if opt == 1: return Velocidad * 3.6
    else: return Velocidad / 3.6

# ############ Funciones Fisicas
def CaidaLibre():
    if Gravedad <= 0 or Altura <= 0:
        print("\033[1;31m Error: La gravedad no puede ser 0 y/o la altura no puede ser negativa.\033[0m")
        input("\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")
    else:
        return round(math.sqrt(2 * Altura / Gravedad), 2)

def Desplazamiento():
    if Tiempo <= 0 or Gravedad <= 0:
        print("\033[1;31m Error: El tiempo y/o la aceleración no pueden ser 0 y/o negativos.\033[0m")
        input("\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")
    else:
        return round(Velocidad * Tiempo + 0.5 * Gravedad * Tiempo ** 2, 2)

def LanzamientoProyectil():
    if Velocidad <= 0 or Angulo <= 0 or Gravedad <= 0 or Altura <= 0:
        print("\033[1;31m Error: La velocidad, el ángulo, la gravedad y/o la altura no pueden ser 0 y/o negativos.\033[0m")
        input("\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")
    else:
        return round((Velocidad ** 2 * math.sin(2 * math.radians(Angulo)) / Gravedad), 2)

# ############ Funciones Vectores
def SumaVectores(A, B):
    if len(A) != len(B): 
        print ("\033[1;31m Error: Los vectores deben tener la misma dimensión/Largo.\033[0m")
        input("\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")
    else: 
        return [A[i] + B[i] for i in range(len(A))]

def ProductoPunto(A,  B, opt):
    if len(A) != len(B) and opt == 0:
        print ("\033[1;31m Error: Los vectores deben tener la misma dimensión/Largo.\033[0m")
        input("\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

    elif len(A) != len(B) and opt == 1:
        return 0
    
    else:
        return sum([A[i] * B[i] for i in range(len(A))])

def MagnitudVector(A):
    if len(A) == 0:
        return None
    else:
        return round(math.sqrt(sum([A[i] ** 2 for i in range(len(A))])), 2)

def AnguloVectores(A, B):
    if len(A) != len(B):
        return None
    elif MagnitudVector(A) == 0 or MagnitudVector(A) == None or MagnitudVector(B) == 0 or MagnitudVector(B) == None:
        return None
    else:
        return round(math.acos(ProductoPunto(A, B, 1) / (MagnitudVector(A) * MagnitudVector(B))), 2)
    
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
          
def MostrarMagnitud(A, Nombre, Color):
    print(f"|\033[{Color}m{Nombre}\033[0m| = \033[{Color}m{MagnitudVector(A)}\033[0m")

def ReiniciarPropiedades():
    global Altura, Gravedad, Tiempo, Velocidad, Angulo, Distancia
    Altura    = 0
    Gravedad  = 0
    Tiempo    = 0
    Velocidad = 0
    Angulo    = 0
    Distancia = 0

def ActualizarGraficas():
    global GraficoCaida, GraficoDesplazamiento, GraficoProyectil
    GraficoCaida = f"""    | 
    |   \033[1;31m●\033[0m <- \033[3mh = {Altura} m\033[0m
    |   ↓  
    |   \033[3mg = {Gravedad} m/s²\033[0m 
    |     
    |  
    |___________________________

\033[3;33m    t = {Tiempo} s\033[0m
"""
    GraficoDesplazamiento = f"""                                \033[3mv = {Velocidad} m/s\033[0m
                                \033[3ma = {Gravedad} m/s²\033[0m
                                \033[3mt = {Tiempo} s\033[0m
      \033[1;31m●\033[0m   ------------>   \033[1;32m●\033[0m  ←  \033[3;33md = {Distancia} m\033[0m
------+-------------------+-----
"""
    GraficoProyectil = f"""              \033[33m_ \033[1;34m● \033[0m\033[33m_\033[0m             \033[3;34mH = {Altura} m\033[0m
            \033[33m.       .\033[0m           \033[3mv = {Velocidad} m/s\033[0m
          \033[33m/           \\\033[0m         \033[3ma = {Angulo} °\033[0m
        \033[1;31m●               \033[1;32m●\033[0m       \033[3mg = {Gravedad} m/s²\033[0m
--------+---------------+------
                        \033[3;32mX = {Distancia}\033[0m
"""

# ############ Funciones SubMenus
def MenuUnidades():
    Exit = False
    while not Exit:
        os.system("cls")
        print(Cabecera)
        print(GraficoAngulo)
        print(GraficoVelocidad)
        print("\033[1;32m    Conversor de Unidades:\033[0m")
        print("Opciones: \n")
        print("\033[1;33m1.\033[0m Angulos.")
        print("\033[1;33m2.\033[0m Velocidad.")
        print("\033[1;31m3.\033[0m Volver.")
        opt = int(input(" \nIngrese una opción: "))

        if opt == 1:
            SubExit = False
            while not SubExit:
                os.system("cls")
                print(Cabecera)
                print(GraficoAngulo)
                print("\033[1;32m    Conversor de Unidades:\033[0m")
                print("\033[1;34m  Angulos:\033[0m")
                print("Opciones:")
                print("\033[1;33m1.\033[0m Grados a Radianes.")
                print("\033[1;33m2.\033[0m Radianes a Grados.")
                print("\033[1;31m3.\033[0m Volver.")

                opt = int(input("\n Ingrese una opción: "))
                if opt == 3: break
                Angulo = float(input(" Ingrese el ángulo: "))

                if opt == 1: tipo = "Radianes"
                else: tipo = "Grados"
                Resultado = ConvertirAngulos(Angulo, opt)

                print(f"Resultado: \033[33m{Resultado} {tipo}\033[0m")
                input("\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

        elif opt == 2:
            SubExit = False
            while not SubExit:
                os.system("cls")
                print(Cabecera)
                print(GraficoVelocidad)
                print("\033[1;32m    Conversor de Unidades:\033[0m")
                print("\033[1;34m  Velocidad:\033[0m")
                print("Opciones:")
                print("\033[1;33m1.\033[0m m/s a km/h.")
                print("\033[1;33m2.\033[0m km/h a m/s.")
                print("\033[1;31m3.\033[0m Volver.")

                opt = int(input("\n Ingrese una opción: "))
                if opt == 3: break
                Velocidad = float(input(" Ingrese la velocidad: "))
                if opt == 1: tipo = "km/h"
                else: tipo = "m/s"
            
                Resultado = ConvertirVelocidad(Velocidad, opt)
                print(f"Resultado: \033[33m{Resultado} {tipo}\033[0m")
                input("\033[3m    Presione \033[1mEnter\033[0m\033[3m para continuar...\033[0m")

        elif opt == 3:
            Exit = True

        else:
            Error()

def MenuFisica():
    global Altura, Gravedad, Tiempo, Velocidad, Angulo, Distancia
    Exit = False
    while not Exit:
        os.system("cls")
        print(Cabecera)
        print("\033[1;32m    Calculadora de Fisica:\033[0m")
        print("Opciones: \n")
        print("\033[1;33m1.\033[0m Caida Libre.")
        print("\033[1;33m2.\033[0m Desplazamiento.")
        print("\033[1;33m3.\033[0m Lanzamiento de Proyectil.")
        print("\033[1;31m4.\033[0m Volver.")

        opt = int(input(" \nIngrese una opción: "))

        # Menú Caida Libre
        if opt == 1:
            ReiniciarPropiedades()
            Gravedad = 9.81
            SubExit = False
            while not SubExit:
                if Altura != 0 and Gravedad != 0:
                    Tiempo = CaidaLibre()
                
                os.system("cls")
                print(Cabecera)
                ActualizarGraficas()
                print(GraficoCaida)
                print("\033[1;32m    Calculadora de Fisica:\033[0m")
                print("\033[1;34m  Caida Libre:\033[0m")
                print("Opciones: \n")
                print("\033[1;33m1.\033[0m Cambiar Altura.")
                print("\033[1;33m2.\033[0m Cambiar Gravedad.")
                print("\033[1;31m3.\033[0m Volver.")

                opt = int(input(" \nIngrese una opción: "))

                if opt == 1:   
                    Altura = float(input("\n Ingrese la altura: "))
                elif opt == 2: 
                    Gravedad = float(input("\n Ingrese la gravedad: "))
                elif opt == 3: 
                    SubExit = True
                else: Error()   
        
        # Menú Desplazamiento
        elif opt == 2:
            ReiniciarPropiedades()
            SubExit = False
            while not SubExit:
                if Gravedad != 0 and Tiempo != 0:
                    Distancia = Desplazamiento()

                os.system("cls")
                print(Cabecera)
                ActualizarGraficas()
                print(GraficoDesplazamiento)
                print("\033[1;32m    Calculadora de Fisica:\033[0m")
                print("\033[1;34m  Desplazamiento:\033[0m")
                print("Opciones: \n")
                print("\033[1;33m1.\033[0m Cambiar Velocidad inicial.")
                print("\033[1;33m2.\033[0m Cambiar Aceleración.")
                print("\033[1;33m3.\033[0m Cambiar Tiempo.")
                print("\033[1;31m4.\033[0m Volver.")

                opt = int(input(" \nIngrese una opción: "))
                
                if opt == 1:
                    Velocidad = float(input("\n Ingrese la velocidad inicial: "))
                elif opt == 2:
                    Gravedad = float(input("\n Ingrese la aceleración: "))
                elif opt == 3:
                    Tiempo = float(input("\n Ingrese el tiempo: "))
                elif opt == 4:
                    SubExit = True
                else:
                    Error()
        
        # Menú Lanzamiento de Proyectil
        elif opt == 3:
            ReiniciarPropiedades()
            Gravedad = 9.81
            SubExit = False
            while not SubExit:
                if Velocidad != 0 and Angulo != 0:
                    Distancia = LanzamientoProyectil()

                os.system("cls")
                print(Cabecera)
                ActualizarGraficas()
                print(GraficoProyectil)
                print("\033[1;32m    Calculadora de Fisica:\033[0m")
                print("\033[1;34m  Lanzamiento de Proyectil:\033[0m")
                print("Opciones: \n")
                print("\033[1;33m1.\033[0m Cambiar Velocidad inicial.")
                print("\033[1;33m2.\033[0m Cambiar Ángulo.")
                print("\033[1;31m3.\033[0m Volver.")

                opt = int(input(" \nIngrese una opción: "))
                
                if opt == 1:
                    Velocidad = float(input("\n Ingrese la velocidad inicial: "))
                elif opt == 2:
                    Angulo = float(input("\n Ingrese el ángulo: "))
                elif opt == 3:
                    SubExit = True
                else:
                    Error()

        elif opt == 4:
            Exit = True
        else:
            Error()

def MenuVectores():
    Exit = False
    A = []
    B = []
    while not Exit:
        os.system("cls")
        print(Cabecera)
        print(GraficoVectores)
        print("\033[1;32m    Operaciones con Vectores:\033[0m")
        print("Opciones: \n")
        print("\033[1;33m1.\033[0m Suma de Vectores.")
        print("\033[1;33m2.\033[0m Producto Punto.")
        print("\033[1;31m3.\033[0m Volver.")

        opt = int(input(" \nIngrese una opción: "))

        # Menú Suma de Vectores
        if opt == 1:
            SubExit = False
            Resultado = []
            while not SubExit:
                os.system("cls")
                print(Cabecera)
                MostrarVector(A, "A", "1;31")
                MostrarVector(B, "B", "1;34")
                MostrarVector(Resultado, "A\033[0m + \033[1;35mB", "1;35")
                print("\n\033[1;32m    Operaciones con Vectores:\033[0m")
                print("\033[1;34m  Suma de Vectores:\033[0m")
                print("Opciones: \n")
                print("\033[1;33m1.\033[0m Calcular.")
                print("\033[1;33m2.\033[0m Cambiar Vector A.")
                print("\033[1;33m3.\033[0m Cambiar Vector B.")
                print("\033[1;33m4.\033[0m Reiniciar vectores.")
                print("\033[1;31m5.\033[0m Volver.")

                opt = int(input(" \nIngrese una opción: "))
                
                if opt == 1:
                    Resultado = SumaVectores(A, B)
                elif opt == 2:
                    print("\n\033[3m Ingrese los elementos del vector A separados por espacios.\033[0m")
                    A = list(map(int, input("\033[1m   Ingrese el vector \033[31mA\033[0m: ").split()))
                elif opt == 3:
                    print("\n\033[3m Ingrese los elementos del vector A separados por espacios.\033[0m")
                    B = list(map(int, input("\033[1m   Ingrese el vector \033[34mB\033[0m: ").split()))
                elif opt == 4:
                    A = []
                    B = []
                    Resultado = []
                elif opt == 5:
                    SubExit = True
                    A = []
                    B = []
                else:
                    Error()

        # Menú Producto Punto
        elif opt == 2:
            SubExit = False
            Resultado = 0
            while not SubExit:
                os.system("cls")
                print(Cabecera)
                MostrarVector(A, "A", "1;31")
                MostrarMagnitud(A, "A", "1;31")
                print()
                MostrarVector(B, "B", "1;34")
                MostrarMagnitud(B, "B", "1;34")
                print()
                print(f"\033[1;33mA . B\033[0m = \033[1;33m{Resultado}\033[0m")
                print(f"\033[1;33mθ\033[0m = \033[1;33m{AnguloVectores(A, B)}\033[0m\n")
                print("\033[1;34m    Operaciones con Vectores:\033[0m")
                print("\033[1;32m  Producto Punto:\033[0m")
                print("Opciones: \n")
                print("\033[1;33m1.\033[0m Calcular.")
                print("\033[1;33m2.\033[0m Cambiar Vector A.")
                print("\033[1;33m3.\033[0m Cambiar Vector B.")
                print("\033[1;33m4.\033[0m Reiniciar vectores.")
                print("\033[1;31m5.\033[0m Volver.")

                opt = int(input(" \nIngrese una opción: "))

                if opt == 1:
                    Resultado = ProductoPunto(A, B, 0)
                elif opt == 2:
                    print("\n\033[3m Ingrese los elementos del vector A separados por espacios.\033[0m")
                    A = list(map(int, input("\033[1m   Ingrese el vector \033[31mA\033[0m: ").split()))
                elif opt == 3:
                    print("\n\033[3m Ingrese los elementos del vector A separados por espacios.\033[0m")
                    B = list(map(int, input("\033[1m   Ingrese el vector \033[34mB\033[0m: ").split()))
                elif opt == 4:
                    A = []
                    B = []
                    Resultado = 0
                elif opt == 5:
                    SubExit = True
                    A = []
                    B = []
                else:
                    Error()

        elif opt == 3:
            Exit = True
        else:
            Error()

# ############ Función Menú
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
            MenuUnidades()
        elif opt == 2:
            MenuFisica()
        elif opt == 3:
            MenuVectores()
        elif opt == 4:
            Salida = True
            Adios()
        else:
            Error()


# ############ Ejecución
Menu()