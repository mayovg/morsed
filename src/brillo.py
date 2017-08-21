#-*- coding: utf-8 -*-
"""
  Proceso Digital de Imágenes 2018-1
  :description :Filtros para cambiar el brillo 
  :author: Luis Pablo Mayo Vega

"""
from filtro import Filtro
from PIL import Image

class FiltroBrillo(Filtro):
    """
    Clase para modificar el brillo de una imagen
    """
    def __init__(self, img):
        super(FiltroBrillo, self, img).__init__()


    def brillo(brillo):
        """
        Metodo para modificar el brillo
        """
        if brillo not in range(-128, 129):
            print ("no es un brillo valido!!")
            return
        for i in range(0, self.width):
            for j in range(0, self.height):
                r,g,b = self.img.getpixel((i,j))
                rp = r+brillo
                gp = g+brillo
                bp = b+brillo
                if rp > 255:
                    rp = 255
                elif rp < 0:
                    rp = 0
                elif gp > 255:
                    gp = 255
                elif gp < 0:
                    gp = 0
                elif bp > 255:
                    bp = 255
                elif bp < 0:
                    bp = 0
                self.img.putpixel((i,j),(rp,gp,bp))
        return self.img.save(self.nombre_img+"_brillo", "JPEG")

                
