import numpy as np 

# 创建一个一维数组
x =  [1,2,3] 
a = np.asarray(x)  
print (a)

# 从列表创建一个一维数组
x =  (1,2,3) 
a = np.asarray(x)  
print (a)

# 从元组列表创建一个一维数组
x =  [(1,2,3),(4,5)] # 注意元组长度不一致
a = np.asarray(x, dtype=object) # 使用 dtype=object 处理不规则数组  
print (a)


x =  [(1,2,3),(4,5,6)] #  注意元组长度一致
a = np.asarray(x) # 默认使用 dtype=float  
print (a)

x =  [1,2,3] 
a = np.asarray(x, dtype =  float)  
print (a)

s =  b'Hello World' # 字节字符串
a = np.frombuffer(s, dtype =  'S1')  # 从字节字符串创建一维数组
print (a)

# 使用 range 函数创建列表对象  
list=range(5)
it=iter(list)
 
# 使用迭代器创建 ndarray 
x=np.fromiter(it, dtype=float)
print(x)




