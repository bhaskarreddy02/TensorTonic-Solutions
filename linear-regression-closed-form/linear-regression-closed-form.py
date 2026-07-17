import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    arr1=X
    arr2=y
    transpose=np.transpose(arr1,axes=None)
    z=np.dot(transpose,arr1)
    inverse=np.linalg.inv(z)
    t=np.dot(inverse,transpose)
    return np.dot(t,arr2)
    
    pass