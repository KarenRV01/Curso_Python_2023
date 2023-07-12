# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:23:44 2023

@author: User
"""

#CLASE 3
#Identificacion de variables
a= 5
b= 6.5
c= "numero"
d= True
print(a,b,c,d)
print(type(a))   #se usa type para ver si la variables es:int= numero entero, 
                 #float= numero decimal, str= categorico y bool= boleano
opt= 22//3       #Division entera
# Cadena de caracter concaquenacion
x= 5
exp= "cisco"*x
#"/n"*2  salto de linea 
str1= "CEC"
str2="EPN"
str3= "Curso de Python"
print(str1+str2+str3)   #signo + significa concatenar solo caracteres
print(str1,str2,str3) #para separar eñ texto concatenado, tambien sirve +space
#Funcion de conversion
#print("El valor de x es:" +x)  Es erroneo, por + solo caracteres y x es un valor numerico
print("El valor de x es:",x)    #correcto, no tiene conversion la variable
print("El valor de x es:"+ str(x)) #no modifica la variable
print(type(x))
#Visualizacion
pi=22/7
print(pi)
print("{:.2f}".format(pi))
print("{:.52f}".format(pi)) #Limite
#Listas, tuplas y diccenarios
#Lista []
l= [2,45.4,2,"ENP",True]
l2=[1,62,73.87,3,1]
print(l)
print(l2)
print(type(l))
print(l[0])
print(l[-1])
#print(l[-6])
l[2]=45
del l[4]
print(l2.count(1))
#Tuplas
t=(1,25.2,45,"True",False)
print(type(t))
print(t[0])
print(t[4])
print(t[-1])
#t[-1]=True del t[-1]  las tuplas no son modificables
#Diccionario
dic={1:"IDN","Nombre":"Juan",False:"Matricula","Apellido":"Mata","email":"Kl@false.com","mat":2,2:"IDN2"}
"""dic={1:"IDN","Nombre":"Juan",False:"Matricula","Apellido":"Mata",
"email":"Kl@false.com","mat":2,1:"IDN2"} No puede haber valores repetidos
 tanto en la llave como en el valor"""
print(dic[1])
print(dic["Nombre"])
dic["Tel"]="59339658254"
print(dic)
 

 






