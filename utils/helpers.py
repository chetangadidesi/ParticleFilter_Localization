import numpy as np
import math


def gauss_likelihood(x, sigma):
    return 1.0 / math.sqrt(2.0 * math.pi * sigma ** 2) * math.exp(-x ** 2 / (2 * sigma ** 2))


def calc_covariance(x_est, px, pw):
    cov = np.zeros((4, 4))
    for i in range(px.shape[1]):
        dx = (px[:, i:i + 1] - x_est)
        cov += pw[0, i] * dx @ dx.T
    cov *= 1.0 / (1.0 - pw @ pw.T)
    return cov
