import numpy as np

def bernoulli_pmf_and_moments(x, p):
    x = np.asarray(x, dtype=int)
    pmf = np.where(x == 1, p, 1.0 - p).astype(float)
    mean = float(p)
    variance = float(p * (1.0 - p))
    return {"pmf": pmf, "mean": mean, "variance": variance}
