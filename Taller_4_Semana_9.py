# ----------------------------------------------------------------------------------------
# PROGRAMA: <<Vertices de un cuadrilatero>>
# ----------------------------------------------------------------------------------------
# Descripción: <<Este es un programa que genera imagenes de cuadrilateros, para posteriormente hallar sus puntos de intercección>>
# ----------------------------------------------------------------------------------------
# Autores:
''' 
# Miguel David Benavides Galindo            md_benavidesg@javeriana.edu.co
# Christian Fernando Rodriguez Rodriguez    rodriguezchristianf@javeriana.edu.co
'''
# Version: 1.0
# [29.09.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULES
import cv2 
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# ----------------------------------------------------------------------------------------
# FUNCIONES
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# Nombre: <<Quadrilateral>>
# ----------------------------------------------------------------------------------------
# Descripcion: <<Es una función que crea la imagen de un cuadrilátero magenta en un fondo cian, a partir de un tamaño N, ingresado por el usuario.>>
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# La función necesita 1 argumento:
    # N:    Tamaño (cuadrado) de la imagen a crear
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# 1. Retorna la imagen del cuadrilatero.
# ----------------------------------------------------------------------------------------
def Quadrilateral(N):
    if N % 2 == 0:
        imag = np.zeros((N,N,3), np.uint8)
        imag[:,:] = (245,255,0)
    
        x_1 = int(np.random.uniform(0, N/2, 1))
        y_1 = int(np.random.uniform(0, N/2, 1))
        x_2 = int(np.random.uniform(N/2, N, 1))
        y_2 = int(np.random.uniform(0, N/2, 1))
        x_3 = int(np.random.uniform(0, N/2, 1))
        y_3 = int(np.random.uniform(N/2, N, 1))
        x_4 = int(np.random.uniform(N/2, N, 1))
        y_4 = int(np.random.uniform(N/2, N, 1))
    
        cv2.line(imag,(x_1,y_1),(x_2,y_2),(255,0,242),1)
        cv2.line(imag,(x_2,y_2),(x_4,y_4),(255,0,242),1)
        cv2.line(imag,(x_3,y_3),(x_4,y_4),(255,0,242),1)
        cv2.line(imag,(x_1,y_1),(x_3,y_3),(255,0,242),1)
        cv2.floodFill(imag, None, (int((x_1+x_2+x_3+x_4)/4),int((y_1+y_2+y_3+y_4)/4)), (255,0,242))
    else:
        imag = np.zeros((N,N,3), np.uint8)
        print('El número:', N, 'es impar. Ingrese un número par.')
    return imag

# ----------------------------------------------------------------------------------------
# Nombre: <<DetectCorners>>
# ----------------------------------------------------------------------------------------
# Descripcion: <<Es una función que a partir de una imagen de un cuadrilatero, encuentra las escinas y las encierra en un circulo amarillo.>>
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# La función necesita 1 argumento:
    # imag:    Imagen a encontrar las esquinas del cuadrilatero
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# 1. Retorna la imagen del cuadrilatero con las esquinas resaltadas en amarillo y un arreglo numpy de sus cooredenadas.
# ----------------------------------------------------------------------------------------
def DetectCorners(imag): 
    img = imag
    gray = cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 10, 0.25, 5)
    corners = np.int0(corners)
    for item in corners:
        x, y = item[0]
        cv2.circle(img, (x,y), 5, (0, 233, 255), -1)
    coordenadas = np.array(corners)
    return [img,coordenadas]
    
# ----------------------------------------------------------------------------------------
# Ejecución
# ----------------------------------------------------------------------------------------
N = int(input("Ingrese la dimensión de la imagen cuadrada N: "))
ima = Quadrilateral(N)
cv2.imshow("Imagen", ima)
cv2.waitKey(0)
imagen = DetectCorners(ima)
cv2.imshow("Imagen", imagen[0])
cv2.waitKey(0)
print(imagen[1])
# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------