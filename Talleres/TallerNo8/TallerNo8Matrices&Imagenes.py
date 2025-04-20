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
RutaImagen = r"C:\Users\joseo\OneDrive\Escritorio\Code\ComputacionGrafica\ComputacionGrafica\TallerNo8\GatoEnojado.png"
CarpetaSalida = r"C:\Users\joseo\OneDrive\Escritorio\Code\ComputacionGrafica\ComputacionGrafica\TallerNo8\Resultados"
GuardarResultados = 1  # 0 -> No guardar, 1 -> Guardar

# ############ Funciones

# Función para guardar y mostrar una imagen
def MostrarImagen(img, titulo="Imagen", nombre_archivo=None):
    plt.imshow(img)
    plt.axis("off")
    plt.title(titulo)
    plt.show()
    
    if GuardarResultados and nombre_archivo:
        ruta = os.path.join(CarpetaSalida, nombre_archivo)
        Image.fromarray(img).save(ruta)
        print(f"Imagen guardada: {ruta}")

# 01. Elaborar un procedimiento que diseñe la siguiente matriz

def MatrizColores():
    colores = np.array([
        [[0, 255, 255], [255, 255, 255], [255, 0, 0]],
        [[128, 0, 128], [128, 128, 128], [0, 255, 0]],
        [[255, 255, 0], [0, 0, 0], [0, 0, 255]]
    ], dtype=np.uint8)
    return colores

# 02. Realizar un procedimiento que diseñe la siguiente imagen a través 
#     una matriz.

