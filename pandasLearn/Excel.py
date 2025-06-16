import pandas as pd

# 读取 data.xlsx 文件
# df = pd.read_excel('runoob_pandas_data.xlsx')
df = pd.read_excel(r'F:\wdj\vscode\workspace\pyhonLearn\pandasLearn\runoob_pandas_data.xlsx')

# 打印读取的 DataFrame
print(df)


import pandas as pd

# 读取默认的第一个表单
df = pd.read_excel(r'F:\wdj\vscode\workspace\pyhonLearn\pandasLearn\runoob_pandas_data.xlsx')
print(df)

# 读取指定表单的内容（表单名称）
df = pd.read_excel(r'F:\wdj\vscode\workspace\pyhonLearn\pandasLearn\runoob_pandas_data.xlsx', sheet_name='工作表 1')
print(df)

# 读取多个表单，返回一个字典
dfs = pd.read_excel(r'F:\wdj\vscode\workspace\pyhonLearn\pandasLearn\runoob_pandas_data.xlsx', sheet_name=['Sheet1', '工作表 1'])
print(dfs)

# 自定义列名并跳过前两行
df = pd.read_excel(r'F:\wdj\vscode\workspace\pyhonLearn\pandasLearn\runoob_pandas_data.xlsx', header=None, names=['A', 'B', 'C'], skiprows=2)
print(df)


import pandas as pd

# 创建一个简单的 DataFrame
df = pd.DataFrame({
'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, 30, 35],
'City': ['New York', 'Los Angeles', 'Chicago']
})

# 将 DataFrame 写入 Excel 文件，写入 'Sheet1' 表单
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)

# 写入多个表单，使用 ExcelWriter
with pd.ExcelWriter('output.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    df.to_excel(writer, sheet_name='Sheet2', index=False)



import pandas as pd

# 使用 ExcelFile 加载 Excel 文件
excel_file = pd.ExcelFile(r'F:\wdj\vscode\workspace\pyhonLearn\pandasLearn\runoob_pandas_data.xlsx')

# 查看所有表单的名称
print(excel_file.sheet_names)

# 读取指定的表单
df = excel_file.parse('Sheet1')
print(df)

# 关闭文件
excel_file.close()



with pd.ExcelWriter('output.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1')
    
df1 = pd.DataFrame([["AAA", "BBB"]], columns=["Spam", "Egg"])  
df2 = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  
with pd.ExcelWriter("path_to_file.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Sheet1")  
    df2.to_excel(writer, sheet_name="Sheet2")
    
from datetime import date, datetime  
df = pd.DataFrame(
    [
        [date(2014, 1, 31), date(1999, 9, 24)],
        [datetime(1998, 5, 26, 23, 33, 4), datetime(2014, 2, 28, 13, 5, 13)],
    ],
    index=["Date", "Datetime"],
    columns=["X", "Y"],
)  
with pd.ExcelWriter(
    "path_to_file.xlsx",
    date_format="YYYY-MM-DD",
    datetime_format="YYYY-MM-DD HH:MM:SS"
) as writer:
    df.to_excel(writer)
    
    
# 向现有 Excel 文件追加内容：
with pd.ExcelWriter("path_to_file.xlsx", mode="a", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Sheet3")


# 使用 if_sheet_exists 参数替换已存在的工作表：
with pd.ExcelWriter(
    "path_to_file.xlsx",
    mode="a",
    engine="openpyxl",
    if_sheet_exists="replace",
) as writer:
    df.to_excel(writer, sheet_name="Sheet1")


# 向同一个工作表写入多个 DataFrame，注意 if_sheet_exists 参数需要设置为 overlay：
with pd.ExcelWriter("path_to_file.xlsx",
    mode="a",
    engine="openpyxl",
    if_sheet_exists="overlay",
) as writer:
    df1.to_excel(writer, sheet_name="Sheet1")
    df2.to_excel(writer, sheet_name="Sheet1", startcol=3)


# 将 Excel 文件存储在内存中：
import io
df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])
buffer = io.BytesIO()
with pd.ExcelWriter(buffer) as writer:
    df.to_excel(writer)


# 将 Excel 文件打包到 zip 压缩文件中：
import zipfile  
df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  
with zipfile.ZipFile("path_to_file.zip", "w") as zf:
    with zf.open("filename.xlsx", "w") as buffer:
        with pd.ExcelWriter(buffer) as writer:
            df.to_excel(writer)

