import numpy as np

#heads= 1
#tails= 0

#Number of Trials
N = 100000

#Distribution of data
distribution = np.random.randint(0,2,size = (N,10))

#number of heads
frequency_of_heads = np.count_nonzero(distribution == 1,axis=1)

#part 1
num_6heads = np.count_nonzero(frequency_of_heads == 6)
prob_6heads = num_6heads/N
print(prob_6heads) #answer close to 105/512
#part 2
num_atleast_6heads = np.count_nonzero(frequency_of_heads >=6)
prob_atleast_6heads = num_atleast_6heads/N
print(prob_atleast_6heads) #answer close to 193/512
#part 3
num_atmost_6heads = np.count_nonzero(frequency_of_heads <=6)
prob_atmost_6heads = num_atmost_6heads/N
print(prob_atmost_6heads) #answer close to 53/64