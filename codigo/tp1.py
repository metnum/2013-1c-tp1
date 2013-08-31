# coding=UTF-8
import collections
import os
from subprocess import check_output

def f(x, alpha):
    return x * x - alpha

def e(x, alpha):
    return 1 / (x * x) - alpha

class Experimento(object):
    """
    Clase que realiza experimentos para probar distintos resultados

    entradas: iterable de alfas
    funcion: funcion a calcular ('f' o 'e')
    metodo: algoritmo de aproximación ('n' o 's')
    criterio: criterio de detención ('i', 't', 'r', 'a')
    limite: argumento de limite para el criterio
    x0, x1: puntos iniciales de aproximación
    x0s, x1s: iterables de puntos iniciales de aproximación (uno por cada alfa)
    """
    entradas = None
    funcion = None
    metodo = None
    criterio = None
    limite = None
    x0 = None
    x0s = None
    x1 = None
    x1s = None

    _has_run = False

    resultados = None

    def __init__(self, entradas=None, funcion=None, metodo=None, criterio=None, limite=None, x0=None, x1=None, x0s=None, x1s=None):
        if entradas:
            self.entradas = entradas
        if funcion:
            self.funcion = funcion
        if metodo:
            self.metodo = metodo
        if criterio:
            self.criterio = criterio
        if limite:
            self.limite = limite
        if x0:
            self.x0 = x0
        if x1:
            self.x1 = x1
        if x0s:
            self.x0s = x0s
        if x1s:
            self.x1s = x1s

    def run(self):
        if self.resultados:  # ya se corrio
            return

        # chequeo que todos los valores sean correctos
        params = {}

        if self.funcion == "f":
            params['funcion'] = 'f'
        elif self.funcion == "e":
            params['funcion'] = 'e'
        else:
            raise ValueError(u"La funcion tiene que ser 'f' o 'e'.")

        if self.metodo == "newton":
            params['metodo'] = 'n'
        elif self.metodo == "secante":
            params['metodo'] = 's'
        else:
            raise ValueError(u"El metodo tiene que ser 'newton' o 'secante'.")

        if self.criterio == "iteraciones":
            params['criterio'] = 'i'
        elif self.criterio == "tiempo":
            params['criterio'] = 't'
        elif self.criterio == "relativo":
            params['criterio'] = 'r'
        elif self.criterio == "absoluto":
            params['criterio'] = 'a'
        else:
            raise ValueError(u"El criterio tiene que ser 'iteraciones', 'tiempo', 'relativo' o 'absoluto'.")

        if isinstance(self.limite, (float, int)):
            params['limite'] = self.limite
        else:
            raise ValueError(u"El limite tiene que ser un numero.")

        if self.x0:
            if isinstance(self.x0, (float, int)):
                params['limite'] = self.limite
            else:
                raise ValueError(u"El x0 tiene que ser un numero.")

        if self.x1:
            if isinstance(self.x1, (float, int)):
                params['limite'] = self.limite
            else:
                raise ValueError(u"El x1 tiene que ser un numero.")

        if self.metodo == 'secante' and self.x0 and not self.x1:
            raise ValueError(u"Hay que elegir tanto un x0 como un x1.")

        if self.x0 and self.x0s:
            raise ValueError(u"Se acepta un x0 o una lista en x0s, pero no ambas.")

        if self.metodo == 'newton' and self.x0 and not self.x1:
            self.x1 = self.x0

        #if not isinstance(self.entradas, collections.Iterable):
        #    raise ValueError(u"Entradas no es un iterable.")

        args = [
            params['funcion'],
            params['metodo'],
            params['criterio'],
            params['limite'],
        ]

        if self.x0:
            args.append(params['x0'])
            args.append(params['x1'])

        executable = os.path.join(os.getcwd(), "bin/tp1")

        self.resultados = []

        try:  # Para poder detener el test y poder ver resultados
            for alpha in self.entradas:
                prog_args = ["%s" % arg for arg in [executable, alpha] + args]

                if self.x0s:
                    prog_args.append(str(self.x0s.next()))
                    if self.x1s:
                        prog_args.append(str(self.x1s.next()))

                output = check_output(prog_args)
                segmentos = output.split("\n\n")
                if len(segmentos) == 3:
                    detalle, iteraciones, resultados = segmentos
                    iteraciones = map(lambda line: line.split(" ")[0], iteraciones.split("\n"))
                else:
                    detalle, resultados = segmentos
                    resultados = resultados.lstrip("\n")
                    iteraciones = []

                resultados = map(lambda line: line.split(" ")[0], resultados.split("\n"))
                resultado = float(resultados[0])
                iteraciones = int(resultados[1])
                absoluto = float(resultados[2])
                relativo = float(resultados[3])
                tiempo = float(resultados[4])

                self.resultados.append({
                    'alpha': alpha,
                    'iteraciones': iteraciones,
                    'resultado': resultado,
                    'absoluto': absoluto,
                    'relativo': relativo,
                    'tiempo': tiempo,
                })
        except KeyboardInterrupt:
            import sys
            sys.exc_clear()
