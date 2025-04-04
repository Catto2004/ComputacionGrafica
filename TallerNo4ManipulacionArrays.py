# Computación Grafica: Taller N.4: Manipulación de Arrays en Python by JDRB
import os
import random
import numpy as np

# ############ Variables Globales
Cabecera = """
\033[1;33m    Computación Gráfica:\033[0m\033[33m Taller N.4: Manipulación de Arrays en Python. \033[0m
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

VectorA = np.array([2, 3, 5, 1, 4, 7, 9, 8, 6, 10])
VectorB = np.arange(11, 21)
VectorC = np.concatenate((VectorA, VectorB))


# ############ Funciones de Ejercicios

os.system("cls")
print(Cabecera)
print(Gato)

# 01. Cree el siguiente vector A= [2, 3, 5, 1, 4, 7, 9, 8, 6, 10].

print("\033[3m01. Cree el siguiente vector A= [2, 3, 5, 1, 4, 7, 9, 8, 6, 10].\033[0m") 
VectorA = np.array([2, 3, 5, 1, 4, 7, 9, 8, 6, 10])
print(f"\n\033[1;33mA\033[0m = \033[33m{VectorA}\033[0m")

# 02. Cree un vector B que contenga los elementos desde el 11 hasta el 20.

print("\n\033[3m02. Cree un vector B que contenga los elementos desde el 11 hasta el 20.\033[0m")
VectorB = np.arange(11, 21)
print(f"\n\033[1;33mB\033[0m = \033[33m{VectorB}\033[0m")

# 03. Componer un vector C formado por los vectores A y B en la misma fila respectivamente.

print("\n\033[3m03. Componer un vector C formado por los vectores A y B en la misma fila respectivamente.\033[0m")
VectorC = np.concatenate((VectorA, VectorB))
print(f"\n\033[1;33mC\033[0m = \033[33m{VectorC}\033[0m")

# 04. Encuentre el valor mínimo en el vector C haciendo uso de la función propia de Numpy.

print("\n\033[3m04. Encuentre el valor mínimo en el vector C haciendo uso de la función propia de Numpy.\033[0m")
print(f"\nValor mínimo en el vector C: \033[33m{np.min(VectorC)}\033[0m")

# 05. Encuentre el valor máximo en el vector C haciendo uso de la función propia de Numpy.

print("\n\033[3m05. Encuentre el valor máximo en el vector C haciendo uso de la función propia de Numpy.\033[0m")
print(f"\nValor máximo en el vector C: \033[33m{np.max(VectorC)}\033[0m")

# 06. Encuentre la longitud en el vector C haciendo uso de la función propia de Numpy.

print("\n\033[3m06. Encuentre la longitud en el vector C haciendo uso de la función propia de Numpy.\033[0m")
print(f"\nLongitud del vector C: \033[33m{np.size(VectorC)}\033[0m")

# 07. Encentre el promedio de los elementos en el vector C haciendo uso de las operaciones.
#     elementales suma y división.

print("\n\033[3m07. Encentre el promedio de los elementos en el vector C haciendo uso de las operaciones elementales suma y división.\033[0m")
print(f"\nPromedio en el vector C: \033[33m{np.sum(VectorC) / np.size(VectorC)}\033[0m")

# 08. Encuentre el promedio en el vector C haciendo uso de la función propia de Numpy.

print("\n\033[3m08. Encuentre el promedio en el vector C haciendo uso de la función propia de Numpy.\033[0m")
print(f"\nPromedio en el vector C: \033[33m{np.mean(VectorC)}\033[0m")

# 09. Encuentre la media en el vector C haciendo uso de la función propia de Numpy.

print("\n\033[3m09. Encuentre la media en el vector C haciendo uso de la función propia de Numpy.\033[0m")
print(f"\nMedia en el vector C: \033[33m{np.median(VectorC)}\033[0m")

# 10. Encuentre la suma en el vector C haciendo uso de la función propia de Numpy.

print("\n\033[3m10. Encuentre la suma en el vector C haciendo uso de la función propia de Numpy.\033[0m")
print(f"\nSuma en el vector C: \033[33m{np.sum(VectorC)}\033[0m")

# 11. Cree un vector D a partir del vector C con los elementos mayores que 5.

print("\n\033[3m11. Cree un vector D a partir del vector C con los elementos mayores que 5.\033[0m")
VectorD = np.where(VectorC > 5)
print(f"\n\033[1;33mD\033[0m = \033[33m{VectorD}\033[0m")

# 12. Cree un vector E a partir del vector C con los elementos mayores que 5 y menores que 15.

print("\n\033[3m12. Cree un vector E a partir del vector C con los elementos mayores que 5 y menores que 15.\033[0m")
VectorE = VectorC[(VectorC > 5) & (VectorC < 15)]
print(f"\n\033[1;33mE\033[0m = \033[33m{VectorE}\033[0m")

# 13. Cambie los elementos 5 y 15 del vector C por ‘7’.

print("\n\033[3m13. Cambie los elementos 5 y 15 del vector C por ‘7’.\033[0m")
VectorC_mod = np.where((VectorC == 5) | (VectorC == 15), 7, VectorC)
print(f"\nVector C modificado: \033[33m{VectorC_mod}\033[0m")

# 14. Determine la moda del vector C.

print("\n\033[3m14. Determine la moda del vector C usando solo Numpy.\033[0m")
valores, conteo = np.unique(VectorC, return_counts=True)
moda = valores[np.argmax(conteo)]
print(f"\nModa del vector C: \033[33m{moda}\033[0m con frecuencia: {np.max(conteo)}")

# 15. Ordene el Vector C de menor a mayor.

print("\n\033[3m15. Ordene el Vector C de menor a mayor.\033[0m")
VectorC_sorted = np.sort(VectorC)
print(f"\nVector C ordenado: \033[33m{VectorC_sorted}\033[0m")

# 16. Multiplique el vector C por 10.

print("\n\033[3m16. Multiplique el vector C por 10.\033[0m")
VectorC_mult10 = VectorC * 10
print(f"\nVector C * 10: \033[33m{VectorC_mult10}\033[0m")

# 17. Cambie los elementos del 6 al 8 de la matriz C por 60, 70 y 80 respectivamente.

print("\n\033[3m17. Cambie los elementos del 6 al 8 de la matriz C por 60, 70 y 80 respectivamente.\033[0m")
VectorC_copy = VectorC.copy()
VectorC_copy[5:8] = [60, 70, 80]
print(f"\nVector C modificado: \033[33m{VectorC_copy}\033[0m")

# 18. Cambie los elementos del 14 al 16 de la matriz C por 140, 150 y 160 respectivamente.

print("\n\033[3m18. Cambie los elementos del 14 al 16 de la matriz C por 140, 150 y 160 respectivamente.\033[0m")
VectorC_copy[13:16] = [140, 150, 160]
print(f"\nVector C modificado: \033[33m{VectorC_copy}\033[0m")
