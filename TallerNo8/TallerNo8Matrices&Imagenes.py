# Computación Grafica: Taller N.8: Matrices & Imagenes en Python by JDRB
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# ############ Variables Globales
Cabecera = """
\033[1;33m    Computación Gráfica:\033[0m\033[33m Taller N.8: Matrices & Imagenes en Python. \033[0m
\033[3m    By Juan Diego Ruiz B. \033[0m
"""
Gato = """\033[93m             ^~^  ,
            ('Y') )
            /   \/
           (\|||/)\033[0m  
"""
RutaImagen = "Imagenes/"

# ############ Ejecución del Programa
os.system("cls")
print(Cabecera)
print(Gato)

# 01.Elaborar un procedimiento que diseñe la siguiente matriz

# [Cian][Blanco][Rojo]
# [lila][gris][verde]
# [amarillo][negro][azul]

# 02. Realizar un procedimiento que diseñe la siguiente imagen a través 
#     una matriz.

# los colores de prueba de una tv

# 03. Elaborar una función que invierta los colores de una imagen.

# 04. Elaborar una función a la que se le envie de una imagen retorne su
#     capa Roja.

# 05. Elaborar una función a la que se le envie de una imagen retorne su
#     capa Verde.

# 06. Elaborar una función a la que se le envié de una imagen retorne su
#     capa Azul.

# 07. Elaborar una función a la que se le envié de una imagen y retorne la
#     imagen en Magenta.

# 08. Elaborar una función a la que se le envié de una imagen y retorne la
#     imagen en Cyan.

# 09. Elaborar una función a la que se le envié de una imagen y retorne la
#     imagen en Amarillo.

# 10. Elaborar una función en la que le envie por separado las capas RGB y
#     con base en ellas reconstruya la imagen en colores.

# 11. Elaborar una función a la que se le envié 2 imágenes y que me retorne
#     la fusión de las dos imágenes sin ecualizar.

# 12. Elaborar una función a la que se le envié 2 imágenes y que me retorne
#     la fusión de las dos imágenes ecualizadas.

# 13. Elaborar una función a la que se le envie una imagen y un factor y
#     retorne la imagen ecualizada según el factor.

# 14. Elaborar una función a la que se le envie una imagen y que retorne la
#     imagen con la Técnica de promedio (Average).

# 15. Elaborar una función a la que se le envié una imagen y que retorne la
#     imagen en escala de grises con la técnica de promedio (Average).

# 16. Elaborar una función a la que se le envié una imagen y que retorne la
#     imagen en escala de grises con la técnica de Luminosidad (Luminosity).

# 17. Elaborar una función a la que se le envié una imagen y que retorne la
#     imagen en escala de grises con la técnica de La tonalidad (Midgray).