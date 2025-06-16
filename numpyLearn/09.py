import numpy as np 

# NumPy 广播
# NumPy 广播是指在不同形状的数组之间进行算术运算时，NumPy 会自动扩展较小的数组以匹配较大数组的形状。
a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b 
print (c)

a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([0,1,2])
print(a + b)

# NumPy 广播的一个常见用法是将一维数组添加到二维数组的每一行。
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
bb = np.tile(b, (4, 1))  # 重复 b 的各个维度
print(a+bb)

