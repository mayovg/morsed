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
        self.img = Image.open(img) # la imagen a la que se aplicara el filtro
        self.width = img.getWidth() # el ancho de la imagen
        self.height = img.getHeight() # la altura de la imagen

    
