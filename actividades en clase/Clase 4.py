# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 17:20:32 2023

@author: Karen Ramos
"""

#Funcion Input Obtener informacion de variables de forma dinamica
nombre= input("Ingrese el nombre: ")
edad= int(input("Ingrese su edad: "))
edad= float(edad)
#Ejemplo
nombre1 = input("Por favor, introduce tu nombre para aplicar al descuento: ")
print("Hola, " + nombre1 + "! Bienvenido/a a Fybeca.")
apellido= input("por favor, ingresa tu apellido: ")
print("Un gusto señor/a "  + apellido + " gracias por preferirnos.")
lugar= input("La ciudad en la que se encuentra es: ")
print("Desde la ciudad de " + lugar + ". Gracias por visitarnos.")
edad1= input( "Cual es tu edad? ")
print("Mi edad es "+ edad1 + " años.")
#Funcion condicional
#Simple
print("Inicio")
datos=100
nativa=20
if nativa==datos:
    print("Las VLAN son iguales")
else:
    print("Las VLAN son diferentes")
    
print("fin")
#Multiple con elif
peso= float(input("Ingrese su peso en kg " ))
if peso >= 0.0 and peso <= 50.01:
    print("bajo peso")
elif peso > 50.1 and peso <=72.01:
    print("peso normal")
else:
    print("Sobre peso")
#Sentencia de control de repeticion 
for item in range(10):
    print(item)
for a in range(1,10+1,1):
     print(a)
for u in range(10,1-1,-1):
    print(u)
l=["R1","R2","R3","S1","S2","S3","AP1","FW1"]
for elemento in l:
    #print(elemento)   mostrara los elementos de forma vertical
    print(elemento, end=" ")
    #print(elemento, end="*") mostrara los elemntos de forma horizontal y en " " depedne el espacio
#Sentencia de control de repeticion convinado con if
l=["R1","R2","R3","S1","S2","S3","AP1","FW1","Pc","Celular"]
"""for elemento in l:
    if "R" in elemento:
        print(elemento)
lr=[]
for elemento in l:
    if "R" in elemento:
        lr.append(elemento)
ls=[]
for elemento in l:
    if "S" in elemento:
        ls.append(elemento)
la=[]
for elemento in l:
    if "A" in elemento:
        la.append(elemento)
ld=[]
for elemento in l:
    if "F" in elemento:
        ld.append(elemento) """
#Otra forma 
lr=[]
ls=[]
la=[]
ld=[]
for elemento in l:
    if "R" in elemento:
        lr.append(elemento)
    if "S" in elemento:
            ls.append(elemento)
    elif "A" and "F" in elemento:
             la.append(elemento)
    else:
        ld.append(elemento)
print(lr,ls,la,ld)






























