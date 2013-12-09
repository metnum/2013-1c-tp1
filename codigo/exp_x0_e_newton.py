#coding=UTF8
"""
El proposito de este experimento es analizar la convergencia del método de
Newton para diferentes magnitudes de x0 y de alphas.

Graficaremos una escala logaritimica en x 10^-n..10^n y veremos cuantas
iteraciones tarda en converger.
"""

import itertools

from copy import deepcopy
from math import isnan
from pylab import plt, legend

from tp1 import Experimento


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


x0s = [10 ** n for n in drange(-10, 10, .1)]
alphas = [0.0000001, 0.0001, 0.5, 2, 1000, 1000000]

marker = itertools.cycle(('+', 'o', '*'))


class Newton(Experimento):
    metodo = 'newton'
    funcion = 'e'
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

    new_x0s = deepcopy(x0s)
    mi_newton = Newton(entradas=[alpha] * len(new_x0s), x0s=new_x0s)
    mi_newton.run()
    resultados[alpha] = mi_newton.resultados

for alpha in alphas:
    resultado = resultados[alpha]
    valores = [res['resultado'] for res in resultado]

    # distancia_a_resultado = [abs(x0 - resultado_real) for x0 in x0s]
    # plt.plot(distancia_a_resultado, [res['iteraciones'] for res in resultado], marker=marker.next(), linestyle='', label=u"α = %s" % alpha)

    plot_x0s = [tup[0] for tup in zip(x0s, valores) if not isnan(tup[1])]
    plot_iters = [tup[0]['iteraciones'] for tup in zip(resultado, valores) if not isnan(tup[1])]
    plt.plot(plot_x0s, plot_iters, label=u"α = %s" % alpha)  # , marker=marker.next(), linestyle='')

legend()
plt.show()
