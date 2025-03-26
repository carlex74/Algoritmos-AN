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

    def graficar(self, x_range=[-10, 10], y_range=[-10, 10]):
        # Crear la figura y los ejes
        fig, ax = plt.subplots()

        # Graficar la función
        ax.plot(self.x, self.y, color='blue', label='f(x)')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Gráfica de la función')
        ax.grid(True)
        ax.legend()

        # Agregar ejes X e Y
        ax.axhline(0, color='black', linewidth=1)  # Eje X
        ax.axvline(0, color='black', linewidth=1)  # Eje Y

        # Ajustar los valores de X e Y según el encuadre deseado
        ax.set_xlim(x_range[0], x_range[1])
        ax.set_ylim(y_range[0], y_range[1])

        # Retornar la figura y los ejes para manipulación futura
        return fig,ax
    
    def show_graf(self):
        plt.show()

    def save_graf(self,nombre):

        plt.savefig(nombre)


