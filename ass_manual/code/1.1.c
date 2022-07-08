#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "./header/coeffs.h"

int  main(void) //main function begins
{
 
//Uniform random numbers
//uniform("uni.dat", 1000000);

//Gaussian random numbers
gaussian("../data/gau1.dat", 1000000,1,1);

//Mean of uniform
//printf("%lf",mean("uni.dat"));
return 0;
}