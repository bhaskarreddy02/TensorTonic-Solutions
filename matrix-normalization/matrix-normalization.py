import numpy as np

def matrix_normalization(matrix, axis=None, norm_type="l2"):
    x = np.asarray(matrix, dtype=float)

    if norm_type == "l1":
        norms = np.sum(np.abs(x), axis=axis, keepdims=True)
    elif norm_type == "l2":
        norms = np.sqrt(np.sum(x ** 2, axis=axis, keepdims=True))
    elif norm_type == "max":
        norms = np.max(np.abs(x), axis=axis, keepdims=True)
    else:
        raise ValueError("Invalid norm_type")

    # Avoiding division by zero
    safe_norms = np.where(norms == 0, 1, norms)

    return x / safe_norms