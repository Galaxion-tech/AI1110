import numpy as np

#part 1

#N = number of trials
N = 1000000

#sample output
sample = np.random.rand(N)
sample = 10*sample

#number of element in sample greater than 6 and less than 8
n_6_8 = np.count_nonzero((sample >=6) & (sample <=8))

#probability of getting number between 6 to 8
prob1 = n_6_8/N

# print answer near to 0.2
print(prob1)  


#part 2


#N = number of trails

#number of element in sample space greater than 5
n_5_10 = np.count_nonzero(sample > 5)

#probability of getting number between 6 to 8 if given number is already greater than 5
prob2 = n_6_8/n_5_10

#print answer near to 0.4
print(prob2)