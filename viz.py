import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec


def show3Dpose(vals, num, color,gs):
    for n in range(num):

        x= vals[n,:,0]
        y= vals[n,:,1]
        z= vals[n,:,2]
        ax = plt.subplot(gs[n], projection='3d')
        ax.plot(x, y, z, lw=2, c=color)

        if False:
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_zlabel("z")

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])

        ax.get_xaxis().set_ticklabels([])
        ax.get_yaxis().set_ticklabels([])
        ax.set_zticklabels([])

        RADIUS = 10 # space around the subject
        ax.set_xlim3d([-RADIUS, RADIUS])
        ax.set_zlim3d([-RADIUS, RADIUS])
        ax.set_ylim3d([-RADIUS, RADIUS])