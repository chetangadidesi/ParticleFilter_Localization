import matplotlib.pyplot as plt
from utils.angle import rot_mat_2d
import math
import numpy as np


def plot_covariance_ellipse(x, y, cov, chi2=3.0, color='--r'):
    eig_val, eig_vec = np.linalg.eig(cov)
    big_ind = 0 if eig_val[0] >= eig_val[1] else 1
    small_ind = 1 - big_ind

    a = math.sqrt(chi2 * max(eig_val[big_ind], 0))
    b = math.sqrt(chi2 * max(eig_val[small_ind], 0))
    angle = math.atan2(eig_vec[1, big_ind], eig_vec[0, big_ind])

    t = np.arange(0, 2 * math.pi + 0.1, 0.1)
    px = a * np.cos(t)
    py = b * np.sin(t)

    fx = rot_mat_2d(angle) @ np.vstack([px, py])
    plt.plot(fx[0] + x, fx[1] + y, color)
