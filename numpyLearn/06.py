import numpy as np
 
x = np.arange(5)  
print (x)

# 设置了 dtype
x = np.arange(5, dtype =  float)  
print (x)

x = np.arange(10,20,2)  # 从10开始到20，步长为2
print (x)

a = np.linspace(1,10,10) # 从1到10，生成10个等间距的数
print(a)

a = np.linspace(1,1,10)
print(a)

a = np.linspace(10, 20,  5)   # 从10到20，生成5个等间距的数，包含20
print(a)

a = np.linspace(10, 20,  5, endpoint =  False)   # 从10到20，生成5个等间距的数，不包含20
print(a)


a =np.linspace(1,10,10,retstep= True)
 
print(a)
# 拓展例子
b =np.linspace(1,10,10).reshape([10,1])
print(b)


# 默认底数是 10
a = np.logspace(1.0,  2.0, num =  10)  # 从10^1到10^2，生成10个等间距的数
print (a)


a = np.logspace(0,9,10,base=2) # 从2^0到2^9，生成10个等间距的数
print (a)
