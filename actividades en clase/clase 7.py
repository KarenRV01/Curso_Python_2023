# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 18:43:53 2023

@author: User
"""

# -*- coding: utf8 -*-
import tostadas_pipo
from tostadas_pipo.utilidades import calculos as ca
from tostadas_pipo.utilidades.impuestos import impuesto_iva14 as imp14

monto = int(input("Introduzca un monto entero: "))
monto_suma = int(input("Introduzca un monto entero a sumar: "))

suma = imp14(monto) + ca.suma_total(monto_suma)

print ("Total a Facturar: {0} BsS, con IVA 14%.".format(suma))

