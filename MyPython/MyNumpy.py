
import numpy as np

def Astr(A, indent=0):
    tabs = '\t' * indent
    return tabs + str(A).replace('\n', '\n'+tabs)

def is_raveled(A):
    return len(A.shape) == 1

def is_2d(A):
    return len(A.shape) == 2

def is_1Din2D(A):
    return is_2d(A) and (1 in A.shape)

def enforce_row(A):
    if is_raveled(A): return A.reshape(1, len(A))
    elif is_2d(A):
        if 1 not in A.shape: raise Exception("A must be 1xN or Nx1")
        return A.reshape(1, max(*A.shape))
    else: raise Exception("A must be a 1- or 2- dimensional array")
    
def enforce_column(A):
    if is_raveled(A): return A.reshape(len(A), 1)
    elif is_2d(A):
        if 1 not in A.shape: raise Exception("A must be 1xN or Nx1")
        return A.reshape(max(*A.shape), 1)
    else: raise Exception("A must be a 1- or 2- dimensional array")

def is_not_prob(A):
    return np.any(A > 1.0) or np.any(A < 0.0)

def savetxt(A, path):
    np.savetxt(path, A, delimiter=',')
