import matplotlib.pyplot as plt

# 读取图像文件，下载地址：https://static.jyshare.com/images/mix/tiger.jpeg
# img_array = plt.imread('tiger.jpeg')
img_array = plt.imread('f:/wdj/vscode/workspace/pyhonLearn/matplotlibLearn/tiger.jpeg')
tiger = img_array/255
#print(tiger)

# 显示图像
plt.figure(figsize=(10,6))

for i in range(1,5):
    plt.subplot(2,2,i)
    x = 1 - 0.2*(i-1)
    plt.axis('off') #hide coordinate axes
    plt.title('x={:.1f}'.format(x))
    plt.imshow(tiger*x)

plt.show()


import matplotlib.pyplot as plt

# 读取图像文件，下载地址：https://static.jyshare.com/images/mix/tiger.jpeg
# img_array = plt.imread('tiger.jpeg')
img_array = plt.imread('f:/wdj/vscode/workspace/pyhonLearn/matplotlibLearn/tiger.jpeg')

tiger = img_array/255
#print(tiger)

# 显示图像
plt.figure(figsize=(6,6))
plt.imshow(tiger[:300,100:400,:])
plt.axis('off')
plt.show()



# 如果我们将 RGB 颜色的绿色和蓝色坐标的数组元素设置为 0，我们将得到红色的图像：
import matplotlib.pyplot as plt

# 读取图像文件，下载地址：https://static.jyshare.com/images/mix/tiger.jpeg
# img_array = plt.imread('tiger.jpeg')
img_array = plt.imread('f:/wdj/vscode/workspace/pyhonLearn/matplotlibLearn/tiger.jpeg')
tiger = img_array/255
#print(tiger)

# 显示图像
red_tiger = tiger.copy()

red_tiger[:, :,[1,2]] = 0

plt.figure(figsize=(10,10))
plt.imshow(red_tiger)
plt.axis('off')
plt.show()