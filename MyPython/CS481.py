
import numpy as np

# Stabilizes a Markov Matrix
STABILIZATION_BOUNDARY = 10 * 1000
def stabilize(M, Limit=STABILIZATION_BOUNDARY):
    M_prev = M
    M_curr = M @ M
    n = 1
    while not np.array_equal(M_prev, M_curr):
        M_prev = M_curr
        M_curr = M_curr @ M
        n += 1
        if n > STABILIZATION_BOUNDARY:
            break
    return M_prev, n
