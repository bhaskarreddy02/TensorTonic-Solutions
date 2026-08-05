import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    arr1=np.array(X,dtype=float)
    mean=arr1.mean(axis=axis,keepdims=True)
    dev=arr1.std(axis=axis,keepdims=True)
    z=(arr1-mean)/(dev+eps)
    return z
    pass