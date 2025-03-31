# Computación Grafica: Taller N.10: Imagenes Termograficas en Python by JDRB
import os
import random

# ############ Variables Globales
Cabecera = """
\033[1;33m    Computación Gráfica:\033[0m\033[33m Taller N.10: Imagenes Termograficas en Python. \033[0m
\033[3m    By Juan Diego Ruiz B. \033[0m
"""
Gato = """\033[93m             ^~^  ,
            ('Y') )
            /   \/
           (\|||/)\033[0m  
"""
FotoTermica = [
    r"C:\Users\joseo\OneDrive\Escritorio\Code\ComputacionGrafica\ComputacionGrafica\TallerNo10\FotoTermica1.tiff",
    r"C:\Users\joseo\OneDrive\Escritorio\Code\ComputacionGrafica\ComputacionGrafica\TallerNo10\FotoTermica2.tiff",
    r"C:\Users\joseo\OneDrive\Escritorio\Code\ComputacionGrafica\ComputacionGrafica\TallerNo10\FotoTermica3.tiff",
    r"C:\Users\joseo\OneDrive\Escritorio\Code\ComputacionGrafica\ComputacionGrafica\TallerNo10\FotoTermica4.tiff"
]

# ############ Ejecución del Programa
os.system("cls")
print(Cabecera)
print(Gato)

""" TEORIA
Una cámara térmica es un dispositivo sin contacto que detecta la energía
infrarroja (calor) y la convierte en una señal electrónica, que luego se procesa
para producir una foto térmica en un monitor de video y realizar cálculos de
temperatura. La imagen térmica se almacena en formato tiff y básicamente es
una matriz de valores en una escala entre 0 y 2^(14) bits.

Para transformar la matriz en datos con temperatura en grados centígradosse
usa la siguiente formula.
D= matriz con los datos de la imagen
TemMin=-40
TemMax=160
NBits=14
GradosC = (TemMax-TemMin)*D/2^NBits+TemMin
"""

# 1. Calcule y muestre en un print la temperatura promedio, medina y moda,
#    la temperatura máxima (con sus coordenadas x,y) y la temperatura
#    mínima de la imagen (con sus coordenadas x,y).

# 2. Realice una figura llamada “Imagen Termográfica” donde muestre en el
#    primer subplot la imagen termográfica, en el segundo subplot muestre
#    el histograma de la imagen (para el histograma use los componentes
#    histogram de Numpy y hist de Matplotlib).

# 3. Marque el punto máximo de temperatura en la grafica de la imagen
#    termográfica (para ello use un Círculo de color Magenta).

# 4. Marque el punto mínimo de temperatura en la grafica de la imagen
#    termográfica (para ello use un Rombo de color cian).

""" Nota:
- MatrizCenti contiene tiene la matriz con los datos convertidos a grados
centígrados
- Use la función shape de numpy para obtener las dimensiones de la matriz
(Filas, Columnas, Capas)
"""