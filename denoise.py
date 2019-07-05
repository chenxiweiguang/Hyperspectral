from PIL import Image
from pylab import *
from numpy import *

import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
img = cv2.imread('30mA-2.64V.bmp')
# 这里需要我们在当前目录下放一张名为cat.jpg的文件
# img.tofile('30mA-2.64V.raw')
#利用numpy中array的函数tofile将数据写入文件
#这时我们发现当前目录下新增了一个文件，名为cat.raw
# 我们先确定原图片的数据格式和大小，通道数，否者无法进行下一步转换
type = img.dtype#得到数据格式，如uint8和uint16等
width, height, channels = img.shape# 得到图像大小和通道数

b=['1p2dc25c','1p23dc25c','1p3dc25c']
c=['2dc25c','23dc25c','3dc25c']
path1="E:/高光谱数据/a190513/a25c"
path2="E:/高光谱数据/a190513/b25c"

for k in range(len(b)):
    print("正在处理第"+str(k+1)+"个文件中...")
# 利用numpydefromfile函数读取raw文件，并指定数据格式
    imgData1 = np.fromfile(os.path.join(path1,b[k])+'.raw', dtype=uint16)
    imgData2= np.fromfile(os.path.join(path1,c[0])+'.raw', dtype=uint16)
    # print(imgData1.shape,imgData2.shape)

    #数据大小补齐
    a=[]
    for j in range(36192):
        a = np.append(a, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    if len(imgData1)<283383360:
        imgData1=np.append(imgData1, a)
    if len(imgData2)<283383360:
        imgData2=np.append(imgData2, a)
    #去光学串扰
    imgData=imgData1-imgData2
    # print(imgData.shape)
    # print(imgData.dtype)
    for i in range(283383360):
        if imgData[i]>imgData1[i]:
            imgData[i]=0
    #生成新的文件
    # imgData=int16(imgData)
    imgData.tofile(os.path.join(path2,b[k])+'new.raw')
'''
    # length= imgData.shape
    length=len(imgData)
    new_channels=int(length/(width*height))
    # 利用numpy中array的reshape函数将读取到的数据进行重新排列。
    imgData = imgData.reshape(width, new_channels, height)
    # print(length,width, height, channels,new_channels)
    print(imgData)
    # 展示图像
    imgData0 = imgData[:, 68, :]
    imshow(imgData0)


    # cv2.imshow('img',imgData)
    # # 注意到这个函数只能显示uint8类型的数据，如果是uint16的数据请先转成uint8。否则图片显示会出现问题。**
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    #显示某一像素点的光谱曲线
    figure()
    x=np.array(imgData[600,:,350])
    plt.plot(x)
    show()
'''
