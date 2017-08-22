#-*- coding: utf-8 -*-
"""
  Proceso Digital de Imágenes 2018-1
  :description :clase base para los filtros 
  :author: Luis Pablo Mayo Vega

"""

from PIL import Image

class Filtro:
    """
    Clase base para manejar las caracteristicas en comun de los filtros
    """
    def __init__(self, img):
        self.nombre_img = img
        self.img = Image.open(img) # la imagen a la que se aplicara el filtro
        self.width = self.img.width # el ancho de la imagen
        self.height = self.img.height # la altura de la imagen

    
