import numpy as np
import matplotlib.pyplot as plt
from clases import Grafica

#Algoritmo de biseccion para encontrar la raiz de una funcion

xr=None
xl=1.50
xu=2.50

def funcion(x):
    return x**3 - 6*x**2 + 11*x - 6.1


def formuloBiseccion(xl,xu):
    return (xl+xu)/2


f_prueba=Grafica(funcion)
f_prueba.set_range(-10,10,500) #Setea el rango que matplotlib va a graficar de la funcion   
f_prueba.graficar([1,2.5],[-1,1]) #Grafica la funcion

for i in range(6):
    xr=formuloBiseccion(xl,xu)

    xr_graf= f_prueba.set_grafPunto(xr,funcion(xr),color='red') #Grafica el punto xr
    xl_graf= f_prueba.set_grafPunto(xl,funcion(xl),color='orange') #Grafica el punto xl
    xu_graf= f_prueba.set_grafPunto(xu,funcion(xu),color='orange') #Grafica el punto xu
    line_graf= f_prueba.set_line([xl,funcion(xl)],[xu,funcion(xu)]) #Grafica la linea que une los puntos xl y xu
    
    if funcion(xl)*funcion(xr)<0:
        xu=xr
    else:
        xl=xr

    print(f"xl: {xl} xu: {xu} xr: {xr} f(xr): {funcion(xr)}")
    f_prueba.save_graf(f"./logGrafica/biseccion-it{i}.png")

    xr_graf.remove()
    xl_graf.remove()
    xu_graf.remove()
    line_graf.pop(0).remove()