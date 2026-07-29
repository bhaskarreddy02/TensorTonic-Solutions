import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if len(y)==0:
        return 0.0

    counts=np.bincount(y)
    probs=counts/len(y)

    probs=probs[probs>0]
    
    return float(-np.sum(probs * np.log2(probs)))
    pass