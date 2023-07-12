# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 16:23:34 2023

@author: Karen Ramos
"""
#Ejercicio 1
def suma(*a):
    print("\nTipo de datos del argumento: ",
          type(a))
    sum=0
    for n in a:
        sum+=n
        #sum=sum+n
    print("Suma: ", sum)

suma(1)
suma(5,8)
suma(1,6)
suma(2,8,10)
suma(0,1)
suma(1,2)
suma(3,5)
suma(4,5,6,7)
suma(1,2,3,5,6)
suma(1,2,3,5,6,7,8,9,10)
suma(1,2,3,5,6,7,8,9,10,11,12,13,14)
suma(1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17)
#Ejercicio 2
def keyw(**datos):
    print("\nTipo de datos del argumento: ", 
          type(datos))
    for key, value in datos.items():
        print("{} is {}".format(key,value))
keyw(Firstname="Juan", Lastname="Dominguez",
    Age=42,Phone=123456789)
keyw(Firstname="John", Lastname="Wood", Email= "joh@mail",
    Age=25,Phone=987652314)
#Funcion lambda
impar= lambda num: num%2==0
print(impar(4))
sumar = lambda x,y: x+y
print(sumar(5,2))
#Modulo, Paquetes y Excepciones
#Modulos
#Metodo 1
import math
#import sys
#import 
print(math.sin(math.p1/2))
pi=22/7
def sin():
    return 0.999999999
print(math.pi)
print(sin())
print(pi)
#Metodo 2
#from math import sin,pi *
ai=sin(pi/2)
print(ai)
#Metodo 3 wiht as
#import math as m 
math.p1


















































