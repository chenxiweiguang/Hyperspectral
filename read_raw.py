from PIL import Image
from pylab import *
from numpy import *
import matplotlib.pyplot as plt
import numpy as np
import cv2
img = cv2.imread('30mA-2.64V.bmp')
# 这里需要我们在当前目录下放一张30mA-2.64V.bmp的文件
# img.tofile('30mA-2.64V.raw')
#利用numpy中array的函数tofile将数据写入文件
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
print(length,width, height, channels,new_channels)
print(imgData)
# 展示图像
imgData1 = imgData[:, 68, :]
imshow(imgData1)


# cv2.imshow('img',imgData)
# # 注意到这个函数只能显示uint8类型的数据，如果是uint16的数据请先转成uint8。否则图片显示会出现问题。**
# cv2.waitKey()
# cv2.destroyAllWindows()

#显示某一像素点的光谱曲线
figure()
x=np.array(imgData[575,:,350])
plt.plot(x)
show()


