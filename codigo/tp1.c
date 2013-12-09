#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include <float.h>
#include <math.h>
#include <sys/time.h>

#define MAX_ITER 1000

// Funciones para calcular el tiempo
struct timeval start, end;
void init_time()
{
    gettimeofday(&start,NULL);
}

double get_time()
{
    gettimeofday(&end,NULL);
    return (1000000*(end.tv_sec-start.tv_sec)+(end.tv_usec-start.tv_usec))/1000000.0;
}


 /* Funciones a encontrarles la raiz
 *
 * Se pide tres definiciones, dada g(x) se pide:
 * double g(double * x, double * alpha) --> g(x)
 * double g1(double * x, double * alpha) --> g'(x) (derivada)
 * double g_end(double * x, double * alpha) --> como obtener el resultado desde el x obtenido
 */

/****** f(x) ******/
double f(double * x, double * a) {
    // f(x) = x^2 - alpha
    return *x * *x - *a;
}

double f1(double * x, double * a) {
    // f'(x) = 2 x
    return *x * 2;
}
double f_end(double * x, double * a) {
    // f_end(x) = 1 / x
    // f(x) devuelve beta = sqrt(alpha) por lo que devolvemos la inversa
    return 1.0 / *x;
}

/****** e(x) ******/
double e(double * x, double * a) {
    // e(x) = 1 / x^2 - alpha
    return 1 / (*x * *x) - *a;
}

double e1(double * x, double * a) {
    // e'(x) = -2 / (x^3)
    return -2 / (*x * *x * *x);
}
double e_end(double * x, double * a) {
    // e_end(x) = 1 / x
    // e(x) devuelve 1 / sqrt(alpha) por lo que no hacemos nada
    return *x;
}

/* Metodos a utilizar para encontrar la raices
 *
 * Se piden dos definiciones para cada metodo:
 * metodo_start(x_prev, x_next, alpha) --> elije los valores x0 y x1
 * metodo_iter(x_prev, x_next, alpha, g, g1) --> realiza una iteracion
 */

/****** newton ******/
void newton_start(double * x_prev, double * x_next, double * alpha) {
    // No modifico los valores de entrada de x0 y x1
    return;
}

void newton_iter(double * x_prev, double * x_next, double * alpha, double (*g)(double *, double *), double (*g1)(double *, double *)) {
    // x_n+1 = x_n - g(x) / g'(x)
    *x_next = *x_prev - (*g)(x_prev, alpha) / (*g1)(x_prev, alpha);
    *x_prev = *x_next;
}

/****** secante ******/
void secante_start(double * x_prev, double * x_next, double * alpha) {
    // No modifico los valores de entrada de x0 y x1
    return;
}

void secante_iter(double * x_prev, double * x_next, double * alpha, double (*g)(double *, double *), double (*g1)(double *, double *)) {
    // x_n+1 = x_n - ( x_n - x_n-1 ) / ( g(x_n) - g(x_n-1) ) * g(x_n)
    double aux = *x_next;
    if (fabs(*x_next  - *x_prev) < DBL_MIN) {  // or DBL_EPSILON?
        // ya terminamos, sino dividimos por 0
        return;
    }
    *x_next = *x_next - (*x_next - *x_prev) / ( g(x_next, alpha) - g(x_prev, alpha) ) * g(x_next, alpha);
    *x_prev = aux;
}

/* Criterios a utilizar para parar
 *
 * Se pide una funcion que devuelva 1 para seguir o 0 para parar.
 * Tambien puede imprimir opcionalmente el resultado
 * int nombre_criterio(limite, x, alpha, iteraciones, tiempo, print_value)
 */

int iteraciones(double * limite, double x, double * alpha, int * iteraciones, double tiempo, int print_value) {
    if (print_value) {
        printf("%i iteraciones\n", *iteraciones);
    }
    if (*iteraciones < *limite) {
        return 1;
    } else {
        return 0;
    }
}

int absoluto(double * limite, double x, double * alpha, int * iteraciones, double tiempo, int print_value) {
    double error = 1 / (x * x) - *alpha;
    if (print_value) {
        printf("%.99f error absoluto\n", error);
    }
    if (fabs(error) >= *limite) {
        return 1;
    } else {
        return 0;
    }
}

int relativo(double * limite, double x, double * alpha, int * iteraciones, double tiempo, int print_value) {
    double error = ((1 / (x * x)) - *alpha) / *alpha;
    if (print_value) {
        printf("%.99f error relativo\n", error);
    }
    if (fabs(error) >= *limite) {
        return 1;
    } else {
        return 0;
    }
}

int tiempo(double * limite, double x, double * alpha, int * iteraciones, double tiempo, int print_value) {
    double error = ((1 / (x * x)) - *alpha) / *alpha;
    if (print_value) {
        printf("%.99f tiempo\n", get_time());
    }
    if (get_time() <= *limite) {
        return 1;
    } else {
        return 0;
    }
}


