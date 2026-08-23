import numpy as np

def covariance_matrix(X):
    X = np.asarray(X, dtype=float)
    centered = X - np.mean(X, axis=0)
    return centered.T @ centered / (X.shape[0] - 1)
