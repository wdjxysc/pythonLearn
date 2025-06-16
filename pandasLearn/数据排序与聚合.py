import pandas as pd

# 示例数据
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)

# 按照 "Age" 列的值进行降序排序
df_sorted = df.sort_values(by='Age', ascending=False)
print(df_sorted)


# 按照行索引进行排序
df_sorted_by_index = df.sort_index(axis=0)
print(df_sorted_by_index)


# groupby() 示例:
import pandas as pd

# 示例数据
data = {'Department': ['HR', 'Finance', 'HR', 'IT', 'IT'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Salary': [50000, 60000, 55000, 70000, 75000]}

df = pd.DataFrame(data)

# 按照部门分组，并计算每个部门的平均薪资
grouped = df.groupby('Department')['Salary'].mean()
print(grouped)


# 按照部门分组，并计算每个部门的薪资的平均值和总和
grouped_multiple = df.groupby('Department').agg({'Salary': ['mean', 'sum']})
print(grouped_multiple)


# 按照部门分组后，按薪资降序排序
grouped_sorted = df.groupby('Department').apply(lambda x: x.sort_values(by='Salary', ascending=False))
print(grouped_sorted)

# 使用 pivot_table 计算每个部门的薪资平均值
pivot_table = df.pivot_table(values='Salary', index='Department', aggfunc='mean')
print(pivot_table)