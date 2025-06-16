import pandas as pd

url = "https://static.jyshare.com/download/property-data.csv"
df = pd.read_csv(url)

print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())


# 以上例子中我们看到 Pandas 把 n/a 和 NA 当作空数据，na 不是空数据，不符合我们要求，我们可以指定空数据类型：
import pandas as pd

missing_values = ["n/a", "na", "--"]
df = pd.read_csv(url, na_values = missing_values)

print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())


# 接下来的实例演示了删除包含空数据的行。
import pandas as pd

df = pd.read_csv(url, na_values = missing_values)

new_df = df.dropna()

print(new_df.to_string())


# 如果你要修改源数据 DataFrame, 可以使用 inplace = True 参数:
import pandas as pd

df = pd.read_csv(url)

df.dropna(inplace = True)

print(df.to_string())

# 移除 ST_NUM 列中字段值为空的行：
import pandas as pd

df = pd.read_csv(url)

df.dropna(subset=['ST_NUM'], inplace = True)

print(df.to_string())



# 我们也可以 fillna() 方法来替换一些空字段：
import pandas as pd

df = pd.read_csv(url)

df.fillna(12345, inplace = True)

print(df.to_string())


# 使用 12345 替换 PID 为空数据：
import pandas as pd

df = pd.read_csv(url)

df['PID'].fillna(12345, inplace = True)

print(df.to_string())


# 使用 mean() 方法计算列的均值并替换空单元格：
import pandas as pd

df = pd.read_csv(url)

x = df["ST_NUM"].mean()

df["ST_NUM"].fillna(x, inplace = True)

print(df.to_string())



# 以下实例会格式化日期：
import pandas as pd

# 第三个日期格式错误
data = {
  "Date": ['2020/12/01', '2020/12/02' , '20201226'],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())


# 以下实例会替换错误年龄的数据：
import pandas as pd

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)

df.loc[2, 'age'] = 30 # 修改数据

print(df.to_string())


# 将 age 大于 120 的设置为 120:
import pandas as pd

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 200, 12345]    
}

df = pd.DataFrame(person)

for x in df.index:
  if df.loc[x, "age"] > 120:
    df.loc[x, "age"] = 120

print(df.to_string())



# 将 age 大于 120 的删除:
import pandas as pd

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)

for x in df.index:
  if df.loc[x, "age"] > 120:
    df.drop(x, inplace = True)

print(df.to_string())



# 以下实例演示了如何使用 duplicated() 方法来查找重复数据。
import pandas as pd

person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]  
}
df = pd.DataFrame(person)

print(df.duplicated())

df.drop_duplicates(inplace = True) # 删除重复数据
print(df)


# 填充缺失值：
import pandas as pd

# 示例数据
data = {'Name': ['Alice', 'Bob', 'Charlie', None],
        'Age': [25, 30, None, 35],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# 填充缺失的 "Age" 为均值
df['Age'].fillna(df['Age'].mean(), inplace=True)

print(df)


# 独热编码：
import pandas as pd

# 示例数据
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# 对 "City" 列进行 One-Hot 编码
df_encoded = pd.get_dummies(df, columns=['City'])

print(df_encoded)