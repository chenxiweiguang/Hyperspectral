from PIL import Image
from pylab import *
from numpy import *
import matplotlib.pyplot as plt
import numpy as np
import cv2
img = cv2.imread('30mA-2.64V.bmp')
# 这里需要我们在当前目录下放一张名为cat.jpg的文件
# img.tofile('30mA-2.64V.raw')
#利用numpy中array的函数tofile将数据写入文件
#这时我们发现当前目录下新增了一个文件，名为cat.raw
# 我们先确定原图片的数据格式和大小，通道数，否者无法进行下一步转换
type = img.dtype#得到数据格式，如uint8和uint16等
width, height, channels = img.shape# 得到图像大小和通道数

# 利用numpydefromfile函数读取raw文件，并指定数据格式
imgData = np.fromfile('1p25c.raw', dtype=uint16)
# length= imgData.shape
length=len(imgData)
new_channels=int(length/(width*height))
# 利用numpy中array的reshape函数将读取到的数据进行重新排列。
imgData = imgData.reshape(width, new_channels, height)
imgData1 = imgData[:, 68, :]
imshow(imgData1)
figure()
x=np.array(imgData[575,:,350])
plt.plot(x)
figure()
max_list=[]
true_max=0
for a in range(783):
    for b in range(696):
        max = 0
        for c in imgData[a,:,b]:

            if c>max:
                max=c
        max_list.append(max)
        if max>true_max:
            true_max=max
true=[]
print(true_max)
for d in max_list:
    if d>true_max/3:
        e=1
    else:
        e=0
    true.append(e)

true=np.array(true).reshape(783,696)
imshow(true)
plt.show()
