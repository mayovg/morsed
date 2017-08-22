#-*- coding: utf-8 -*-
"""
  Proceso Digital de Imágenes 2018-1
  :description :Filtros para colorear de un solo color 
  :author: Luis Pablo Mayo Vega

"""
from filtro import Filtro
from PIL import Image
import random

class FiltroColores(Filtro):
    """
    Clase para modelar los filtros de un solo color (RGB)
    """
    def __init__(self, img):
        super(FiltroColores, self).__init__(img)


    def rojo(self):
        """
        Dejamos unicamente el color rojo en la imagen
        """
        for i in range(0, self.width):
            for j in range(0, self.height):
                r,g,b = self.img.getpixel((i,j))
                self.img.putpixel((i,j), (r,0,0))
        return self.img.save(self.nombre_img+"rojo","JPEG")
            

    def verde(self):
        """
        Dejamos unicamente el color verde en la imagen
        """
        for i in range(0, self.width):
            for j in range(0, self.height):
                r,g,b = self.img.getpixel((i,j))
                self.img.putpixel((i,j), (0,g,0))
        return self.img.save(self.nombre_img+"verde","JPEG")

    
    def azul(self):
        """
        Dejamos unicamente el color azul en la imagen
        """
        for i in range(0, self.width):
            for j in range(0, self.height):
                r,g,b = self.img.getpixel((i,j))
                self.img.putpixel((i,j), (0,0,b))
        return self.img.save(self.nombre_img+"azul","JPEG")
            

    def azar(self):
        """
        Elige un color aleatorio y colorea la imagen con el mismo
        """
        color = random.randint(0,2)
        if color == 0:
            return rojo()
        elif color == 1:
            return verde()
        else:
            return azul()

        
    
