import tkinter as tk
from tkinter import filedialog
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# ========== Funciones de imagen ==========

def abrir_imagen(ruta):
    return np.array(Image.open(ruta))

def mostrar_imagen(imagen):
    plt.imshow(imagen)
    plt.axis('off')
    plt.show()

def gris_average(imagen):
    gris = np.mean(imagen, axis=2).astype(np.uint8)
    mostrar_imagen(np.stack([gris]*3, axis=2))

def gris_luminusidad(imagen):
    r, g, b = imagen[:,:,0], imagen[:,:,1], imagen[:,:,2]
    gris = (0.21 * r + 0.72 * g + 0.07 * b).astype(np.uint8)
    mostrar_imagen(np.stack([gris]*3, axis=2))

def gris_tonalidad(imagen):
    max_val = np.max(imagen, axis=2)
    min_val = np.min(imagen, axis=2)
    gris = ((max_val + min_val) / 2).astype(np.uint8)
    mostrar_imagen(np.stack([gris]*3, axis=2))

def invertir_colores(imagen):
    invertida = 255 - imagen
    mostrar_imagen(invertida)

def ajustar_brillo_canal(imagen, canal, factor):
    idx = {'R': 0, 'G': 1, 'B': 2}[canal]
    arr = imagen.astype(np.float32)
    arr[:, :, idx] = np.clip(arr[:, :, idx] * factor, 0, 255)
    mostrar_imagen(arr.astype(np.uint8))

def rotar_imagen(imagen, angle):
    if angle == 90:
        rotada = np.rot90(imagen, k=3)
    elif angle == 180:
        rotada = np.rot90(imagen, k=2)
    elif angle == 270:
        rotada = np.rot90(imagen, k=1)
    mostrar_imagen(rotada)

def ajustar_contraste(imagen, factor):
    mean = np.mean(imagen, axis=(0, 1), keepdims=True)
    arr = imagen.astype(np.float32)
    arr = mean + factor * (arr - mean)
    arr = np.clip(arr, 0, 255)
    mostrar_imagen(arr.astype(np.uint8))

def mostrar_histograma(imagen):
    colores = ('r', 'g', 'b')
    for i, color in enumerate(colores):
        plt.hist(imagen[:, :, i].ravel(), bins=256, color=color, alpha=0.5, label=f'Canal {color.upper()}')
    plt.legend()
    plt.title('Histograma RGB')
    plt.xlabel('Valor de Intensidad')
    plt.ylabel('Frecuencia')
    plt.show()

def extraer_capa(imagen, capa):
    capa_idx = {'R': 0, 'G': 1, 'B': 2}
    if capa in capa_idx:
        arr = np.zeros_like(imagen)
        arr[:, :, capa_idx[capa]] = imagen[:, :, capa_idx[capa]]
        mostrar_imagen(arr)

def fusionar_imagenes(imagen1, imagen2, alpha):
    imagen2_resized = np.array(Image.fromarray(imagen2).resize((imagen1.shape[1], imagen1.shape[0])))
    fusionada = (imagen1 * alpha + imagen2_resized * (1 - alpha)).astype(np.uint8)
    mostrar_imagen(fusionada)

# ========== Interfaz ==========

