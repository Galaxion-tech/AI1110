def function(x):
    return x*x*x
def double_derivate_function(x):
    return 6*x

eta = 10
sigma = 2

estimate = function(eta)+double_derivate_function(eta)*sigma*sigma/2
print(estimate)