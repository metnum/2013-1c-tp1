#coding=UTF8
"""
El proposito de este experimento es analizar la convergencia del método de
Newton para x0 == alpha
"""

import itertools

from copy import deepcopy
from decimal import Decimal
from math import isnan
from pylab import plt, legend

from tp1 import Experimento

alphas = [Decimal(10 ** (n * 2)) for n in range(-25, 25, 2)]

marker = itertools.cycle(('+', 'o', '*'))


class Newton(Experimento):
    metodo = 'secante'
    funcion = 'e'
    criterio = 'relativo'
    limite = 0.0001


plt.figure(1)
plt.xlabel(u'α')
plt.ylabel('iteraciones')
plt.semilogx()

# codigo

x0s = deepcopy(alphas)
x0s = [1 / x0 for x0 in x0s]
x1s = [2 * x0 for x0 in x0s]
mi_newton = Newton(entradas=alphas, x0s=x1s, x1s=x0s)
mi_newton.run()
resultado = mi_newton.resultados
valores = [res['resultado'] for res in resultado]
plot_alphas = [tup[0] for tup in zip(alphas, valores) if not isnan(tup[1])]
plot_iters = [tup[0]['iteraciones'] for tup in zip(resultado, valores) if not isnan(tup[1])]
plt.plot(plot_alphas, plot_iters, label=u"x0 = 1 / α, x1 = 2 * x0")


x0s = deepcopy(alphas)
x0s = [1 / (x0 * 10) for x0 in x0s]
x1s = [2 * x0 for x0 in x0s]
mi_newton = Newton(entradas=alphas, x0s=x0s, x1s=x1s)
mi_newton.run()
resultado = mi_newton.resultados
valores = [res['resultado'] for res in resultado]
plot_alphas = [tup[0] for tup in zip(alphas, valores) if not isnan(tup[1])]
plot_iters = [tup[0]['iteraciones'] for tup in zip(resultado, valores) if not isnan(tup[1])]
plt.plot(plot_alphas, plot_iters, label=u"x0 = 1 / (α * 10), x1 = 2 * x0")


mi_newton = Newton(entradas=alphas)
mi_newton.run()
resultado = mi_newton.resultados
valores = [res['resultado'] for res in resultado]
plot_alphas = [tup[0] for tup in zip(alphas, valores) if not isnan(tup[1])]
plot_iters = [tup[0]['iteraciones'] for tup in zip(resultado, valores) if not isnan(tup[1])]
plt.plot(plot_alphas, plot_iters, label=u"x0 = DBL_EPSILON, x1 = x0 + 0.0000000001")


mi_newton = Newton(entradas=alphas, x0=1, x1=1 + 0.00001)
mi_newton.run()
resultado = mi_newton.resultados
valores = [res['resultado'] for res in resultado]
plot_alphas = [tup[0] for tup in zip(alphas, valores) if not isnan(tup[1])]
plot_iters = [tup[0]['iteraciones'] for tup in zip(resultado, valores) if not isnan(tup[1])]
plt.plot(plot_alphas, plot_iters, label=u"x0 = 1, x1 = x0 + 0.00001")


mi_newton = Newton(entradas=alphas, x0=0.1, x1=0.1 + 0.00001)
mi_newton.run()
resultado = mi_newton.resultados
valores = [res['resultado'] for res in resultado]
plot_alphas = [tup[0] for tup in zip(alphas, valores) if not isnan(tup[1])]
plot_iters = [tup[0]['iteraciones'] for tup in zip(resultado, valores) if not isnan(tup[1])]
plt.plot(plot_alphas, plot_iters, label=u"x0 = 0.1, x1 = x0 + 0.00001")

plt.axvline(x=1, linestyle='--', label=u"α = 1")

legend()

# alphas = [10 ** n  for n in range(-10, 20, 1)]
# 
# plt.figure(2)
# plt.xlabel(u'α')
# plt.ylabel('iteraciones')
# plt.semilogx()
# 
# # codigo
# 
# x0s = deepcopy(alphas)
# mi_newton = Newton(entradas=alphas, x0s=x0s)
# mi_newton.run()
# resultado = mi_newton.resultados
# plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = α", marker='+', linestyle='')
# 
# x0s = deepcopy(alphas)
# x0s = [x0 / 2 for x0 in x0s]
# mi_newton = Newton(entradas=alphas, x0s=x0s)
# mi_newton.run()
# resultado = mi_newton.resultados
# plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = α / 2", marker='+', linestyle='')
# 
# mi_newton = Newton(entradas=alphas, x0=0.5)
# mi_newton.run()
# resultado = mi_newton.resultados
# plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = 0.5", marker='o', linestyle='')
# 
# mi_newton = Newton(entradas=alphas, x0=1)
# mi_newton.run()
# resultado = mi_newton.resultados
# plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = 1", marker='o', linestyle='')
# 
# mi_newton = Newton(entradas=alphas, x0=1000)
# mi_newton.run()
# resultado = mi_newton.resultados
# plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = 1000", marker='*', linestyle='')
# 
# mi_newton = Newton(entradas=alphas, x0=2000)
# mi_newton.run()
# resultado = mi_newton.resultados
# plt.plot(alphas, [res['iteraciones'] for res in resultado], label=u"x0 = 2000", marker='*', linestyle='')


legend()
plt.show()
