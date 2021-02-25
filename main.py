import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
import argparse
import viz


parser = argparse.ArgumentParser()
parser.add_argument("-f","--file_dir",type=str,default="./test.txt",help="Enter the path of input file.")
parser.add_argument("-np","--is_npy",type=bool,default=False,help="Use NPY file input, CSV as default.")
parser.add_argument("-n","--number",type=int,default=1,help="Number of Pose in one screen.")

args = parser.parse_args()

N_JOINT = 12
f_dir = args.file_dir
n = args.number

if args.is_npy:
    pose_arr = np.load(f_dir)
else:
    pose_arr = np.loadtxt(f_dir, delimiter=',')

pose_arr = pose_arr.reshape(-1, n,N_JOINT,3)

fig = plt.figure( figsize=(9.6, 5.4))
gs = gridspec.GridSpec(1, n) # 1 rows, n columns
gs.update(wspace=-0.00, hspace=0.05) # set the spacing between axes.
plt.axis('off')

ax = plt.subplot(gs[0], projection='3d')



plt.show()


print(pose_arr.shape)
