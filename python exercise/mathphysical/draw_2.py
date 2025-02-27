import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

# 设置字体，包含中文字符,这些是警告信息，不是错误信息。如果你不想看到这些警告信息，你可以在代码中添加一行来设置字体，使其包含需要的字符。
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 读取Excel文件
data = pd.read_excel('hhh.xlsx')

# 提取数据列
# 提取数据列
data1 = data.iloc[1:402, 1].values.flatten()  # 提取B列的数据，从第2行到第402行
data2 = data.iloc[1:402, 2].values.flatten()  # 提取C列的数据，从第2行到第402行

# 定义拟合函数
def nihehans(x, a, b):
    return a * x + b

# 使用最小二乘法拟合曲线
nihecans, _ = curve_fit(nihehans, data1, data2, [1, 1])

a = nihecans[0]
b = nihecans[1]

# 计算拟合质量指标
residuals = data2 - nihehans(data1, *nihecans)
mse = np.mean(residuals**2)
rsquared = 1 - (np.sum(residuals**2) / np.sum((data2 - np.mean(data2))**2))

# 相关性分析
correlation_matrix = np.corrcoef(data1, data2)
correlation_coefficient = correlation_matrix[0, 1]

# 绘制残差图
plt.figure()
plt.plot(data1, residuals, 'o')
plt.xlabel('压力')
plt.ylabel('残差')
plt.title('残差图')

# 绘制原始数据和拟合结果
plt.figure()
plt.plot(data1, data2, '.', label='原始数据')
plt.plot(data1, nihehans(data1, *nihecans), 'r', label='拟合结果')
plt.xlabel('压力')
plt.ylabel('弹性模量')
plt.legend()
plt.title('弹性模量与压力关系拟合')

plt.show()

print('拟合结果：弹性模量 = {} * 压力 + {}'.format(a, b))
print('均方误差 (MSE):', mse)
print('确定系数 (R-squared):', rsquared)
print('相关系数:', correlation_coefficient)
