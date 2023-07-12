# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 18:18:54 2023

@author: Karen Ramos
"""
#Sentencias de control
#Funcion While (Mientras)
contar= int(input("Ingrese el numero al que contare: "))
contador=1
while contador <= contar:
    print(contador)
    contador+=1
    
contar1= int(input("Ingrese el numero al que contare: "))
contador1=1
while True:
    print(contador1)
    contador1+=1
    if contador1 > contar1:
        break  
#Ejercico 1
while True:
    x = input("Enter a number to count to: ")
    if x == 'q' or x == 'quit':
        break
    x = int(x)
    y = 1
    while True:
        print(y)
        y = y + 1
        if y > x:
            break
#Funciones en Python
def mensaje ():
    print("Ingrese un valor: ")
mensaje ()
a= input()
mensaje ()
b= input()
mensaje ()
c= input()
print(a+b+c)
#Funcion orientada a objetos
def saludo (nombre):
    print("Hola!,",nombre,"\n")
    saludo("Ana")
    saludo("Jose")
    saludo("Dilan")
    saludo()
#Revisar (Arriba)