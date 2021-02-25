import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
import argparse
import viz


color="#3498db"
N_JOINT = 12 # total number of joint
RADIUS = 10 # space around the subject
parser = argparse.ArgumentParser()
parser.add_argument("-f","--file_dir",type=str,default="./test.txt",help="Enter the path of input file.")
parser.add_argument("-np","--is_npy",type=bool,default=False,help="Use NPY file input, CSV as default.")
parser.add_argument("-n","--number",type=int,default=1,help="Number of Pose in one screen at the same time.")

args = parser.parse_args()

f_dir = args.file_dir
num = args.number

if args.is_npy:
    pose_arr = np.load(f_dir)
else:
    pose_arr = np.loadtxt(f_dir, delimiter=',')

pose_arr = pose_arr.reshape(-1, num ,N_JOINT,3)

plt.rcParams['figure.figsize'] = (5*num, 5)
gs = gridspec.GridSpec(1, num) # 1 rows, n columns
gs.update(wspace=-0.00, hspace=0.05) # set the spacing between axes.
plt.axis('off')


for i in range(pose_arr.shape[0]):
    for n in range(num):
        x= pose_arr[i,n,:,0]
        y= pose_arr[i,n,:,1]
        z= pose_arr[i,n,:,2]
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

        ax.set_xlim3d([-RADIUS, RADIUS])
        ax.set_zlim3d([-RADIUS, RADIUS])
        ax.set_ylim3d([-RADIUS, RADIUS])
    plt.show()


print(pose_arr.shape)