int main (int argc, char * argv[]) {

    // Me fijo que hayan dado un valor a calcular su raiz cuadrada
    if (argc < 5 ) {
        printf("Ejectuar ./tp1 <valor_de_alpha> <funcion> <metodo> <criterio_de_parada> <valor_de_fin_de_criterio> [x0 x1]\n");
        printf("Funciones -> f: f(x), e: e(x)\n");
        printf("Metodos -> n: newton, s: secante\n");
        printf("Criterio de parada -> i: iteraciones, t: tiempo, r: error relativo, a: error absoluto\n");
        exit(-1);
    }

    // Convierto <valor_de_alpha> a alpha
    char * end;
    double alpha = strtod(argv[1], &end);
    if (argv[1] == end) {
        printf("Error: El <valor_de_alpha> debe ser un double\n");
        exit(-1);
    }

    printf("Buscando 1 / sqrt(%f)\n", alpha);

    // Selecciono las funciones derivadas de e o f
    double (*g)(double *, double *);
    double (*g1)(double *, double *);
    double (*g_end)(double *, double *);

    if (strcmp(argv[2], "f") == 0) {
        // utilizo g = f
        g = f;
        g1 = f1;
        g_end = f_end;
        printf("Utilizando f(x)\n");
    } else if (strcmp(argv[2], "e") == 0) {
        // utilizo g = e
        g = e;
        g1 = e1;
        g_end = e_end;
        printf("Utilizando e(x)\n");
    } else {
        printf("Error: El valor de <funcion> debe ser f o e\n");
        exit(-1);
    }

    // Selecciono las funciones start e iter de newton o de secante
    void (*start)(double *, double *, double *);
    void (*iter)(double * x_prev, double * x_next, double * alpha, double (*g)(double *, double *), double (*g1)(double *, double *));

    if (strcmp(argv[3], "n") == 0) {
        // utilizo metodo = newton
        start = newton_start;
        iter = newton_iter;
        printf("Utilizando Newton\n");
    } else if (strcmp(argv[3], "s") == 0) {
        // utilizo metodo = secante
        start = secante_start;
        iter = secante_iter;
        printf("Utilizando Secante\n");
    } else {
        printf("Error: El valor de <metodo> debe ser n o s\n");
        exit(-1);
    }

    // Selecciono los criterios de parada
    int (*criterio)(double *, double, double *, int *, double, int);

    if (strcmp(argv[4], "i") == 0) {
        criterio = iteraciones;
        printf("Criterio de parada iteraciones");
    } else if (strcmp(argv[4], "a") == 0) {
        criterio = absoluto;
        printf("Criterio de parada error absoluto");
    } else if (strcmp(argv[4], "r") == 0) {
        criterio = relativo;
        printf("Criterio de parada error relativo");
    } else if (strcmp(argv[4], "t") == 0) {
        criterio = tiempo;
        printf("Criterio de parada tiempo");
    } else {
        printf("Error: El valor de <metodo> debe ser i, a, r o t\n");
        exit(-1);
    }

    // Cargo el limite
    double limite = strtod(argv[5], &end);
    if (argv[5] == end) {
        printf("Error: El <limite> debe ser un double\n");
        exit(-1);
    }
    printf(" con limite %f\n", limite);

    double x_prev = DBL_EPSILON; // Mi x0 con el cual empiezo
    double x_next = DBL_EPSILON + 0.0000000001;

    // Me fijo si uso las x_next y x_prev default o las que pidio el usuario
    if (argc == 8 || argc == 7) {
        x_prev = strtod(argv[6], &end);
        if (argv[6] == end) {
            printf("Error: El <x0> debe ser un double\n");
            exit(-1);
        }
        if (argc == 8) {
            x_next = strtod(argv[7], &end);
            if (argv[7] == end) {
                printf("Error: El <x1> debe ser un double\n");
                exit(-1);
            }
        }
    } else {
        // TODO: Inicializo x_prev y x_next
        // Las funciones ahora no hacen nada
        (*start)(&x_prev, &x_next, &alpha);
    }

    printf("Utilizando x0=%f y x1=%f\n", x_prev, x_next);

    // Terminado el preambulo, linea en blanco
    printf("\n");

    int i = 0;


    // Empiezo a contar el tiempo
    init_time();

    while ((*criterio)(&limite, (*g_end)(&x_next, &alpha), &alpha, &i, get_time(), 0) &&  i < MAX_ITER) {
        (*iter)(&x_prev, &x_next, &alpha, g, g1);
        printf("%.99f Iter\n", x_next);
        i++;
    }
    if (i == MAX_ITER) {
        // Devolver NaN si termine por MAX_ITER
        x_next = 0.0 / 0.0;
    }
    double tiempo_total = get_time();

    // Terminadas las iteraciones, linea en blanco
    printf("\n");

    printf("%.99f resultado\n", (*g_end)(&x_next, &alpha));
    iteraciones(&limite, (*g_end)(&x_next, &alpha), &alpha, &i, tiempo_total, 1);
    absoluto(&limite, (*g_end)(&x_next, &alpha), &alpha, &i, tiempo_total, 1);
    relativo(&limite, (*g_end)(&x_next, &alpha), &alpha, &i, tiempo_total, 1);
    tiempo(&limite, (*g_end)(&x_next, &alpha), &alpha, &i, tiempo_total, 1);

    return 0;
}

