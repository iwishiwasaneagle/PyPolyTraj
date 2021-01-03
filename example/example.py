import matplotlib.pyplot as plt
from pypolytraj import QuinticPolynomialTrajectory as Trajectory
import numpy as np

if __name__ == "__main__":
    pos = []
    dpos = []
    ddpos = []
    t_store = []
    dt = 0.01
    t = 0 

    wps = np.array([[0,0],[5,0],[5,5],[0,5], [0,0]])
    Ts = np.array([5,2,10,2,5])

    for wp_old, wp_next, T in zip(wps[:-1], wps[1:], Ts):

        trajectory = Trajectory(wp_old,wp_next,[0,0],[0,0],[0,0],[0,0],T)

        for ti in np.linspace(0, T, int(T/dt)):           
            pos.append(trajectory.position(ti))
            dpos.append(trajectory.velocity(ti))
            ddpos.append(trajectory.acceleration(ti))
            t_store.append(t+ti)

        t += ti

    pos = np.array(pos)
    dpos = np.array(dpos)
    ddpos = np.array(ddpos)

    plt.plot(pos[:,0], pos[:,1])

    plt.show()