import matplotlib.pyplot as plt
import numpy as np

class Grafica():
    def __init__(self, funcion):

        self.funcion = funcion
        self.x=None
        self.y=None

    def set_range(self, a , b, puntos):
        
        #Se crea un rango de valores para x y Y que tomara la funcion
        rango=np.linspace(a,b,puntos)
        self.x=rango
        self.y=self.funcion(rango)
    

    def set_grafPunto(self, x , y, color='red'):

        return plt.scatter(x, y, color=color, s=25)  # s es el tamaño del punto


    def set_line(self, p1, p2):

       # Dibujar el segmento entre los puntos
        return plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='green', linestyle='--', linewidth=2)

    def graficar(self,x_range=[-10,10],y_range=[-10,10]):
    
        plt.plot(self.x, self.y, color='blue', label='f(x)')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gráfica de la función')
        plt.grid(True)
        plt.legend()

        # Agregar ejes X e Y
        plt.axhline(0, color='black', linewidth=1)  # Eje X
        plt.axvline(0, color='black', linewidth=1)  # Eje Y

        plt.xlim(x_range[0],x_range[1])  # Ajustar los valores de X según el encuadre deseado
        plt.ylim(y_range[0],y_range[1])  # Ajustar los valores de Y según el encuadre deseado

    
    def show_graf(self):
        plt.show()

    def save_graf(self,nombre):

        plt.savefig(nombre)


