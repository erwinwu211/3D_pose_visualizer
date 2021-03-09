import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
import argparse
from viz import show3Dpose
import glob
import cv2

color="#3498db"
N_JOINT = 17 # total number of joint

parser = argparse.ArgumentParser()
parser.add_argument("-i","--file_dir",type=str,default="./test.txt",help="Enter the path of input pose file.")
parser.add_argument("-p","--img_dir",type=str,default="./imgs",help="Enter the path of input img folder.")
parser.add_argument("-npy","--is_npy",type=bool,default=False,help="Use NPY file input, CSV as default.")
parser.add_argument("-n","--number",type=int,default=1,help="Number of Pose in one screen at the same time.")

args = parser.parse_args()

f_dir = args.file_dir
num = args.number

img_dir = args.img_dir
img_list = glob.glob(img_dir+'/*.png')
print(len(img_list))
if args.is_npy:
    pose_arr = np.load(f_dir)
else:
    pose_arr = np.loadtxt(f_dir, delimiter=',')

pose_arr = pose_arr.reshape(-1, num ,N_JOINT,3)
print(pose_arr)
plt.rcParams['figure.figsize'] = (5*num, 5)
gs = gridspec.GridSpec(1, num) # 1 rows, n columns
gs.update(wspace=-0.00, hspace=0.05) # set the spacing between axes.
plt.axis('off')

for i in range(pose_arr.shape[0]):
    show3Dpose(pose_arr[i],num,color,gs)
    frame = cv2.imread(img_list[i])
    frame = cv2.resize(frame,(512,512))
    cv2.imshow('frame',frame)
    plt.show()


print(pose_arr.shape)
