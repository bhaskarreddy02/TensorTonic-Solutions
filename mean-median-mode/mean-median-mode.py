import numpy as np
from collections import Counter

def mean_median_mode(x):
    arr = np.array(x)

    mean = np.mean(arr)
    median = np.median(arr)

    counter = Counter(arr)
    mode = counter.most_common(1)[0][0]

    return mean, median, mode