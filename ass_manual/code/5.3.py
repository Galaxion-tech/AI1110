import numpy as np
import matplotlib.pyplot as plt
import scipy
#if using termux
import subprocess
import shlex
#
randvar = np.loadtxt('../data/y.dat',dtype=float)

y=np.linspace(0,1,1000000)

plt.plot(y,randvar,'o')
plt.ylabel("$Y$")
plt.xlabel("$X$")
plt.grid()
plt.savefig('../figs/5.3.png')
#plt.savefig('../figs/5.3.eps')
#