#coding=UTF8
"""
El proposito de este experimento es analizar la convergencia del método de
Newton para x0 == alpha
"""

import itertools

from copy import deepcopy
from decimal import Decimal
from pylab import plt, legend

from tp1 import Experimento

alphas = [Decimal(10 ** (n * 2)) for n in range(-25, 25, 2)]

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
x0s = [1 / x0 for x0 in x0s]
mi_newton = Newton(entradas=alphas, x0s=x0s)
mi_newton.run()
resultado = mi_newton.resultados
plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = 1 / α")

mi_newton = Newton(entradas=alphas)
mi_newton.run()
resultado = mi_newton.resultados
plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = DBL_EPSILON")

mi_newton = Newton(entradas=alphas, x0=1)
mi_newton.run()
resultado = mi_newton.resultados
plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = 1")

mi_newton = Newton(entradas=alphas, x0=1000)
mi_newton.run()
resultado = mi_newton.resultados
plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = 1000")


legend()

alphas = [Decimal(10 ** n)  for n in range(-10, 20, 1)]

plt.figure(2)
plt.xlabel(u'α')
plt.ylabel('iteraciones')
plt.semilogx()

# codigo

x0s = deepcopy(alphas)
x0s = [1 / x0 for x0 in x0s]
mi_newton = Newton(entradas=alphas, x0s=x0s)
mi_newton.run()
resultado = mi_newton.resultados
plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = 1 / α", marker='+', linestyle='')

x0s = deepcopy(alphas)
x0s = [2 / x0 for x0 in x0s]
mi_newton = Newton(entradas=alphas, x0s=x0s)
mi_newton.run()
resultado = mi_newton.resultados
plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = 2 / α", marker='+', linestyle='')

mi_newton = Newton(entradas=alphas, x0=0.5)
mi_newton.run()
resultado = mi_newton.resultados
plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = 0.5", marker='o', linestyle='')

mi_newton = Newton(entradas=alphas, x0=1)
mi_newton.run()
resultado = mi_newton.resultados
plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = 1", marker='o', linestyle='')

mi_newton = Newton(entradas=alphas, x0=1000)
mi_newton.run()
resultado = mi_newton.resultados
plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = 1000", marker='*', linestyle='')

mi_newton = Newton(entradas=alphas, x0=2000)
mi_newton.run()
resultado = mi_newton.resultados
plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = 2000", marker='*', linestyle='')


legend()
plt.show()
