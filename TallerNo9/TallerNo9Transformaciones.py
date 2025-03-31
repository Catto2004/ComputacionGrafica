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
RutaImagen = r"C:\Users\joseo\OneDrive\Escritorio\Code\ComputacionGrafica\ComputacionGrafica\TallerNo9\Esmeralda.JPEG"

# ############ Ejecución del Programa
os.system("cls")
print(Cabecera)
print(Gato)

# 1. Elaborar una función a la que se le envié de una imagen y un factor de
#    ajuste (permite aumentar o disminuir el brillo), la función debe
#    retornar la imagen con el brillo deseado de acuerdo al factor de ajuste.

# 2. Elaborar una función a la que se le envié de una imagen, el canal y un
#    factor de ajuste (permite aumentar o disminuir el brillo), la función
#    debe retornar la imagen con el brillo deseado de acuerdo al canal y al
#    factor de ajuste.

# 3. Elaborar una función a la que se le envié de una imagen y un factor de
#    contraste, la función debe retornar la imagen con el contraste deseado
#    de acuerdo al factor de contraste.

# 4. Elaborar una función que permita realizarle un zoom a una parte de la
#    imagen.

# 5. Elaborar una función que permita binarizar una imagen.

# 6. Elaborar una función que permita rotar una imagen.

# 7. Elaborar un procedimiento que permita sacar el histograma de cada
#    una de las capas de una imagen.