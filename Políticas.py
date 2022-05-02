# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:08:56 2022

@author: Jaume
"""

import pandas as pd

url = "https://es.wikipedia.org/wiki/Anexo:Diputados_y_senadores_de_Espa%C3%B1a_desde_1977"

nombre = list(pd.read_html(url)[1]["Nombre"])

partido = list(pd.read_html(url)[1]["Partido político"])
 
designacion = list(pd.read_html(url)[1]["Elección / Designación"])

congreso = list(pd.read_html(url)[1]["Legislaturas en el Congreso"])

senado = list(pd.read_html(url)[1]["Legislaturas en el Senado"])

legislaturas = list(pd.read_html(url)[1]["Legislaturas en total"])

data = pd.DataFrame({"Nombre": nombre,
                     "Partido": partido,
                     "Designación": designacion,
                     "Congreso": congreso,
                     "Senado": senado,
                     "Legislaturas": legislaturas})

data.to_csv("Políticas.csv", index = False)