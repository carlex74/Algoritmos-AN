import numpy as np
import matplotlib.pyplot as plt
from clases import Grafica

#Algoritmo de biseccion para encontrar la raiz de una funcion
def tolerancia(cantCifrasSign):
    return (0.5 * (10**(2-cantCifrasSign)))


def funcion(x):
    return x**3 - 6*x**2 + 11*x - 6.1

def formuloBiseccion(xl,xu):
    return (xl+xu)/2

def errorAproximado(xu,xl):
    return abs((xu-xl)/(xu+xl)) * 100


xr=None
xl=1.50
xu=2.50
cantCifrasSign = 6
tol = tolerancia(cantCifrasSign)
print(tol)
maxIteraciones = 25

f_prueba = Grafica(funcion)
f_prueba.set_range(-10,10,500) #Setea el rango que matplotlib va a graficar de la funcion   
fig,ax=f_prueba.graficar([xl,xu],[funcion(xl),funcion(xu)]) #Grafica la funcion
ea = errorAproximado(xu, xl)


if funcion(xl) * funcion(xu) < 0:
    i = 0
    while i <= maxIteraciones and ea > tol:

        xr = formuloBiseccion(xl,xu)

        xr_graf = f_prueba.set_grafPunto(xr,funcion(xr),color='red') #Grafica el punto xr
        xl_graf = f_prueba.set_grafPunto(xl,funcion(xl),color='orange') #Grafica el punto xl
        xu_graf = f_prueba.set_grafPunto(xu,funcion(xu),color='orange') #Grafica el punto xu
        line_graf = f_prueba.set_line([xl,funcion(xl)],[xu,funcion(xu)]) #Grafica la linea que une los puntos xl y xu
        
        if funcion(xl)*funcion(xr)<0:
            xu = xr
        else:
            xl = xr

        ea = errorAproximado(xu, xl)
    

        #Gráfica
        print(f"xl: {xl} xu: {xu} xr: {xr} ea: {ea} f(xr): {funcion(xr)}")
        f_prueba.save_graf(f"./logGrafica/biseccion-it{i}.png")

        xr_graf.remove()
        xl_graf.remove()
        xu_graf.remove()
        line_graf.pop(0).remove()

        i += 1

else:
    print("No se puede aplicar el método con seguridad")

print()
print(f"Raiz aproximada: {ea}")
print(f"Tolerancia: {tol}")
print(f"Error absoluto: {ea}")
print()

if ea == 0:
    print("Se encontró la raiz ")
elif ea < tol:
    print(f"Se encontró un valor aproximado por debajo de la tolerancia en la iteracion {i-1}")
else:
    print("Skibidi toilet")

