import numpy as np
import matplotlib.pyplot as plt

from utils.params import DT, SIM_TIME, show_animation, rf_id
from utils.plot_utils import plot_covariance_ellipse
from utils.control import calc_input
from utils.init import initialize_states
from observation import observation
from pf_localization import pf_localization


def main():
    print("Particle Filter Localization Simulation Started!")

    time = 0.0

    # Initialize states and particles
    x_est, x_true, x_dr, px, pw, h_x_est, h_x_true, h_x_dr = initialize_states()

    plt.figure()
    plt.pause(2)

    while time <= SIM_TIME:
        time += DT
        u = calc_input()

        x_true, z, x_dr, ud = observation(x_true, x_dr, u, rf_id)
        x_est, PEst, px, pw = pf_localization(px, pw, z, ud)

        # store history
        h_x_est = np.hstack((h_x_est, x_est))
        h_x_true = np.hstack((h_x_true, x_true))
        h_x_dr = np.hstack((h_x_dr, x_dr))

        if show_animation:
            plt.cla()
            plt.gcf().canvas.mpl_connect(
                'key_release_event',
                lambda event: [exit(0) if event.key == 'escape' else None])

            for i in range(len(z[:, 0])):
                plt.plot([x_true[0, 0], z[i, 1]], [x_true[1, 0], z[i, 2]], "-k")

            plt.plot(rf_id[:, 0], rf_id[:, 1], "*k")
            plt.plot(px[0, :], px[1, :], ".r")
            plt.plot(h_x_true[0, :], h_x_true[1, :], "-b", label="True")
            plt.plot(h_x_dr[0, :], h_x_dr[1, :], "-k", label="Dead reckoning")
            plt.plot(h_x_est[0, :], h_x_est[1, :], "-r", label="PF Estimate")
            plot_covariance_ellipse(x_est[0, 0], x_est[1, 0], PEst[0:2, 0:2])
            plt.axis("equal")
            plt.grid(True)
            plt.legend()
            plt.pause(0.001)


if __name__ == "__main__":
    main()
