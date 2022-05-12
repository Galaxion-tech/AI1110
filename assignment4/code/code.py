import numpy as np
from scipy.stats import bernoulli

#Practical
#Given data
P_A1= 0.8
P_B1= 0.7
P_AorB1=0.95

#Inclusion and Exclusion
P_AandB1=P_A1+P_B1-P_AorB1
print(P_AandB1)

#Theortical
N=10000000    #N=1000000
A= bernoulli.rvs(size = N,p=P_A1)
B= bernoulli.rvs(size=N,p=P_B1)

#adding corresponding element of A and B
S=np.add(A,B)

#S contain 2 only in position where A and B both have 1
num_AandB=np.count_nonzero(S == 2)

#probability of scoring in both exam
P_AandB1 = num_AandB/N
print(P_AandB1)
