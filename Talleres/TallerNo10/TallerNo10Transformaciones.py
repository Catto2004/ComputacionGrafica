# Computación Grafica: Taller N.10: Imagenes Termograficas en Python by JDRB
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import scipy.stats as stats

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
RutaImagen = r"C:\Users\joseo\OneDrive\Escritorio\Code\ComputacionGrafica\ComputacionGrafica\TallerNo10\FotoTermica1.tiff"
CarpetaSalida = r"C:\Users\joseo\OneDrive\Escritorio\Code\ComputacionGrafica\ComputacionGrafica\TallerNo10\Resultados"
GuardarResultados = 0  # 0 -> No guardar, 1 -> Guardar

# Parametros de temperatura
TemMin = -40
TemMax = 160
NBits = 14

# ############ Funciones

# Función para guardar y mostrar una imagen
def MostrarImagen(img, titulo="Imagen", nombre_archivo=None):
    plt.imshow(img, cmap='hot')
    plt.axis("off")
    plt.title(titulo)
    plt.show()
    
    if GuardarResultados and nombre_archivo:
        if not os.path.exists(CarpetaSalida):
            os.makedirs(CarpetaSalida)
        ruta = os.path.join(CarpetaSalida, nombre_archivo)
        Image.fromarray(img).save(ruta)
        print(f"Imagen guardada: {ruta}")

# Cargar imagen térmica
def CargarImagenTermica(ruta):
    img = np.array(Image.open(ruta))
    return img

# Convertir a grados centígrados
def ConvertirAGradosC(matriz):
    return (TemMax - TemMin) * matriz / (2 ** NBits) + TemMin

# 1. Calcule y muestre en un print la temperatura promedio, medina y moda,
#    la temperatura máxima (con sus coordenadas x,y) y la temperatura
#    mínima de la imagen (con sus coordenadas x,y).

def ObtenerEstadisticas(matriz):
    media = np.mean(matriz)
    mediana = np.median(matriz)
    moda = float(stats.mode(matriz, axis=None).mode)  # Solución del error
    min_val = np.min(matriz)
    max_val = np.max(matriz)
    min_pos = np.unravel_index(np.argmin(matriz), matriz.shape)
    max_pos = np.unravel_index(np.argmax(matriz), matriz.shape)
    
    print(f"Temperatura promedio: {media:.2f}°C")
    print(f"Mediana: {mediana:.2f}°C")
    print(f"Moda: {moda:.2f}°C")  # Ahora no dará error
    print(f"Temperatura mínima: {min_val:.2f}°C en {min_pos}")
    print(f"Temperatura máxima: {max_val:.2f}°C en {max_pos}")
    
    return min_pos, max_pos

# 2. Realice una figura llamada “Imagen Termográfica” donde muestre en el
#    primer subplot la imagen termográfica, en el segundo subplot muestre
#    el histograma de la imagen (para el histograma use los componentes
#    histogram de Numpy y hist de Matplotlib).

def GraficarImagenTermica(matriz, min_pos, max_pos, nombre_archivo):
    plt.figure(figsize=(8, 6))
    plt.imshow(matriz, cmap="inferno")
    plt.colorbar(label="Temperatura (°C)")
    plt.scatter(max_pos[1], max_pos[0], color='magenta', marker='o', label='Máximo')
    plt.scatter(min_pos[1], min_pos[0], color='cyan', marker='D', label='Mínimo')
    plt.legend()
    plt.title("Imagen Termográfica")
    plt.axis("off")
    plt.show()
    
    if GuardarResultados:
        if not os.path.exists(CarpetaSalida):
            os.makedirs(CarpetaSalida)  # Crear carpeta si no existe
        ruta = os.path.join(CarpetaSalida, nombre_archivo)
        plt.savefig(ruta)
        print(f"Imagen térmica guardada: {ruta}")

# 3. Marque el punto máximo de temperatura en la grafica de la imagen
#    termográfica (para ello use un Círculo de color Magenta).

def GraficarHistograma(matriz, nombre_archivo):
    plt.figure(figsize=(8, 4))
    plt.hist(matriz.ravel(), bins=256, color='orange', alpha=0.75)
    plt.title("Histograma de Temperaturas")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Frecuencia")
    plt.show()
    
    if GuardarResultados:
        if not os.path.exists(CarpetaSalida):
            os.makedirs(CarpetaSalida)  # Crear carpeta si no existe
        ruta = os.path.join(CarpetaSalida, nombre_archivo)
        plt.savefig(ruta)
        print(f"Histograma guardado: {ruta}")

# 4. Marque el punto mínimo de temperatura en la grafica de la imagen
#    termográfica (para ello use un Rombo de color cian).

# ############ Ejecución del Programa
os.system("cls")
print(Cabecera)
print(Gato)

os.system("cls")
print(Cabecera)
print(Gato)

imagen_raw = CargarImagenTermica(RutaImagen)
imagen_celsius = ConvertirAGradosC(imagen_raw)
min_pos, max_pos = ObtenerEstadisticas(imagen_celsius)
GraficarImagenTermica(imagen_celsius, min_pos, max_pos, "imagen_termografica.png")
GraficarHistograma(imagen_celsius, "histograma_temperaturas.png")