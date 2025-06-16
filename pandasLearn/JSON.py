import os

current_dir = os.path.dirname(os.path.abspath(__file__))
print("Current directory:", current_dir)

file_path = os.path.join(current_dir, 'site.json')
print("File path:", file_path)

import pandas as pd

df = pd.read_json(file_path)
   
print(df.to_string())


import pandas as pd


# 字典格式的 JSON                                                                                              
s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}

# 读取 JSON 转为 DataFrame                                                                                           
df = pd.DataFrame(s)
print(df)



import pandas as pd

URL = 'https://static.jyshare.com/download/sites.json'
df = pd.read_json(URL)
print(df)


import pandas as pd

# JSON 数据
json_data = '''
[
  {"Name": "Alice", "Age": 25, "City": "New York"},
  {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
  {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]
'''

# 从 JSON 字符串读取数据，指定 orient='records'
df = pd.read_json(json_data, orient='records')

print(df)




import pandas as pd

df = pd.read_json(os.path.join(current_dir, 'nested_list.json'))

print(df)

import pandas as pd
import json

# 使用 Python JSON 模块载入数据
with open(os.path.join(current_dir, 'nested_list.json'),'r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(data, record_path =['students'])
print(df_nested_list)


# 显示结果还没有包含 school_name 和 class 元素，如果需要展示出来可以使用 meta 参数来显示这些元数据：
import pandas as pd
import json

# 使用 Python JSON 模块载入数据
with open(os.path.join(current_dir, 'nested_list.json'),'r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(
    data, 
    record_path =['students'], 
    meta=['school_name', 'class']
)
print(df_nested_list)



import pandas as pd
import json

# 使用 Python JSON 模块载入数据
with open(os.path.join(current_dir, 'nested_mix.json'),'r') as f:
    data = json.loads(f.read())
    
df = pd.json_normalize(
    data, 
    record_path =['students'], 
    meta=[
        'class',
        ['info', 'president'], 
        ['info', 'contacts', 'tel']
    ]
)

print(df)



import pandas as pd
from glom import glom

df = pd.read_json(os.path.join(current_dir, 'nested_deep.json'))

data = df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)


# 将 DataFrame 转换为 JSON
import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# 将 DataFrame 转换为 JSON 字符串
json_str = df.to_json()

print(json_str)


# 将 DataFrame 转换为 JSON 文件（指定 orient='records'）：
import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# 将 DataFrame 转换为 JSON 文件，指定 orient='records'
df.to_json('data.json', orient='records', lines=True)

# 输出生成的文件内容：
# [
#   {"Name":"Alice","Age":25,"City":"New York"},
#   {"Name":"Bob","Age":30,"City":"Los Angeles"},
#   {"Name":"Charlie","Age":35,"City":"Chicago"}
# ]


# 将 DataFrame 转换为 JSON 并指定日期格式：
import pandas as pd

# 创建 DataFrame，包含日期数据
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Date': pd.to_datetime(['2021-01-01', '2022-02-01', '2023-03-01']),
    'Age': [25, 30, 35]
})

# 将 DataFrame 转换为 JSON，并指定日期格式为 'iso'
json_str = df.to_json(date_format='iso')

print(json_str)