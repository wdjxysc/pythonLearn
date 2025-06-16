# 1. merge() — 数据库风格的连接
import pandas as pd

# 示例数据
left = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
right = pd.DataFrame({'ID': [1, 2, 4], 'Age': [24, 27, 22]})

# 使用 merge 进行内连接
result = pd.merge(left, right, on='ID', how='inner')
print(result)



# 2. concat() — 沿轴连接
import pandas as pd

# 示例数据
df1 = pd.DataFrame({'A': [1, 2, 3]})
df2 = pd.DataFrame({'A': [4, 5, 6]})

# 行合并
result = pd.concat([df1, df2], axis=0, ignore_index=True)
print(result)


# 3. join() — 基于索引连接
import pandas as pd

# 示例数据
left = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
right = pd.DataFrame({'B': [4, 5, 6]}, index=[1, 2, 4])

# 使用 join 进行连接
result = left.join(right, how='inner')
print(result)



# 1. pivot_table() — 创建透视表
import pandas as pd

# 示例数据
data = {'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
        'Category': ['A', 'B', 'A', 'B'],
        'Sales': [100, 150, 200, 250]}
df = pd.DataFrame(data)

# 创建透视表
pivot_table = pd.pivot_table(df, values='Sales', index='Date', columns='Category', aggfunc='sum', fill_value=0)
print(pivot_table)


# 2. crosstab() — 创建交叉表
import pandas as pd

# 示例数据
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Region': ['North', 'South', 'North', 'South', 'West', 'East']}
df = pd.DataFrame(data)

# 创建交叉表
cross_table = pd.crosstab(df['Category'], df['Region'])
print(cross_table)


# 1. apply() — 应用函数到 DataFrame 或 Series 上
import pandas as pd

# 示例数据
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

# 定义自定义函数
def custom_func(x):
    return x * 2

# 在列上应用函数
df['A'] = df['A'].apply(custom_func)
print(df)


# 2. applymap() — 在整个 DataFrame 上应用函数
import pandas as pd

# 示例数据
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# 在 DataFrame 上应用自定义函数
df = df.applymap(lambda x: x ** 2)
print(df)


# 3. map() — 应用函数到 Series 上
import pandas as pd

# 示例数据
df = pd.DataFrame({'A': ['cat', 'dog', 'rabbit']})

# 使用字典进行映射
df['A'] = df['A'].map({'cat': 'kitten', 'dog': 'puppy'})
print(df)


