#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "./header/coeffs.h"

int main(void){
    A_distribution("../data/a.dat",0.5);
    Y_distribution("../data/y.dat","../data/a.dat","../data/x.dat","../data/gau.dat");    
}