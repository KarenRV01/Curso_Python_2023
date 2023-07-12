# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:13:51 2023

@author: User
"""

import pandas as pd
titulos= pd.read_csv('titles.csv')
print(titulos.head(10))
print("\n"*2)
elenco=pd.read_csv("cast.csv",encoding="utf-8")
print(elenco.head(10))
print(len(titulos))
#Cual fue la primer pelicula hecha titulada "romeo y julieta
consulta01=titulos[titulos.title=="Rameo and Juliet"].sort_values("year")
print(consulta01)
#listar todos las peliculas que contengan la palabra "Exorcist""
consulta02=titulos[titulos.title.str.contains("Exorcist")].sort_values("year")
print(consulta02)
consulta03=titulos[titulos.title.str.contains("driver")].sort_values("year")
print(consulta03)
print(elenco[elenco.name == "Robert De Niro"] )
#ordenadas de la mas vieja a la mas reciente.
print(titulos[titulos.title.str.contains("Exorcist")].sort_values('year'))
#Cuantas peliculas fueron hechas en el año 1950?
print(len( titulos[titulos.year == 1980] ))
#Cuantas peliculas fueron hechas en el año 1970?
print(len( titulos[titulos.year == 2020] ))
#Cuantas peliculas fueron hechas de 1950 a 1959
print(len( titulos[ (titulos.year >= 1950) & (titulos.year <= 1959) ] ))
print(len( titulos[ titulos.year // 10 == 195] ))
#En que años alguna pelicula llamada "Batman" se presento
print(titulos[ titulos.title == "Batman"])
print(titulos[ titulos.title == "Start Wars"])
print(titulos[titulos.title.str.contains("Star War")].sort_values('year'))
print(titulos[ titulos.year == 1973].head(1))
print(len( titulos[ (titulos.year >= 1980) & (titulos.year <= 2000)]))
#Cuantos roles o papeles hubo en la pelicula "The Godfather"
print(len( elenco[elenco.title == "The Godfather"] ))
#Cuantos papeles en la pelicula "The Godfather" no estan clasificados en algun valor "n"
c = elenco[elenco.title == "The Godfather"]
c = c[c.n.isnull()]
print(len( c ))

