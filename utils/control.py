import numpy as np


def calc_input():
    v = 1.0
    yaw_rate = 0.1
    return np.array([[v, yaw_rate]]).T
