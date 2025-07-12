import numpy as np

DT = 0.1
SIM_TIME = 65.0
MAX_RANGE = 20.0
NP = 100
NTh = NP / 2.0
show_animation = True

Q = np.diag([0.2]) ** 2
R = np.diag([2.0, np.deg2rad(40.0)]) ** 2
Q_sim = np.diag([0.2]) ** 2
R_sim = np.diag([1.0, np.deg2rad(30.0)]) ** 2

rf_id = np.array([[10.0, 0.0],
                  [10.0, 10.0],
                  [0.0, 15.0],
                  [-5.0, 20.0]])
