#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "./header/coeffs.h"

int main(void){
    int n=1000000;
    gaussian("../data/gau1.dat",n,12,2,1,1,1);
    gaussian("../data/gau2.dat",n,12,2,1,2,1);
    chi_square_distribution("../data/v.dat","../data/gau1.dat","../data/gau2.dat");
}