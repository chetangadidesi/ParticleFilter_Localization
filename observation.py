from utils.params import MAX_RANGE, Q_sim, R_sim
from motion import motion_model
import numpy as np
import math


def observation(x_true, xd, u, rf_id):
    x_true = motion_model(x_true, u)

    z = np.zeros((0, 3))
    for i in range(len(rf_id[:, 0])):
        dx = x_true[0, 0] - rf_id[i, 0]
        dy = x_true[1, 0] - rf_id[i, 1]
        d = math.hypot(dx, dy)
        if d <= MAX_RANGE:
            dn = d + np.random.randn() * Q_sim[0, 0] ** 0.5
            zi = np.array([[dn, rf_id[i, 0], rf_id[i, 1]]])
            z = np.vstack((z, zi))

    ud1 = u[0, 0] + np.random.randn() * R_sim[0, 0] ** 0.5
    ud2 = u[1, 0] + np.random.randn() * R_sim[1, 1] ** 0.5
    ud = np.array([[ud1, ud2]]).T

    xd = motion_model(xd, ud)

    return x_true, z, xd, ud
