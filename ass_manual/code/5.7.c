#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "./header/coeffs.h"

int main(int argc, char ** argv){
    double a;
    a=atof(argv[1]);
    A_distribution("../data/a.dat",a);
    Y_distribution("../data/y.dat","../data/a.dat","../data/x.dat","../data/gau.dat");
    X_cap_distribution("../data/x_cap.dat","../data/y.dat");
    return 0;
}