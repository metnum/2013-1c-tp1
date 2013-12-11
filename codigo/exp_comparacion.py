#coding=UTF8
"""
El proposito de este experimento es analizar la convergencia del método de
Newton para x0 == alpha
"""

import itertools

from copy import deepcopy
from pylab import plt, legend

from tp1 import Experimento

alphas = [10 ** (n * 2) for n in range(-25, 25, 2)]

marker = itertools.cycle(('+', 'o', '*'))


class Newton(Experimento):
    metodo = 'newton'
    funcion = 'f'
    criterio = 'relativo'
    limite = 0.0001


plt.figure(1)
plt.xlabel(u'α')
plt.ylabel('iteraciones')
plt.semilogx()

# codigo

x0s = deepcopy(alphas)
mi_newton = Newton(entradas=alphas)
mi_newton.run()
resultado = mi_newton.resultados
plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"f(x) Newton")

mi_newton = Newton(entradas=alphas, funcion='e')
mi_newton.run()
resultado = mi_newton.resultados
plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"e(x) Newton")

mi_newton = Newton(entradas=alphas, funcion='e', metodo='secante')
mi_newton.run()
resultado = mi_newton.resultados
plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"e(x) Secante")


legend()

alphas = [10 ** (n * 2) for n in range(-25, 25, 2)]

replicar = 2
tiempos = {
        'fn': [],
        'en': [],
        'es': [],
}

plt.figure(2)
plt.xlabel(u'α')
plt.ylabel('tiempo (s)')
plt.semilogx()

for i in range(replicar):
    print '%s / %s' % (i, replicar)
    x0s = deepcopy(alphas)
    mi_newton = Newton(entradas=alphas)
    mi_newton.run()
    resultado = mi_newton.resultados
    tiempos['fn'].append([res['tiempo'] for res in resultado])

    mi_newton = Newton(entradas=alphas, funcion='e')
    mi_newton.run()
    resultado = mi_newton.resultados
    tiempos['en'].append([res['tiempo'] for res in resultado])

    mi_newton = Newton(entradas=alphas, funcion='e', metodo='secante')
    mi_newton.run()
    resultado = mi_newton.resultados
    tiempos['es'].append([res['tiempo'] for res in resultado])

plt.plot(alphas, [sum(i) / replicar for i in zip(*tiempos['fn'])], label=u"f(x) Newton")
plt.plot(alphas, [sum(i) / replicar for i in zip(*tiempos['en'])], label=u"e(x) Newton")
plt.plot(alphas, [sum(i) / replicar for i in zip(*tiempos['es'])], label=u"e(x) Secante")

legend()
plt.show()
