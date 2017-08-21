#-*- coding: utf-8 -*-
"""
  Proceso Digital de Imágenes 2018-1
  :description :Filtros para escala de grises 
  :author: Luis Pablo Mayo Vega

"""
import glob, os, sys
from filtro import Filtro
from PIL import Image

class FiltroGrises(Filtro):
    """
    Clase para modelar los filtros de tonos de gris
    """
    def __init__(self, img):
        super(FiltroGrises, self, img).__init__()
        
    
    def grisPorPromedio(self):
        """
        Genera el tono de gris al sumar los valores del pixel y dividirlos entre 3,
        es decir, calcula el promedio de estos.
        """
        for i in range(0, self.width):
            for j in range(0, self.height):
                r,g,b = self.img.getpixel((i,j))
                gris = int((r+g+b)/3)
                self.img.putpixel((i,j),(gris,gris,gris))
        return self.img.save(self.nombre_img+"_grispromedio", "JPEG")

        
    def grisConstante(self):
        """
        Genera el tono de gris al multiplicar cada color por valores ya dados
        """
        for i in range(0, self.width):
            for j in range(0, self.height):
                r,g,b = self.img.getpixel((i,j))
                self.img.putpixel((i,j),(r*0.3, g*0.59, b*0.11))
        return self.img.save(self.nombre_img+"_grisconstante", "JPEG")


    def grisRGB(self, value):
        """
        Genera el tono de gris al sustituir los 3 valores por el de un solo color.
        Hay que tomar en cuenta que los tonos de gris tienen el mismo valor en cada color.
        """
        if value not in ("R", "r","G","g", "B","b"):
            print ("no ingresaste un color valido")
            return
        for i in range (0, self.width):
            for j in range(0, self.height):
                r,g,b = self.img.getpixel((i,j))
                if value == "R" or value == "r":
                    gris = r
                if value == "G" or value == "g":
                    gris = g
                if value == "B" or value == "b":
                    gris = b
                self.img.putpixel((i,j), (gris,gris,gris))
        return self.img.save(self.nombre_img+"_grisrgb","JPEG")

    
    
    def grisMezclaRB(self):
        """
        Genera el tono de gris al sumar los valores de R, B 
        y despues dividirlo entre 2
        """
        for i in range(0, self.width):
            for j in range(0, self.height):
                r,g,b = self.img.getpixel((i,j))
                gris = int((r + b)/2)
                self.img.putpixel((i,j),(gris, gris, gris))
        return self.img.save(self.nombre_img+"_grismezrb", "JPEG")


    def grisMezclaGB(self):
        """
        Genera el tono de gris al sumar los valores de G, B 
        y despues dividirlo entre 2
        """
        for i in range(0, self.width):
            for j in range(0, self.height):
                r,g,b = self.img.getpixel((i,j))
                gris = int((g + b)/2)
                self.img.putpixel((i,j),(gris, gris, gris))
        return self.img.save(self.nombre_img+"_grismezgb", "JPEG")


    def grisMezclaRG(self):
        """
        Genera el tono de gris al sumar los valores de R, G
        y despues dividirlo entre 2
        """
        for i in range(0, self.width):
            for j in range(0, self.height):
                r,g,b = self.img.getpixel((i,j))
                gris = int((r + g)/2)
                self.img.putpixel((i,j),(gris, gris, gris))
        return self.img.save(self.nombre_img+"_grismezrg", "JPEG")
