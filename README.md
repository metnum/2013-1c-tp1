2013-1c-tp1
===========

Tp del primer cuatrimetre del 2013

ROADMAP
=======

CODIGO
------

### general

* decidir e implementar la interfaz de entrada a utilizar en los ejecutables
  * numero de entrada
  * criterio de parada
    * cantidad de iteraciones
    * error relativo
    * error absoluto?
    * cercania al resultado esperado
    * tiempo de ejecución?
  * metodo
    * newton
    * biseccion
    * punto fijo
    * secante
  * eleccion de x0 y x1 (opcional)
* decidir el formato del output de cada corrida
  * resultado
  * num iteraciones
  * tiempo de ejecución (en ms?)
  * error absoluto
  * error relativo
  * cercania con el resultado esperado

### f_x

* unificar f / f' directamente o probar con -O3

### e_x

* abstraer newton de f_x
* implementar secante
* escribir e y e'

INFORME
-------

* Que queremos responder?
  * Por método
    * elección de parada
    * elección de x0 y x1
  * Entre métodos con cual nos quedamos
    * tiempo de ejecución (orden de convergencia)
    * precisión en el resultado (que tipo?)

EXPERIMENTOS
------------

* Sobre una misma corrida de numeros comparar diferentes criterios de parada (todos)
  * Normalizar por tiempo de ejecución
  * Verificar por diferentes tamaños de input (muy grandes y muy chicos)
  * Comprar precisión en el resultado (que tipo?)
* Graficar orden de convergencia de cada metodo con datos reales
* Mismas corridas entre los métodos para e_x
  * con los parametros ajustados anteriormente
