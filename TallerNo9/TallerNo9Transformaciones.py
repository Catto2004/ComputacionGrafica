# Computación Grafica: Taller N.9: Transformaciones en Python by JDRB
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# ############ Variables Globales
Cabecera = """
\033[1;33m    Computación Gráfica:\033[0m\033[33m Taller N.9: Transformaciones en Python. \033[0m
\033[3m    By Juan Diego Ruiz B. \033[0m
"""
Gato = """\033[93m             ^~^  ,
            ('Y') )
            /   \/
           (\|||/)\033[0m  
"""
RutaImagen = r"C:\Users\joseo\OneDrive\Escritorio\Code\ComputacionGrafica\ComputacionGrafica\TallerNo9\Esmeralda.png"
CarpetaSalida = r"C:\Users\joseo\OneDrive\Escritorio\Code\ComputacionGrafica\ComputacionGrafica\TallerNo9\Resultados"
GuardarResultados = 1  # 0 -> No guardar, 1 -> Guardar

# ############ Funciones

# Función para guardar y mostrar una imagen
def MostrarImagen(img, titulo="Imagen", nombre_archivo=None):
    plt.imshow(img)
    plt.axis("off")
    plt.title(titulo)
    plt.show()
    
    if GuardarResultados and nombre_archivo:
        if not os.path.exists(CarpetaSalida):
            os.makedirs(CarpetaSalida)
        ruta = os.path.join(CarpetaSalida, nombre_archivo)
        Image.fromarray(img).save(ruta)
        print(f"Imagen guardada: {ruta}")

# 1. Elaborar una función a la que se le envié de una imagen y un factor de
#    ajuste (permite aumentar o disminuir el brillo), la función debe
#    retornar la imagen con el brillo deseado de acuerdo al factor de ajuste.

def AjustarBrillo(imagen, factor):
    return np.clip(imagen.astype(np.float32) * factor, 0, 255).astype(np.uint8)

# 2. Elaborar una función a la que se le envié de una imagen, el canal y un
#    factor de ajuste (permite aumentar o disminuir el brillo), la función
#    debe retornar la imagen con el brillo deseado de acuerdo al canal y al
#    factor de ajuste.

def AjustarBrilloCanal(imagen, canal, factor):
    img_mod = imagen.copy().astype(np.float32)
    img_mod[..., canal] *= factor
    return np.clip(img_mod, 0, 255).astype(np.uint8)


# 3. Elaborar una función a la que se le envié de una imagen y un factor de
#    contraste, la función debe retornar la imagen con el contraste deseado
#    de acuerdo al factor de contraste.

def AjustarContraste(imagen, factor):
    return np.clip(128 + (imagen - 128) * factor, 0, 255).astype(np.uint8)

# 4. Elaborar una función que permita realizarle un zoom a una parte de la
#    imagen.

def ZoomImagen(imagen, x, y, ancho, alto):
    return imagen[y:y+alto, x:x+ancho]

# 5. Elaborar una función que permita binarizar una imagen.

def BinarizarImagen(imagen, umbral=128):
    gris = np.mean(imagen, axis=-1)
    return np.where(gris > umbral, 255, 0).astype(np.uint8)

# 6. Elaborar una función que permita rotar una imagen.

def RotarImagen(imagen, angulo):
    return np.array(Image.fromarray(imagen).rotate(angulo))

# 7. Elaborar un procedimiento que permita sacar el histograma de cada
#    una de las capas de una imagen.

def HistogramaImagen(imagen):
    colores = ['Red', 'Green', 'Blue']
    for i, color in enumerate(colores):
        plt.hist(imagen[..., i].ravel(), bins=256, color=color.lower(), alpha=0.6)
    plt.title("Histograma RGB")
    plt.show()


# ############ Ejecución del Programa
os.system("cls")
print(Cabecera)
print(Gato)

imagen = np.array(Image.open(RutaImagen))

# Aplicar transformaciones y mostrar imágenes
imagen_brillo = AjustarBrillo(imagen, 1.5)
MostrarImagen(imagen_brillo, "Brillo Ajustado", "brillo.png")

imagen_brillo_rojo = AjustarBrilloCanal(imagen, 0, 1.5)
MostrarImagen(imagen_brillo_rojo, "Brillo en Canal Rojo", "brillo_rojo.png")

imagen_contraste = AjustarContraste(imagen, 1.5)
MostrarImagen(imagen_contraste, "Contraste Ajustado", "contraste.png")

imagen_zoom = ZoomImagen(imagen, 50, 50, 100, 100)
MostrarImagen(imagen_zoom, "Zoom en Imagen", "zoom.png")

imagen_binaria = BinarizarImagen(imagen)
MostrarImagen(imagen_binaria, "Imagen Binarizada", "binarizada.png")

imagen_rotada = RotarImagen(imagen, 45)
MostrarImagen(imagen_rotada, "Imagen Rotada", "rotada.png")

HistogramaImagen(imagen)