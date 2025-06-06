# NumPy 切片和索引
import numpy as np

a = np.arange(10)
s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
print (a[s])
print (s)

a = np.arange(10)  
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)

a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
b = a[5] # 获取索引为 5 的元素
print(b)

a = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
print(a[2:]) # 从索引 2 开始到结尾

a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
print(a[2:5]) # 从索引 2 到索引 5（不包括 5）


a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
# 从某个索引处开始切割
print(a[1:])

a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print('start------')
print (a[...,1])   # 第2列元素  ...表示省略的维度
print (a[1,...])   # 第2行元素
print (a[...,1:])  # 第2列及剩下的所有元素