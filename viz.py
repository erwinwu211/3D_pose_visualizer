import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec

I   = np.array([0,1,2,0,4,5,0,7,8,9,8,11,12,8,14,15]) # start points
J   = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) # end points

def show3Dpose(vals, num, color,gs):
    for n in range(num):
        # x= vals[n,:,0]
        # y= vals[n,:,1]
        # z= vals[n,:,2]
        ax = plt.subplot(gs[n], projection='3d')
        
        for i in np.arange(len(I)):
            x, y, z = [np.array( [vals[n, I[i], j], vals[n, J[i], j]] ) for j in range(3)]
            ax.plot(x, z, -y, lw=2, c=color)

        if False:
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_zlabel("z")

        # ax.set_xticks([])
        # ax.set_yticks([])
        # ax.set_zticks([])

        ax.get_xaxis().set_ticklabels([])
        ax.get_yaxis().set_ticklabels([])
        ax.set_zticklabels([])

        RADIUS = 256 # space around the subject
        ax.set_xlim3d([-RADIUS, RADIUS])
        ax.set_zlim3d([-RADIUS, RADIUS])
        ax.set_ylim3d([-RADIUS, RADIUS])