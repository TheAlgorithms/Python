# Módulos

import doctest
import math
import random
from typing import List

import cv2
import numpy as np

"""
Histogram of oriented gradients
https://en.wikipedia.org/wiki/Histogram_of_oriented_gradients
"""

# Establecemos una semilla
random.seed(1234)


class HistogramOrientedGradients:
    def __init__(self, imagen: np.float32) -> None:

        """
        imagen : numpy array of float values
        """
        self.imagen = imagen

    def HOG(self) -> np.float32:

        """
        Returns the descriptors vector of am inage

        :return: list of the descriptors values
        """

        # Pasamos la imagen a float (escala 0-1)
        self.imagen = np.float32(self.imagen) / 255.0

        # Comenzamos obteniendo las imágenes gradiente. Para ello
        # convolucionamos la imagen con kernels Sobel 1D.

        g_x = cv2.Sobel(self.imagen, cv2.CV_32F, 1, 0, ksize=1)
        g_y = cv2.Sobel(self.imagen, cv2.CV_32F, 0, 1, ksize=1)

        # Calculamos la magnitud
        magnitud = np.sqrt(g_x**2 + g_y**2)

        # Calculamos la orientacion
        orientacion = np.abs(np.arctan2(g_y, g_x) * 180 / np.pi)

        # Ahora debemos calcular un histograma de orientación de gradiente
        # por cada célula 8x8 de nuestra imagen. Para ello crearemos una
        # matriz de listas que iremos rellenando.

        hog = [
            [0 for x in range(int(self.imagen.shape[1] / 8))]
            for y in range(int(self.imagen.shape[0] / 8))
        ]

        # Recorremos cada célula
        for indice1, r in enumerate(range(0, self.imagen.shape[0], 8)):
            for indice2, c in enumerate(range(0, self.imagen.shape[1], 8)):

                # Inicializamos el hog de la célula actual
                hog_aux = [0.0 for i in range(0, 10)]
                hog_angles = [10, 30, 50, 70, 90, 110, 130, 150, 170, 180]
                mag_aux = magnitud[r : r + 8, c : c + 8, 1]
                ori_aux = orientacion[r : r + 8, c : c + 8, 1]

                # Recorremos la célula
                for i in range(mag_aux.shape[0]):
                    for j in range(mag_aux.shape[1]):

                        # Vemos cual es el ángulo más cercano de la lista de hog_angles
                        indx = (np.abs(hog_angles - ori_aux[i][j])).argmin()

                        # Si coincide con el ángulo, añadimos la
                        # magnitud del pixel al hog
                        if ori_aux[i][j] == hog_angles[indx]:
                            hog_aux[indx] += mag_aux[i][j]

                        # Si no coincide, dividimos la magnitud
                        # entre los ángulos adyacentes
                        else:
                            # Si el ángulo es menor
                            if ori_aux[i][j] < hog_angles[indx]:

                                hog_aux[indx - 1] += (
                                    mag_aux[i][j]
                                    * (hog_angles[indx] - ori_aux[i][j])
                                    / (hog_angles[indx] - hog_angles[indx - 1])
                                )

                                hog_aux[indx] += (
                                    mag_aux[i][j]
                                    * (ori_aux[i][j] - hog_angles[indx - 1])
                                    / (hog_angles[indx] - hog_angles[indx - 1])
                                )

                            # Si el ángulo es mayor
                            else:

                                hog_aux[indx] += (
                                    mag_aux[i][j]
                                    * (hog_angles[indx + 1] - ori_aux[i][j])
                                    / (hog_angles[indx + 1] - hog_angles[indx])
                                )

                                hog_aux[indx + 1] += (
                                    mag_aux[i][j]
                                    * (ori_aux[i][j] - hog_angles[indx])
                                    / (hog_angles[indx + 1] - hog_angles[indx])
                                )

                # Almacenamos en hog los valores de hog_aux
                hog[indice1][indice2] = hog_aux

        # Agrupamos los histogramas/célula en bloques
        # de histogramas. Cada bloque estará formado
        # por 4 células.
        hog_bloques = []
        for i in range(0, int(self.imagen.shape[0] / 8) - 1):
            for j in range(0, int(self.imagen.shape[1] / 8) - 1):

                aux: list[float] = []

                aux = aux + hog[i][j]
                aux = aux + hog[i][j + 1]
                aux = aux + hog[i + 1][j]
                aux = aux + hog[i + 1][j + 1]

                hog_bloques.append(aux)

        # Normalizamos el hog por bloques
        for i, bloque in enumerate(hog_bloques):

            # Calculamos el modulo del bloque actual
            modulo = 0.0
            for el in bloque:
                modulo = modulo + el**2

            modulo = math.sqrt(modulo + 0.01)

            # Dividimos el bloque actual entre el módulo
            hog_bloques[i] = [x / modulo for x in bloque]

        # Concatenamos todos los elementos del hog de bloques
        # para obtener el vector de descriptores
        vector_descriptores = [x for lis in hog_bloques for x in lis]

        # Normalizamos el vector de descriptores
        modulo = 0.0
        for el in vector_descriptores:
            modulo = modulo + el**2

        modulo = math.sqrt(modulo + 0.01)

        # Dividimos cada elemento del vector entre el módulo
        vector_descriptores = [x / modulo for x in vector_descriptores]

        return vector_descriptores


if __name__ == "__main__":
    im = cv2.imread("path", 1)
    hog = HistogramOrientedGradients(im)
    descriptors = hog.HOG()
    doctest.testmod()
