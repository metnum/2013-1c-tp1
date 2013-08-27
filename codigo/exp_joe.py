from matplotlib import pyplot as plt
from tp1 import Experimento

# secante vs newton
# comparar cantidad de iteraciones
# funcion f(x)
# criterio error relativo > 0.001

rango = range(1, 10000, 10)

class MiExp(Experimento):
    entradas = rango
    funcion = 'f'
    criterio = 'relativo'
    limite = 0.01

newton = MiExp(metodo='newton')
secante = MiExp(metodo='secante')

newton.run()
secante.run()

plt.figure(1)
plt.title("comparacion de tiempo")
plt.xlabel('alpha')
plt.ylabel('tiempo ms')
plt.grid(True)
plt.plot(rango, [res['tiempo'] * 1000  for res in newton.resultados])
plt.plot(rango, [res['tiempo'] * 1000 for res in secante.resultados])

plt.figure(2)
plt.title("comparacion de iteraciones")
plt.xlabel('alpha')
plt.ylabel('iteraciones')
plt.plot(rango, [res['iteraciones'] for res in newton.resultados])
plt.plot(rango, [res['iteraciones'] for res in secante.resultados])

plt.show()
