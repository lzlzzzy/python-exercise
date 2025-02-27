import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件，指定编码格式为GBK
data = pd.read_csv('Sample1-1.csv', encoding='GBK')

# 提取前两列数据
x = data.iloc[:, 0]
y = data.iloc[:, 1]

# 绘制图像
plt.plot(x, y)
plt.xlabel('time')
plt.ylabel('voltage')
plt.title('sample1')
plt.show()
