import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    arr1=np.array(x)
    x=np.mean(arr1)
    y=np.size(arr1)
    z=np.std(arr1,ddof=1)
    a=(x-mu0)/(z/(y**0.5))
    return a
    
    pass