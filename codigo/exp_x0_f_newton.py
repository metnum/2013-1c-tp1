#coding=UTF8
"""
El proposito de este experimento es analizar la convergencia del método de
Newton para diferentes magnitudes de x0 y de alphas.

Graficaremos una escala logaritimica en x 10^-n..10^n y veremos cuantas
iteraciones tarda en converger.
"""

import itertools

from copy import deepcopy
from math import sqrt
from pylab import plt, legend

from tp1 import Experimento

x0s = [10 ** n for n in range(-10, 10)]
alphas = [0.0001, 0.5, 2, 1000]

marker = itertools.cycle(('+', 'o', '*'))


class Newton(Experimento):
    metodo = 'newton'
    funcion = 'f'
    criterio = 'relativo'
    limite = 0.0001


plt.figure(1)
plt.xlabel('x0')
plt.ylabel('iteraciones')
#plt.xscale('semilog')
plt.semilogx()

# codigo
# voy iterando por cada alpha
resultados = {}
for alpha in alphas:

    resultado_real = sqrt(alpha)

    new_x0s = deepcopy(x0s)
    mi_newton = Newton(entradas=[alpha] * len(new_x0s), x0s=new_x0s)
    mi_newton.run()
    resultados[alpha] = mi_newton.resultados

for alpha in alphas:
    resultado = resultados[alpha]
    # distancia_a_resultado = [abs(x0 - resultado_real) for x0 in x0s]
    # plt.plot(distancia_a_resultado, [res['iteraciones'] for res in resultado], marker=marker.next(), linestyle='', label=u"α = %s" % alpha)
    plt.plot(x0s, [res['iteraciones'] for res in resultado], marker=marker.next(), linestyle='', label=u"α = %s" % alpha)


legend()
plt.show()
