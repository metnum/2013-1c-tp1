#include "stdio.h"
#include "stdlib.h"
#include "string.h"

double f(double * x, double * a) {
    // f(x) = x^2 - alpha
    return *x * *x - *a;
}

double f1(double * x, double * a) {
    // f'(x) = 2 x
    return *x * 2;
}

int main (int argc, char * argv[]) {

    // Me fijo que hayan dado un valor a calcular su raiz cuadrada
    if (argc < 2 ) {
        printf("Ejectuar ./f_x <valor_de_x>\n");
        exit(-1);
    }

    // Convierto la entrada a double
    char * end;
    double alpha = strtod(argv[1], &end);
    if (argv[1] == end) {
        printf("El valor de x debe ser un double\n");
        exit(-1);
    }
    printf("Busando sqrt(%f)\n", alpha);

    double x_prev = 100000000000.5; // Mi x0 con el cual empiezo
    double x_next;

    int i = 0;

    while (i < 45) {
        x_next = x_prev - f(&x_prev, &alpha) / f1(&x_prev, &alpha);
        x_prev = x_next;
        printf("%.99f\n", x_next);

        i++;
    }


    // Newton
    /*
    while (!parar) {
    }
    */

    return 0;
}
