#coding=UTF8
"""
El proposito de este experimento es graficar f(x) y e(x) para un alpha determinado
"""

from pylab import plt, legend
import numpy as np


x = np.arange(-2, 2, 0.05)
x2 = np.arange(0, 10, 0.05)

f_5 = x ** 2 - .05
f1 = x ** 2 - 1
f2 = x ** 2 - 2

e_5 = 1 / (x2 ** 2) - .05
e1 = 1 / (x2 ** 2) - 1
e2 = 1 / (x2 ** 2) - 2

plt.figure(1)
# plt.title("")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.plot(x, f_5, label=u"α = 0.5")
plt.plot(x, f1, label=u"α = 1")
plt.plot(x, f2, label=u"α = 2")
legend()

plt.figure(2)
# plt.title("e(x)")
plt.axis([0, 10, -4, 20])
plt.xlabel('x')
plt.ylabel('e(x)')
plt.grid(True)
plt.plot(x2, e_5, label=u"α = 0.5")
plt.plot(x2, e1, label=u"α = 1")
plt.plot(x2, e2, label=u"α = 2")
legend()

plt.show()
