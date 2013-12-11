#coding=UTF8
"""
El proposito de este experimento es analizar la convergencia práctica de los
métodos.

"""

import itertools

from decimal import Decimal
from pylab import plt, legend

from tp1 import Experimento

alphas = [1000]

marker = itertools.cycle(('+', 'o', '*'))


plt.figure(1)
plt.xlabel('iteraciones')
plt.ylabel('xn / xn+1')
#plt.xscale('semilog')
#plt.semilogx()

# codigo


class Newton(Experimento):
    metodo = 'newton'
    funcion = 'f'
    criterio = 'relativo'
    limite = 0.1

mi_newton = Newton(entradas=alphas)
mi_newton.run()
res = mi_newton.resultados[0]
error_iters = [aprox - 1 / Decimal(res['resultado']) for aprox in res['detalle_iteraciones'][:-1]]
tupla_iters = zip(error_iters, error_iters[1:])
dif_rel = [iter[0] / iter[1] for iter in tupla_iters]
plt.plot(range(len(dif_rel)), dif_rel, label=u"f(x) mediante Newton", marker=marker.next(), linestyle='')

legend()
plt.show()
