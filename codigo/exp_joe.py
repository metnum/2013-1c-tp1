from matplotlib import pyplot as plt
from math import sqrt
from tp1 import Experimento

# secante vs newton
# comparar cantidad de iteraciones
# funcion f(x)
# criterio error relativo > 0.001

alpha = 0.00001
rango = [10**n + sqrt(alpha) for n in range(-5,5)]
class Newton05(Experimento):
    entradas = rango
    funcion = 'f'
    criterio = 'relativo'
    limite = 0.01

alpha = 10000
rango2 = [10**n + sqrt(alpha) for n in range(-5,5)]
class Newton2(Experimento):
    entradas = rango2
    funcion = 'f'
    criterio = 'relativo'
    limite = 0.01

newton_0_5 = Newton05(metodo='newton')
newton_0_5.run()

newton_2 = Newton2(metodo='newton')
newton_2.run()

plt.figure(1)
plt.title("comparacion de iteraciones")
plt.xlabel('alpha')
plt.ylabel('iteraciones')
plt.plot(rango, [res['iteraciones'] for res in newton_0_5.resultados])
plt.plot(rango2, [res['iteraciones'] for res in newton_2.resultados])

plt.show()
