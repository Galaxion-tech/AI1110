#include <stdio.h>
#include <stdlib.h>

double mean(char *str)
{
    int i=0,c;
    FILE *fp;
    double x, temp=0.0;

    fp = fopen(str,"r");
    //get numbers from file
    while(fscanf(fp,"%lf",&x)!=EOF)
    {
    //Count numbers in file
        i=i+1;
    //Add all numbers in file
        temp = temp+x;
    }
    fclose(fp);
    temp = temp/(i-1);
    return temp;
}
double var(char *str, double m){

    int i=0,c;
    FILE *fp;
    double x, temp=0.0;

    fp = fopen(str,"r");

    while(fscanf(fp,"%lf",&x)!=EOF){
        i=i+1;
        temp = temp+ (x-m)*(x-m);
    }
    fclose(fp);
    temp = temp/(i-1);
    return temp;
}
int main(void){
    char * path= "../data/uni.dat";
    double m=mean(path);
    double v=var(path,m);
    printf("%lf\n%lf\n",m,v);
}