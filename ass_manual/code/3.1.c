#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void other_distribution(char * to, char * from){
    int i=0,c;
    FILE *fp1,*fp2;
    double x, temp=0.0;
    fp1 = fopen(to,"w");
    fp2 = fopen(from,"r");
//get numbers from file
    while(fscanf(fp2,"%lf",&x)!=EOF)
    {
//Count numbers in file
        temp = -2*log(1-x);
        fprintf(fp1,"%lf\n",temp);
//Add all numbers in file
    }
fclose(fp1);
fclose(fp2);
}
int main(void){
    other_distribution("../data/other.dat", "../data/uni.dat");
    return 0;
}
