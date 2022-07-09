#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
import subprocess
import shlex
#end 

fcap= np.loadtxt("../data/x_cap.dat",dtype=float)
fx= np.loadtxt("../data/x.dat",dtype=float )

def error(x,x_cap,flag):
    if (flag==1):
        den = np.count_nonzero(x==1)
        num = np.count_nonzero((x_cap==-1)*(x==1))
    else :
        den = np.count_nonzero(x==-1)
        num = np.count_nonzero((x_cap==1)*(x==-1))
    return num/den
p1=error(fx,fcap,1)
p2=error(fx,fcap,-1)
print(p1)
print(p2)