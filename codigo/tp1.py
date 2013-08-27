# coding=UTF-8
import collections
import os
from subprocess import check_output

def f(x, alpha):
    return x * x - alpha

def e(x, alpha):
    return 1 / (x * x) - alpha

class Experimento(object):
    # configuracion
    entradas = None
    funcion = None
    metodo = None
    criterio = None
    limite = None
    x0 = None
    x1 = None

    _has_run = False

    resultados = None

    def __init__(self, entradas=None, funcion=None, metodo=None, criterio=None, limite=None, x0=None, x1=None):
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

        if self.metodo == 'newton' and self.x0 and not self.x1:
            self.x1 = self.x0

        if not isinstance(self.entradas, collections.Iterable):
            raise ValueError(u"Entradas no es un iterable.")

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

        for alpha in self.entradas:
            final_args = ("%s" % arg for arg in [executable, alpha] + args)
            output = check_output(final_args)
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
        from pprint import pprint
        pprint(self.resultados)
