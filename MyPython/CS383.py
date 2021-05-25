
import math
import numpy as np

# Numpy Array Prep
def shuffle_rows(data, seed=0):
    return np.random.RandomState(seed=seed).permutation(data)
def standardize(data, mean=None, std=None, return_stats=False):
    if type(mean) == type(None):
        mean = np.mean(data, axis=0)
    if type(std) == type(None):
        std  = np.std( data, axis=0, ddof=1)
    standardized_data = ((data - mean) / std)
    if return_stats:
        return standardized_data,  mean,  std
    else:
        return standardized_data
def add_bias(data):
    biased_data = np.ones((data.shape[0], data.shape[1]+1))
    biased_data[:, 1:] = data
    return biased_data

# Analysis
_SE = lambda y,y_hat: (y-y_hat)**2
_RM = lambda s,n: math.sqrt(s / n)
RMSE = lambda Y,Y_hat: None if (len(Y) != len(Y_hat)) else \
    _RM(sum([_SE(Y[i], Y_hat[i]) for i in range(len(Y))]), len(Y))
L1_distance = lambda a,b: sum([abs(ai-bi) for ai, bi in zip(a,b)])