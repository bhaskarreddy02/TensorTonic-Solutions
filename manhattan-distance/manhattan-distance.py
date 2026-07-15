import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    arr1=np.array(x)
    arr2=np.array(y)
    z=np.abs(arr1-arr2)
    return float(np.sum(z))
    pass