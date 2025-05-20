import numpy as np

def integral_raiz_x(a, b):
    #Area de un rect: delta_x * f(x)
    # f(x) = sqrt(x)
    delta_x = 0.000001
    area = 0
    for x in np.arange(a, b, delta_x):
        area += delta_x * ((x) ** 0.5)
    return area        

respuesta = integral_raiz_x(2, 7)
print(respuesta)