import numpy as np
import matplotlib.pyplot as plt


def f(x,k):
    if (x !=-1 ):
        num = x**2-2*x-3.0
        den = x+1.0
        fval = num/den   #basically fval is x-3 when x != -1
        return fval
    else:
        return k

fvec = np.vectorize(f)
x = np.linspace(-2,0,100)




##Input parameters
k = -3
plt.scatter(-1,-3,marker='o')
plt.plot(x,fvec(x,k),label='discontinuous, k = -3')
k = -4
plt.scatter(-1,-4,marker='o')
plt.plot(x,fvec(x,k),label='continuous, k = -4')

#
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()

plt.savefig("./continuous.jpg")
plt.show()

