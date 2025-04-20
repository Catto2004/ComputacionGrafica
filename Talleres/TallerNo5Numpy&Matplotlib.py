# Computación Grafica: Taller N.5: Numpy & Matplotlib en Python by JDRB
import os
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# ############ Variables Globales
Cabecera = """
\033[1;33m    Computación Gráfica:\033[0m\033[33m Taller N.5: Numpy & Matplotlib en Python. \033[0m
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

# ############ Ejecución del Programa
os.system("cls")
print(Cabecera)
print(Gato)

# 01. Creación y Manipulación de Arrays
A = np.arange(1, 16)
A = A.reshape(3, 5)
print("\n\033[3m01. Matriz A (1 al 15, redimensionada 3x5):\033[0m")
print(f"\n\033[1;33mA\033[0m =\n\033[33m{A}\033[0m")

# 02. Operaciones Básicas
suma_A = np.sum(A)
media_A = np.mean(A)
producto_A = np.prod(A)
print("\n\033[3m02. Suma, media y producto de A:\033[0m")
print(f"\nSuma: \033[33m{suma_A}\033[0m, Media: \033[33m{media_A}\033[0m, Producto: \033[33m{producto_A}\033[0m")

# 03. Acceso y Slicing
elementos = A[1, 1:3]
print("\n\033[3m03. Segundo y tercer elemento de la segunda fila de A:\033[0m")
print(f"\nElementos: \033[33m{elementos}\033[0m")

# 04. Indexación Booleana
B = A[A > 7]
print("\n\033[3m04. Array B con elementos mayores que 7 de A:\033[0m")
print(f"\n\033[1;33mB\033[0m = \033[33m{B}\033[0m")

# 05. Álgebra Lineal
C = np.array([[2, 5, 7],
              [6, 3, 4],
              [5, -2, -3]])
determinante_C = np.linalg.det(C)
inversa_C = np.linalg.inv(C)
print("\n\033[3m05. Determinante e inversa de la matriz C:\033[0m")
print(f"\nMatriz C:\n\033[33m{C}\033[0m")
print(f"\nDeterminante: \033[33m{determinante_C}\033[0m")
print(f"\nInversa:\n\033[33m{inversa_C}\033[0m")

# 06. Estadísticas con NumPy
D = np.random.rand(100)
max_D = np.max(D)
min_D = np.min(D)
media_D = np.mean(D)
std_D = np.std(D)
print("\n\033[3m06. Estadísticas del array D (100 números aleatorios):\033[0m")
print(f"\nMáximo: \033[33m{max_D}\033[0m, Mínimo: \033[33m{min_D}\033[0m, Media: \033[33m{media_D}\033[0m, Desviación estándar: \033[33m{std_D}\033[0m")

# 07. Gráfico Básico
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_seno = np.sin(x)
y_coseno = np.cos(x)
plt.figure()
plt.plot(x, y_seno, label='Seno')
plt.plot(x, y_coseno, label='Coseno')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funciones Seno y Coseno')
plt.legend()
plt.grid(True)
plt.show()

# 08. Gráficos de Dispersión
indices = np.arange(len(D))
plt.figure()
plt.scatter(indices, D)
plt.xlabel('Índice')
plt.ylabel('Valor de D')
plt.title('Gráfico de Dispersión de D')
plt.grid(True)
plt.show()

# 09. Histogramas
plt.figure()
plt.hist(D, bins=10, edgecolor='black')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma de D')
plt.grid(True)
plt.show()

# 10. Manipulación de Imágenes con Matplotlib
imagen_color = mpimg.imread(r'C:\Users\juanc\OneDrive\Escritorio\Code\ComputacionGrafica\TallerNo4\imagen.png')

# 11. Convertir a escala de grises
imagen_gris = np.dot(imagen_color[...,:3], [0.2989, 0.5870, 0.1140])

# 12. Mostrar imagen original
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(imagen_color)
plt.title('Imagen Original')
plt.axis('off')

# 13. Mostrar imagen en escala de grises
plt.subplot(1, 2, 2)
plt.imshow(imagen_gris, cmap='gray')
plt.title('Imagen en Escala de Grises')
plt.axis('off')

plt.show()