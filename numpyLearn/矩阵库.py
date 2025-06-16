import numpy as np
 
a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('转置数组：')
print (a.T)



# matlib.empty() 函数返回一个新的矩阵，语法格式为：
import numpy.matlib 
import numpy as np
 
print (np.matlib.empty((2,2)))
# 填充为随机数据

# numpy.matlib.zeros() 函数创建一个以 0 填充的矩阵。
import numpy.matlib 
import numpy as np 
 
print (np.matlib.zeros((2,2)))

# numpy.matlib.ones()函数创建一个以 1 填充的矩阵。
import numpy.matlib 
import numpy as np 
 
print (np.matlib.ones((2,2)))


# numpy.matlib.eye() 函数返回一个矩阵，对角线元素为 1，其他位置为零。
import numpy.matlib 
import numpy as np 
 
print (np.matlib.eye(n =  3, M =  4, k =  0, dtype =  float))

# numpy.matlib.identity() 函数返回给定大小的单位矩阵。
import numpy.matlib 
import numpy as np 
 
# 大小为 5，类型位浮点型
print (np.matlib.identity(5, dtype =  float))

# numpy.matlib.rand() 函数创建一个给定大小的矩阵，数据是随机填充的。
import numpy.matlib 
import numpy as np 
 
print (np.matlib.rand(3,3))


# 矩阵总是二维的，而 ndarray 是一个 n 维数组。 两个对象都是可互换的。
import numpy.matlib 
import numpy as np  
 
i = np.matrix('1,2;3,4')  
print (i)

import numpy.matlib 
import numpy as np  
 
j = np.asarray(i)  
print (j)

import numpy.matlib 
import numpy as np  
 
k = np.asmatrix (j)  
print (k)