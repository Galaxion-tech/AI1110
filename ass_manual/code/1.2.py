#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
import subprocess
import shlex
#end if



x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('../data/uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def cdf(x):
	return x

y=np.linspace(0,1,10)
cdf_plot=scipy.vectorize(cdf)
plt.plot(y.T,cdf_plot(y),'o',label="theory")
plt.plot(x.T,err,label="numerical")#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_U(x)$')

plt.legend(loc="best")
#if using termux
plt.savefig('../figs/uni_cdf.pdf')
plt.savefig('../figs/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ./figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
#plt.show() #opening the plot window
