import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    arr1=[]
    arr2=[]
    
    if num_classes is None:
        num_classes = max(y) + 1
        for i in y:
            arr1=np.zeros(num_classes)
            arr1[i]=1
            arr2.append(arr1)
        return np.asarray(arr2)
    else:
        for i in y:
            arr1=np.zeros(num_classes)
            arr1[i]=1
            arr2.append(arr1)
        return np.asarray(arr2)

    pass