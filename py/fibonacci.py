# -*- coding: utf-8 -*-
"""
Cálculo de elementos n-1 y n de la sucesión de Fibonacci
"""

# Input desde html
input = 2; # Corresponde al número de iteraciones 

# Inicialización de variables 
y1 = 1;         # Almacena valor del elemento asociado a iteración previa
y2 = 1;         # Almacena valor del elemento asociado a iteración actual
actual = 1;     # Almacena valor actual de la sucesión

if (input == 1):
   # Se entrega primer elemento y se menciona que el elemento anterior no existe
   print ('El primer elemento es: ', y2 , ', y el elemento anterior no existe') 
elif (input == 2):
   # Entrega de resultados
   print ('El elemento ', input , ' es: ', y2, ', y el elemento anterior es: ', y1) 
else: # n > 2
   # Comienza iteración
   n = input;   #Contador 
   while (n-2 >= 0):
       # Calculo nuevo término y actualizo las salidas
       actual = y1 + y2;
       y1 = y2;
       y2 = actual;
       # Reduzco el número de iteraciones restantes en 1
       n = n-1;     
   # Entrega de resultados
   print ('El elemento ', input , ' es: ', y2, ', y el elemento anterior es: ', y1) 