def ventana_emergente():
    ventana = tk.Tk()
    ventana.title("Editor de Imagen")
    ventana.geometry("650x900")
    ventana.config(bg="white")

    # Variables globales de estado
    imagen_cargada = [None]
    imagen_original = [None]
    imagen_extra = [None]
    alpha = [0.5]
    brillo_factor = {'R': 1.0, 'G': 1.0, 'B': 1.0}
    contraste_factor = [1.0]

    # Funciones para botones
    def cargar_imagen():
        ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg *.jpeg *.png")])
        if ruta:
            imagen = abrir_imagen(ruta)
            imagen_cargada[0] = imagen
            imagen_original[0] = imagen.copy()
            mostrar_imagen(imagen)

    def restablecer_imagen():
        if imagen_original[0] is not None:
            imagen_cargada[0] = imagen_original[0]
            mostrar_imagen(imagen_original[0])

    def cargar_segunda_imagen():
        ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg *.jpeg *.png")])
        if ruta:
            imagen_extra[0] = abrir_imagen(ruta)
            if imagen_cargada[0] is not None:
                fusionar_imagenes(imagen_cargada[0], imagen_extra[0], alpha[0])

    def ajustar_alpha(delta):
        if imagen_cargada[0] is not None and imagen_extra[0] is not None:
            alpha[0] = min(max(alpha[0] + delta, 0.0), 1.0)
            fusionar_imagenes(imagen_cargada[0], imagen_extra[0], alpha[0])

    def ajustar_brillo(canal, delta):
        if imagen_cargada[0] is not None:
            brillo_factor[canal] += delta
            ajustar_brillo_canal(imagen_cargada[0], canal, brillo_factor[canal])

    def ajustar_contraste_ui(delta):
        if imagen_cargada[0] is not None:
            contraste_factor[0] += delta
            ajustar_contraste(imagen_cargada[0], contraste_factor[0])

    # Encabezado
    tk.Label(ventana, text="Editor de Imagen", font=("Arial", 18, "bold"), bg="white").pack(pady=10)

    # Contenedor de botones en dos columnas
    marco_botones = tk.Frame(ventana, bg="white")
    marco_botones.pack(pady=10)

    # Lista de botones
    botones = [
        ("Cargar Imagen", cargar_imagen),
        ("Gris Promedio", lambda: gris_average(imagen_cargada[0]) if imagen_cargada[0] is not None else None),
        ("Gris Luminancia", lambda: gris_luminusidad(imagen_cargada[0]) if imagen_cargada[0] is not None else None),
        ("Gris Tonalidad", lambda: gris_tonalidad(imagen_cargada[0]) if imagen_cargada[0] is not None else None),
        ("Invertir Colores", lambda: invertir_colores(imagen_cargada[0]) if imagen_cargada[0] is not None else None),
        ("Rotar 90°", lambda: rotar_imagen(imagen_cargada[0], 90) if imagen_cargada[0] is not None else None),
        ("Rotar 180°", lambda: rotar_imagen(imagen_cargada[0], 180) if imagen_cargada[0] is not None else None),
        ("Rotar 270°", lambda: rotar_imagen(imagen_cargada[0], 270) if imagen_cargada[0] is not None else None),
        ("Mostrar Histograma", lambda: mostrar_histograma(imagen_cargada[0]) if imagen_cargada[0] is not None else None),
        ("Cargar Imagen Fusión", cargar_segunda_imagen),
        ("Aumentar Fusión (+)", lambda: ajustar_alpha(0.1)),
        ("Reducir Fusión (-)", lambda: ajustar_alpha(-0.1)),
        ("Extraer R", lambda: extraer_capa(imagen_cargada[0], 'R') if imagen_cargada[0] is not None else None),
        ("Extraer G", lambda: extraer_capa(imagen_cargada[0], 'G') if imagen_cargada[0] is not None else None),
        ("Extraer B", lambda: extraer_capa(imagen_cargada[0], 'B') if imagen_cargada[0] is not None else None),
        ("Brillo R (+)", lambda: ajustar_brillo('R', 0.1)),
        ("Brillo R (-)", lambda: ajustar_brillo('R', -0.1)),
        ("Brillo G (+)", lambda: ajustar_brillo('G', 0.1)),
        ("Brillo G (-)", lambda: ajustar_brillo('G', -0.1)),
        ("Brillo B (+)", lambda: ajustar_brillo('B', 0.1)),
        ("Brillo B (-)", lambda: ajustar_brillo('B', -0.1)),
        ("Contraste (+)", lambda: ajustar_contraste_ui(0.1)),
        ("Contraste (-)", lambda: ajustar_contraste_ui(-0.1)),
        ("Restablecer", restablecer_imagen)
    ]

    # Distribuir botones en 2 columnas
    for i, (texto, accion) in enumerate(botones):
        fila = i // 2
        columna = i % 2
        boton = tk.Button(marco_botones, text=texto, command=accion, width=30, height=2, bg="#f0f0f0")
        boton.grid(row=fila, column=columna, padx=5, pady=5)

    ventana.mainloop()

# Ejecutar la interfaz
ventana_emergente()
