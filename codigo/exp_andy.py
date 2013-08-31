#coding: utf8
from matplotlib import pyplot as plt
from tp1 import Experimento
import math
import json
import itertools
import os

# Métodos:
#
# f(x) por Newton
# f(x) por secante -- No prioritario
# e(x) por Newton
# e(x) por secante
#
# Estudios
# - Cantidad de iteraciones hasta convergencia general(rangos amplios (cerca a
# cero, intervalos regulares, números grandes))
# - Criterios de parada (valores selectos)
#   (Para estos dos probablemente se puede argumentar que el tiempo es
#   proporcional a las iteraciones y evitarse gráficos)
#   - Error absoluto (acorde a valores selectos)
#        - Cantidad de iteraciones y tiempo hasta converger
#   - Error relativo (un par de niveles de precisión para los valores)
#        - Cantidad de iteraciones p/converger
# - Número de iteraciones para convergencia dependiendo de distancia a alpha
# (cambiando la distancia a alpha por órden de magnitud)
# (valores selectos)
#
# Inputs:
# - Muy chicos
# - Regulres intermedios
# - Muy grandes

# Intervalos de prueba
def chicos():
    """
    Casos chicos de alfa
    """
    def make_chico():
        start = 1 * 10 ** (-5)
        end = 1 * 10 ** (-3)
        step = 1 * 10 ** (-5)

        iters = 0
        a = start
        while a < end:
            yield a
            a += step
            iters += 1
            if iters % 100 == 0:
                print("%s iterations, a=%s, end=%s" % (iters, a, end))
        raise StopIteration
    return make_chico()


def regulares():
    """
    Casos "regulares" de alfa, de 1 a 10000, en incrementos fijos
    """
    def make_regular():
        start = 1
        end = 10000
        step = 1

        a = start
        iters = 0
        while a < end:
            yield a
            a += step
            iters += 1
            if iters % 100 == 0:
                print("%s iterations, a=%s, end=%s" % (iters, a, end))
        raise StopIteration
    return make_regular()


def grandes():
    """
    Casos "grandes" de todo tiempo, arrancando en 10e4 hasta 10e12 en intervalos que incrementan logaritmicamente
    """
    def make_grande():
        start = 1 * 10 ** (8)
        end = 1 * 10 ** (10)
        step = 1 * 10 ** (8)

        iters = 0
        a = start
        while a < end:
            yield a
            a += step
            iters += 1
            if iters % 100 == 0:
                print("%s iterations, a=%s, end=%s" % (iters, a, end))
        raise StopIteration
    return make_grande()


def fijo(alfas):
    """
    Genera los x0s cercanos para un conjunto de parámetros
    El valor es 0 + epsilon para poder ser utilizado al resolver secantes
    """
    def make_fijos(alfas):
        for alfa in alfas:
            yield 1 * 10 ** (-7)
        raise StopIteration
    return make_fijos(alfas)


def fijo_x1(alfas):
    def make_fijos(alfas):
        for alfa in alfas:
            yield alfa
        raise StopIteration
    return make_fijos(alfas)


def cercanos(alfas):
    def make_cercanos(alfas):
        for alfa in alfas:
            result = math.sqrt(alfa)
            yield result - 0.5
        raise StopIteration
    return make_cercanos(alfas)

def cercanos_x1(alfas):
    def make_cercanos(alfas):
        for alfa in alfas:
            result = math.sqrt(alfa)
            yield result + 0.5
        raise StopIteration
    return make_cercanos(alfas)

def normales(alfas):
    def make_normales(alfas):
        for alfa in alfas:
            yield alfa - alfa/8
        raise StopIteration
    return make_normales(alfas)

def normales_x1(alfas):
    def make_normales(alfas):
        for alfa in alfas:
            yield alfa + alfa/8
        raise StopIteration
    return make_normales(alfas)

def distantes(alfas):
    def make_distantes(alfas):
        for alfa in alfas:
            yield alfa / 2
        raise StopIteration
    return make_distantes(alfas)

def distantes_x1(alfas):
    def make_distantes(alfas):
        for alfa in alfas:
            yield alfa * 1.5
        raise StopIteration
    return make_distantes(alfas)

# Tests de intervalos
funcion = ['f']
metodos = ['newton', 'secante']  # Newton, Secante, F
intervalos = {'chicos': chicos, 'regulares': regulares, 'grandes': grandes}
#x0s = {'fijo': fijo, 'cercanos': cercanos} #, 'normales': normales, 'distantes': distantes}
#x1s = {'fijo': fijo_x1, 'cercanos': cercanos_x1} # 'normales': normales_x1, 'distantes': distantes_x1}
x0s = {'cercanos': cercanos, 'fijo': fijo}
x1s = {'cercanos': cercanos_x1, 'fijo': fijo}
detencion = 'relativo',
detencion_args = (0.01, 0.0001, 0.000001)

def make_experimentos(params_list):
    """
    Toma una lista de listas de argumentos para el experimento,
    los realiza, y guarda los gráficos de las mismas.
    """
    for params in params_list:
        intervalo = list(intervalos[params[2]]())
        experimento = Experimento(
            funcion=params[0], metodo=params[1], entradas=intervalo,
            criterio=params[3], limite=params[4], x0s=x0s[params[5]](intervalo), x1s=x1s[params[5]](intervalo))
        experimento.name = '-'.join(map(str, params))

        # Obtener x0 y x1 para alpha
        experimento_filename = 'resultados/' + experimento.name + '.json'
        if os.path.exists(experimento_filename):
            print "Salteando test %s..." % experimento.name
            continue

        with open(experimento_filename, 'w') as datafile:
            try:
                print "Corriendo tests para experimento %s..." % experimento.name
                experimento.run()
                json.dump(experimento.resultados, datafile, indent=4)

                # Make plots
                fig1 = plt.figure(1)
                plt.title(experimento.name.replace('-', ', '))
                plt.xlabel('alpha')
                plt.ylabel('tiempo ms')
                plt.grid(True)
                plt.plot(intervalo, [res['tiempo'] * 1000 for res in experimento.resultados])
                fig1.savefig('resultados/' + 'tiempo-' + experimento.name + '.png')
                plt.close()

                fig2 = plt.figure(2)
                plt.title(experimento.name.replace('-', ', '))
                plt.xlabel('alpha')
                plt.ylabel('error relativo')
                plt.grid(True)
                plt.plot(intervalo, [res['relativo'] for res in experimento.resultados])
                fig2.savefig('resultados/' + 'relativo-' + experimento.name + '.png')
                plt.close()

                fig3 = plt.figure(3)
                plt.title(experimento.name.replace('-', ', '))
                plt.xlabel('alpha')
                plt.ylabel('iteraciones')
                plt.grid(True)
                plt.plot(intervalo, [res['iteraciones']for res in experimento.resultados])
                fig3.savefig('resultados/' + 'iteraciones-' + experimento.name + '.png')
                plt.close()
            except KeyboardInterrupt:
                print "Saliendo del programa. Experimento actual: %s..." % experimento.name
                exit(1)


make_experimentos(list(itertools.product(
    funcion[0], metodos, intervalos, detencion, detencion_args, x0s)))
