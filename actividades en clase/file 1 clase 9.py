# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 18:55:44 2023

@author: User
"""
lista=[]
archivo=open("devices.txt")
for elemento in archivo:
    elemento=elemento.strip() 
    lista.append(elemento)
archivo.close()
print(elemento)

