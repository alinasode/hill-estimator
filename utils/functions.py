import numpy as np


def hill_estimator(data):
    """
    Returns the Hill Estimators for some 1D data set.
    """
    sorted_data = sorted(data, reverse=True)

    # Pre-compute all the logged data and cumulative log sums
    log_sorted_data = np.log(sorted_data)  # log(Y_k)
    cumulative_sum = np.cumsum(log_sorted_data)  # sum log(Y_j)

    scales = np.arange(2, len(cumulative_sum) + 1)
    scaled_log_sums = cumulative_sum[1:] / scales  # estimator starts at k = 2

    hill_est = scaled_log_sums - log_sorted_data[1:]

    kappa = 1.0 / hill_est

    return kappa
