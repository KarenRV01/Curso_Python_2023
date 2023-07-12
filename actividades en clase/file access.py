# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:31:34 2023

@author: Karen Ramos
"""
archivo=open("devices.txt","a")
while True:
    newitem = input("Ingrese el nuevo dispositivo (o escriba 'exit' para salir): ")
    
    if newitem.lower() == "exit":
        print("¡Todo listo!")
        break
    
    archivo.write(newitem + "\n")
    print("Dispositivo agregado correctamente.")
    
archivo.close()


