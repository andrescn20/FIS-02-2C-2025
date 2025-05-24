#Queremos un programa que me permita calcular el vector
# de campo eléctrico, en cualquier punto, generado por una carga
# puntual de cualquier signo. 

import math
import matplotlib.pyplot as plt

def plot_vector(x, y, campo_x, campo_y):
    plt.figure(figsize=(6,6))
    plt.quiver(x, y, campo_x, campo_y, angles='xy', scale_units='xy', scale=1, color='r')
    plt.xlim(x-10, x+10)
    plt.ylim(y-10, y+10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Vector de Campo Eléctrico')
    plt.grid(True)
    plt.show()

def plot_vectors(xs, ys, campos_x, campos_y):
    plt.figure(figsize=(6,6))
    plt.quiver(xs, ys, campos_x, campos_y, angles='xy', scale_units='xy', scale=1, color='r')
    plt.xlim(min(xs)-10, max(xs)+10)
    plt.ylim(min(ys)-10, max(ys)+10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Vectores de Campo Eléctrico')
    plt.grid(True)
    plt.show()

def calculoCampoElectrico(carga, coordenada_x, coordenada_y):
    constante_electrica = 9*(10**9)
    denominador = ((coordenada_x**2)+(coordenada_y**2))**(3/2)
    numerador = (constante_electrica*carga)
    factor_comun = numerador/denominador
    campo_x = factor_comun*coordenada_x
    campo_y = factor_comun*coordenada_y
    print(f'Campo Eléctrio en ({coordenada_x},{coordenada_y}):')
    print(f'Coordenada x: {campo_x:.4f}')
    print(f'Coordenada y: {campo_y:.4f}')
    plot_vector(coordenada_x, coordenada_y, campo_x, campo_y)

def calculoVariosCampos(carga, coordenadas):
    xs, ys, campos_x, campos_y = [], [], [], []
    for (x, y) in coordenadas:
        constante_electrica = 9*(10**9)
        denominador = ((x**2)+(y**2))**(3/2)
        numerador = (constante_electrica*carga)
        factor_comun = numerador/denominador
        campo_x = factor_comun*x
        campo_y = factor_comun*y
        print(f'Campo Eléctrio en ({x},{y}):')
        print(f'Coordenada x: {campo_x:.4f}')
        print(f'Coordenada y: {campo_y:.4f}')
        xs.append(x)
        ys.append(y)
        campos_x.append(campo_x)
        campos_y.append(campo_y)
    plot_vectors(xs, ys, campos_x, campos_y)

# calculoCampoElectrico((2*(10**-9)), 5, 3)
# Ejemplo de uso:
coordenadas = [
    (10, 0), (7, 7), (0, 10), (-7, 7), (-10, 0), (-7, -7), (0, -10), (7, -7),
    (5, 0), (3, 4), (0, 5), (-3, 4), (-5, 0), (-3, -4), (0, -5), (3, -4)
]
calculoVariosCampos((20*(10**-9)), coordenadas)

