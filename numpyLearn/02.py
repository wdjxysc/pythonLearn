import numpy as np

dt = np.dtype(np.int32)
print(dt)


# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt = np.dtype('i4')
print(dt)

# 字节顺序标注
dt = np.dtype('<i4')
print(dt)

dt = np.dtype([('age',np.int8)]) 
print(dt)

a = np.array([(10,),(20,),(30,)], dtype = dt) 
print(a)

a = np.array([(10,),(20,),(30,)], dtype = dt) 
print(a['age'])

# 这是一个数据类型
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
print(student)

a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print(a)