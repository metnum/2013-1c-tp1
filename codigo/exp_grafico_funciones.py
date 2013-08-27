# el proposito de este experimento es graficar f(x) y e(x) para un alpha
# determinado

from matplotlib import pyplot as plt
import numpy as np
from tp1 import e, f


x = np.arange(-2, 2, 0.05)

f_5 = x**2 - .05
f1 = x**2 - 1
f2 = x**2 - 2

e_5 = 1 / (x**2) - .05
e1 = 1 / (x**2) - 1
e2 = 1 / (x**2) - 2

plt.figure(1)
# plt.title("")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.plot(x, f_5)
plt.plot(x, f1)
plt.plot(x, f2)

plt.figure(2)
# plt.title("e(x)")
plt.axis([-2, 2, -4, 20])
plt.xlabel('x')
plt.ylabel('e(x)')
plt.grid(True)
plt.plot(x, e_5)
plt.plot(x, e1)
plt.plot(x, e2)

plt.show()

