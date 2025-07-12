import numpy as np
from utils.params import NP


def initialize_states():
    x_est = np.zeros((4, 1))
    x_true = np.zeros((4, 1))
    x_dr = np.zeros((4, 1))
    px = np.zeros((4, NP))
    pw = np.ones((1, NP)) / NP
    h_x_est = x_est
    h_x_true = x_true
    h_x_dr = x_dr
    return x_est, x_true, x_dr, px, pw, h_x_est, h_x_true, h_x_dr
