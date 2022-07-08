#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import mpmath
import scipy
#if using termux
import subprocess
import shlex
#end if



x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('./gau.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def Q(x):
	return 0.5*mpmath.erfc(x/np.sqrt(2))
def cdf(x):
	F=1-Q(x)
	return F
cdf_plot= scipy.vectorize(cdf)
plt.plot(x.T,err,"o",label="numerical")#plotting the CDF
plt.plot(x.T,cdf_plot(x),label="theory")
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.legend(loc="best")
#if using termux
plt.savefig('../figs/gau_cdf.pdf')
plt.savefig('../figs/gau_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
#plt.show() #opening the plot window
