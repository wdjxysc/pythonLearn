# NumPy 高级索引
import numpy as np 
 
x = np.array([[1,  2],  [3,  4],  [5,  6]])  
y = x[[0,1,2],  [0,1,0]] # 通过行索引和列索引获取元素
# 这里的 [0,1,2] 是行索引， [0,1,0] 是列索引
print (y)

# 以下实例获取了 4X3 数组中的四个角的元素。 行索引是 [0,0] 和 [3,3]，而列索引是 [0,2] 和 [0,2]。
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print ('我们的数组是：' )
print (x)
print ('\n')
rows = np.array([[0,0],[3,3]]) # 行索引
cols = np.array([[0,2],[0,2]]) # 列索引
# 通过行索引和列索引获取四个角的元素
y = x[rows,cols]  
print ('这个数组的四个角元素是：')
print (y)

a = np.array([[1,2,3], [4,5,6],[7,8,9]])
b = a[1:3, 1:3]
c = a[1:3,[1,2]]
d = a[...,1:]
print(b)
print(c)
print(d)

# NumPy 布尔索引 返回一个一维数组
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print ('我们的数组是：')
print (x)
print ('\n')
# 现在我们会打印出大于 5 的元素  
print  ('大于 5 的元素是：')
print (x[x >  5])

# 以下实例使用了 ~（取补运算符）来过滤 NaN。
a = np.array([np.nan,  1,2,np.nan,3,4,5])  
print (a[~np.isnan(a)])

# 以下实例演示如何从数组中过滤掉非复数元素。
a = np.array([1,  2+6j,  5,  3.5+5j])  
print (a[np.iscomplex(a)])



x = np.arange(9)
print(x)
# 一维数组读取指定下标对应的元素
print("-------读取下标对应的元素-------")
x2 = x[[0, 6]] # 使用花式索引
print(x2)

print(x2[0])
print(x2[1])


x=np.arange(32).reshape((8,4))
print(x)
# 二维数组读取指定下标对应的行
print("-------读取下标对应的行-------")
print (x[[4,2,1,7]])

# 传入倒序索引数组
x=np.arange(32).reshape((8,4))
print (x[[-4,-2,-1,-7]])

# 二维数组读取指定下标对应的行和列
x=np.arange(32).reshape((8,4))
print (x[np.ix_([1,5,7,2],[0,3,1,2])])
