import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def AbrirImagen(Ruta):
    Imagen = Image.open(Ruta)
    return Imagen

def MostrarImagen(Imagen):
    plt.imshow(Imagen)
    plt.axis("off")
    plt.show()

def RecortarImagen(Imagen, Xi, Yi, Xf, Yf):
    ImagenArray = np.array(Imagen)
    return ImagenArray[Yi:Yf, Xi:Xf]

def AjustarBrillo(Imagen, Valor):
    ImagenArray = np.array(Imagen, dtype=np.float32)
    ImagenAjustada = np.clip(ImagenArray + Valor, 0, 255)
    return ImagenAjustada.astype(np.uint8)

def FusionarImagen(Imagen1, Imagen2, Alpha=0.5):
    Imagen1 = np.array(Imagen1, dtype=np.float32)
    Imagen2 = np.array(Imagen2, dtype=np.float32)
    
    return np.clip(Alpha * Imagen1 + (1 - Alpha) * Imagen2, 0, 255).astype(np.uint8)

RutaCat = r"C:\Users\juanc\OneDrive\Escritorio\Code\ComputacionGrafica\Clase18Febrero\cat.jpg"
RutaPan = r"C:\Users\juanc\OneDrive\Escritorio\Code\ComputacionGrafica\Clase18Febrero\pan.jpg"

ImagenCat = AbrirImagen(RutaCat)
ImagenPan = AbrirImagen(RutaPan)

CatRecortado = RecortarImagen(ImagenCat, 80, 100, 200, 200)
PanEditado = AjustarBrillo(ImagenPan, 100)
CatPan = FusionarImagen(ImagenCat, ImagenPan)

MostrarImagen(ImagenCat)
MostrarImagen(ImagenPan)

MostrarImagen(CatRecortado)
MostrarImagen(PanEditado)
MostrarImagen(CatPan)