def ColoresTV():
    tv_colores = np.zeros((100, 300, 3), dtype=np.uint8)
    colores = [ [255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [255, 255, 255], [0, 0, 0] ]
    for i, color in enumerate(colores):
        tv_colores[:, i*50:(i+1)*50] = color
    return tv_colores

# 03. Elaborar una función que invierta los colores de una imagen.

def InvertirColores(imagen):
    if imagen.shape[-1] == 4:  # Si la imagen tiene canal alfa
        rgb = imagen[..., :3]  # Solo tomar los primeros tres canales
        alfa = imagen[..., 3:]  # Separar el canal alfa
        invertida = 255 - rgb
        return np.concatenate((invertida, alfa), axis=-1)  # Reunir canales
    else:
        return 255 - imagen

# 04-06. Elaborar una función a la que se le envie de una imagen retorne su
#     capa Roja, Verde y Azul.

def ObtenerCapa(imagen, canal):
    if imagen.shape[-1] == 4:  # Si la imagen tiene canal alfa
        capa = np.zeros_like(imagen)
        capa[..., canal] = imagen[..., canal]  # Extraer la capa deseada
        capa[..., 3] = imagen[..., 3]  # Mantener el canal alfa intacto
    else:
        capa = np.zeros_like(imagen)
        capa[..., canal] = imagen[..., canal]
    return capa

# 07. Elaborar una función a la que se le envié de una imagen y retorne la
#     imagen en Magenta.

def ImagenMagenta(imagen):
    magenta = imagen.copy()
    magenta[..., 1] = 0  # Eliminar canal verde
    return magenta

# 08. Elaborar una función a la que se le envié de una imagen y retorne la
#     imagen en Cyan.

def ImagenCyan(imagen):
    cyan = imagen.copy()
    cyan[..., 0] = 0  # Eliminar canal rojo
    return cyan

# 09. Elaborar una función a la que se le envié de una imagen y retorne la
#     imagen en Amarillo.

def ImagenAmarillo(imagen):
    amarillo = imagen.copy()
    amarillo[..., 2] = 0  # Eliminar canal azul
    return amarillo

# 10. Elaborar una función en la que le envie por separado las capas RGB y
#     con base en ellas reconstruya la imagen en colores.

def ReconstruirImagen(capa_r, capa_g, capa_b):
    return np.stack([capa_r[..., 0], capa_g[..., 1], capa_b[..., 2]], axis=-1)

# 11. Elaborar una función a la que se le envié 2 imágenes y que me retorne
#     la fusión de las dos imágenes sin ecualizar.

def FusionarImagenes(img1, img2):
    return np.clip((img1.astype(np.float32) + img2.astype(np.float32)) / 2, 0, 255).astype(np.uint8)

# 12. Elaborar una función a la que se le envié 2 imágenes y que me retorne
#     la fusión de las dos imágenes ecualizadas.

def FusionarEcualizado(img1, img2):
    img1 = img1.astype(np.float32) / 255.0
    img2 = img2.astype(np.float32) / 255.0
    fusion = (img1 + img2) / np.maximum(img1 + img2, 1)
    return (fusion * 255).astype(np.uint8)

# 13. Elaborar una función a la que se le envie una imagen y un factor y
#     retorne la imagen ecualizada según el factor.

def EcualizarImagen(imagen, factor):
    return np.clip(imagen.astype(np.float32) * factor, 0, 255).astype(np.uint8)

# 14. Elaborar una función a la que se le envie una imagen y que retorne la
#     imagen con la Técnica de promedio (Average).

def EscalaGrisesAverage(imagen):
    gris = np.mean(imagen, axis=-1)
    return np.stack([gris]*3, axis=-1).astype(np.uint8)

# 15. Elaborar una función a la que se le envié una imagen y que retorne la
#     imagen en escala de grises con la técnica de promedio (Average).

def EscalaGrisesLuminosity(imagen):
    gris = 0.21 * imagen[..., 0] + 0.72 * imagen[..., 1] + 0.07 * imagen[..., 2]
    return np.stack([gris]*3, axis=-1).astype(np.uint8)

# 16. Elaborar una función a la que se le envié una imagen y que retorne la
#     imagen en escala de grises con la técnica de Luminosidad (Luminosity).

def EscalaGrisesMidgray(imagen):
    gris = (np.max(imagen, axis=-1) + np.min(imagen, axis=-1)) / 2
    return np.stack([gris]*3, axis=-1).astype(np.uint8)

# ############ Ejecución del Programa
os.system("cls")
print(Cabecera)
print(Gato)

if GuardarResultados and not os.path.exists(CarpetaSalida):
    os.makedirs(CarpetaSalida)
    print(f"\nSe Guardaron los Resultados en la Carpeta: \e[1;33m{CarpetaSalida}\033[0m")


imagen = np.array(Image.open(RutaImagen))

MostrarImagen(MatrizColores(), "Matriz de Colores", "matriz_colores.png")
MostrarImagen(ColoresTV(), "Colores de TV", "colores_tv.png")

imagen_invertida = InvertirColores(imagen)
MostrarImagen(imagen_invertida, "Imagen Invertida", "imagen_invertida.png")

capa_roja = ObtenerCapa(imagen, 0)
capa_verde = ObtenerCapa(imagen, 1)
capa_azul = ObtenerCapa(imagen, 2)
MostrarImagen(capa_roja, "Capa Roja", "capa_roja.png")
MostrarImagen(capa_verde, "Capa Verde", "capa_verde.png")
MostrarImagen(capa_azul, "Capa Azul", "capa_azul.png")

MostrarImagen(ImagenMagenta(imagen), "Imagen en Magenta", "imagen_magenta.png")
MostrarImagen(ImagenCyan(imagen), "Imagen en Cyan", "imagen_cyan.png")
MostrarImagen(ImagenAmarillo(imagen), "Imagen en Amarillo", "imagen_amarillo.png")

imagen_reconstruida = ReconstruirImagen(capa_roja, capa_verde, capa_azul)
MostrarImagen(imagen_reconstruida, "Imagen Reconstruida", "imagen_reconstruida.png")

imagen_gris_avg = EscalaGrisesAverage(imagen)
MostrarImagen(imagen_gris_avg, "Escala de Grises (Average)", "imagen_gris_average.png")

imagen_gris_lum = EscalaGrisesLuminosity(imagen)
MostrarImagen(imagen_gris_lum, "Escala de Grises (Luminosity)", "imagen_gris_luminosity.png")

imagen_gris_mid = EscalaGrisesMidgray(imagen)
MostrarImagen(imagen_gris_mid, "Escala de Grises (Midgray)", "imagen_gris_midgray.png")