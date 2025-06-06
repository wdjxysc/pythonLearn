import numpy as np

a = np.arange(24)
print(a.ndim)  # 输出数组的维度
a = a.reshape(2, 3, 4)  # 重塑数组为2x3x4的形状
print(a.ndim)  # 输出重塑后的数组的维度
print(a)  # 输出数组的形状


a = np.array([[1,2,3],[4,5,6]])  
print (a.shape)

a = np.array([[1,2,3],[4,5,6]]) 
a.shape =  (3,2)  
print (a)


a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(2,3)  
print (b)

# 数组的 dtype 为 int8（一个字节）  
x = np.array([1,2,3,4,5], dtype = np.int8)  
print (x.itemsize)
 
# 数组的 dtype 现在为 float64（八个字节） 
y = np.array([1,2,3,4,5], dtype = np.float64)  
print (y.itemsize)


x = np.array([1,2,3,4,5])  
print (x.flags)