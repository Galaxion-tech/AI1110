#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "./header/coeffs.h"

int main(int argc, char ** argv){
    double y;
    y=atof(argv[1]);
    //X_distribution("../data/x.dat");
    rayleigh("../data/rayleigh.dat",y);
    Y_distribution("../data/y.dat","../data/rayleigh.dat","../data/x.dat","../data/gau.dat");
    X_cap_distribution("../data/x_cap.dat","../data/y.dat");
    return 0;
}