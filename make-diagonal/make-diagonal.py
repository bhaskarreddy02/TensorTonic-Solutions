import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    arr1=np.array(v)
    length=len(arr1)
    print(f"shape =({length},{length}, diagonal ={list(arr1)}")
    return np.diag(arr1)
    
    pass
