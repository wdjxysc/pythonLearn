# import pandas as pd

# # 从 CSV 文件中读取数据
# df = pd.read_csv('data.csv')

# # 从 Excel 文件中读取数据
# df = pd.read_excel('data.xlsx')

# # 从 SQL 数据库中读取数据
# import sqlite3
# conn = sqlite3.connect('database.db')
# df = pd.read_sql('SELECT * FROM table_name', conn)

# # 从 JSON 字符串中读取数据
# json_string = '{"name": "John", "age": 30, "city": "New York"}'
# df = pd.read_json(json_string)

# # 从 HTML 页面中读取数据
# url = 'https://www.runoob.com'
# dfs = pd.read_html(url)
# df = dfs[0] # 选择第一个数据框



# # 显示前五行数据
# df.head()

# # 显示后五行数据
# df.tail()

# # 显示数据信息
# df.info()

# # 显示基本统计信息
# df.describe()

# # 显示数据的行数和列数
# df.shape


# import pandas as pd

# data = [
#     {"name": "Google", "likes": 25, "url": "https://www.google.com"},
#     {"name": "Runoob", "likes": 30, "url": "https://www.runoob.com"},
#     {"name": "Taobao", "likes": 35, "url": "https://www.taobao.com"}
# ]

# df = pd.DataFrame(data)
# # 显示前两行数据
# print(df.head(2))
# # 显示前最后一行数据
# print(df.tail(1))


# # 删除包含缺失值的行或列
# df.dropna()

# # 将缺失值替换为指定的值
# df.fillna(0)

# # 将指定值替换为新值
# df.replace('old_value', 'new_value')

# # 检查是否有重复的数据
# df.duplicated()

# # 删除重复的数据
# df.drop_duplicates()


# # 选择指定的列
# df['column_name']

# # 通过标签选择数据
# df.loc[row_index, column_name]

# # 通过位置选择数据
# df.iloc[row_index, column_index]

# # 通过标签或位置选择数据
# df.ix[row_index, column_name]

# # 选择指定的列
# df.filter(items=['column_name1', 'column_name2'])

# # 选择列名匹配正则表达式的列
# df.filter(regex='regex')

# # 随机选择 n 行数据
# df.sample(n=5)


# # 按照指定列的值排序
# df.sort_values('column_name')

# # 按照多个列的值排序
# df.sort_values(['column_name1', 'column_name2'], ascending=[True, False])

# # 按照索引排序
# df.sort_index()

# # 按照指定列进行分组
# df.groupby('column_name')

# # 对分组后的数据进行聚合操作
# df.aggregate('function_name')

# # 生成透视表
# df.pivot_table(values='value', index='index_column', columns='column_name', aggfunc='function_name')


# # 将多个数据框按照行或列进行合并
# df = pd.concat([df1, df2])

# # 按照指定列将两个数据框进行合并
# df = pd.merge(df1, df2, on='column_name')


# import pandas as pd

# # 读取 JSON 数据
# df = pd.read_json('data.json')

# # 删除缺失值
# df = df.dropna()

# # 用指定的值填充缺失值
# df = df.fillna({'age': 0, 'score': 0})

# # 重命名列名
# df = df.rename(columns={'name': '姓名', 'age': '年龄', 'gender': '性别', 'score': '成绩'})

# # 按成绩排序
# df = df.sort_values(by='成绩', ascending=False)

# # 按性别分组并计算平均年龄和成绩
# grouped = df.groupby('性别').agg({'年龄': 'mean', '成绩': 'mean'})

# # 选择成绩大于等于90的行，并只保留姓名和成绩两列
# df = df.loc[df['成绩'] >= 90, ['姓名', '成绩']]

# # 计算每列的基本统计信息
# stats = df.describe()

# # 计算每列的平均值
# mean = df.mean()

# # 计算每列的中位数
# median = df.median()

# # 计算每列的众数
# mode = df.mode()

# # 计算每列非缺失值的数量
# count = df.count()