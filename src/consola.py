#-*- coding: utf-8 -*-
"""
  Proceso Digital de Imágenes 2018-1
  :description :programa en consola
  :author: Luis Pablo Mayo Vega

"""
import sys
from escalagrises import FiltroGrises
from colores import FiltroColores
from brillo import FiltroBrillo

class Console:

    def __init__(self, args):
        self.filtro = args[1] # filtro a aplicar
        if len(args) > 3:
            # si el filtro recibe un parametro aparte
            self.mode = args[2]
            self.filename = args[3]
        else:
            self.filename = args[2] # nombre del archivo
       

    def handler(self):
        """
        Recibe una lista con las opciones elegidas por el usuario
        y se encarga de generar los parametros correspondientes para cada filtro.
        La lista es de la forma [filtro, modo (opcional), nombre_de_archivo]
        """
        # Filtros con modos
        if self.filtro == "grisrgb":
            # escala de grises con un valor de RGB
            img = FiltroGrises(self.filename).grisRGB(self.mode)
        elif self.filtro == "brillo":
            img = FiltroBrillo(self.filename).brillo(int(self.mode))
        # Filtros sin modos
        elif self.filtro == "grisprom":
            # gris por promedio
            img = FiltroGrises(self.filename).grisPorPromedio()

        elif self.filtro == "griscons":
            # gris por las constantes dadas
            img = FiltroGrises(self.filename).grisConstante()
            
        elif self.filtro == "grisrb":
            # gris por promedio de rojo y azul
            img = FiltroGrises(self.filename).grisMezclaRB()

        elif self.filtro == "grisgb":
            # gris por promedio de verde y azul
            img = FiltroGrises(self.filename).grisMezclaGB()

        elif self.filtro == "grisrg":
            # gris por promedio de rojo y verde
            img = FiltroGrises(self.filename).grisMezclaRG()

        elif self.filtro == "rojo":
            # filtro rojo
            img = FiltroColores(self.filename).rojo()
                
        elif self.filtro == "verde":
            # filtro verde
            img = FiltroColores(self.filename).verde()

        elif self.filtro == "azul":
            img = FiltroColores(self.filename).azul()

        elif self.filtro == "azar":
            img = FiltroColores(self.filename).azar()

            img.show()
        else:
            print ("Opción incorrecta, no se pudo ejecutar el programa")
        
        

                
OPCIONES=""" Uso: python consola.py <filtro> <opción> <ruta-del-archivo>
             
             Filtros:
                    grisprom : Tonos de gris por promedio
                    griscons : Tonos de gris por constantes dadas
                    grisrgb <opción> : Tonos de gris a partir de uno de los valores RGB
                             Opciones : {"r", "g", "b"}
                    grisrb   : Tonos de gris a partir del promedio de rojo y azul
                    grisgb   : Tonos de gris a partir del promedio de verde y azul
                    grisrg   : Tonos de gris a partir del promedio de rojo y verde
                    rojo     : Filtro rojo
                    verde    : Filtro verde
                    azul     : Filtro azul
                    azar     : Filtro aleatorio de rojo, verde o azul
                    brillo <opción> : Filtro de cambio de brillo
                             Opciones: valores de -128 a 128
            
         """

if len(sys.argv) > 1:
    cons = Console(sys.argv)
    cons.handler()
else:
    print(OPCIONES)
