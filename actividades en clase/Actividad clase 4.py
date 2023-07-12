# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:17:26 2023

Nombre: Karen Ramos: 
"""

#Actividad clase 4
nombre = input("Por favor, introduce tu nombre para aplicar al descuento: ")
apellido= input("por favor, ingresa tu apellido: ")
lugar= input("La ciudad en la que se encuentra es: ")
edad= input( "Cual es tu edad? ")
print("Hola, " + nombre + " Tu descuento se aplica al señor/a " + apellido + "! Bienvenido/a a Fybeca" + ". El lugar de tu ultima compra fue "+ lugar + " y tu edad es " + edad + " años. Fue un placer atenderte!")
edad=int(edad)
if edad >=0 and edad <= 17:
    print("Infante")
elif edad >=18 and edad <= 50:
     print("Adulto")
else:
     print("Anciano")
    

     