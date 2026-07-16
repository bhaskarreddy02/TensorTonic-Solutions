import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    arr1=np.array(a)
    arr2=np.array(b)
    result1 = np.dot(arr1, arr2)
    res2=np.linalg.norm(arr1)
    res3=np.linalg.norm(arr2)
    if res2 * res3 ==0:
        return 0
    else:    
        x=(result1)/(res2 * res3)
        return x
    pass