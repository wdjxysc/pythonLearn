import pandas as pd

# 示例数据
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [45, 55, 65, 75, 85],
    'Age': [20, 25, 30, 35, 40]
}

df = pd.DataFrame(data)

# 计算皮尔逊相关系数
correlation = df.corr(method='pearson')
print(correlation)

# 计算斯皮尔曼等级相关系数
spearman_correlation = df.corr(method='spearman')
print(spearman_correlation)

# 计算肯德尔秩相关系数
kendall_correlation = df.corr(method='kendall')
print(kendall_correlation)

# 计算相关性矩阵
correlation_matrix = df.corr()
print(correlation_matrix)

# 相关性热图（Correlation Heatmap）
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# 绘制相关性热图
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.show()


# 可视化相关性
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# 计算 Pearson 相关系数
correlation_matrix = df.corr()
# 使用热图可视化 Pearson 相关系数
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()


