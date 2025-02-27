import matplotlib.pyplot as plt
import numpy as np

# 定义 x 变量的范围 (-3，3) 数量 50
x=np.linspace(-3,3,50)
y=x**2

# Figure 并指定大小
plt.figure(num=3,figsize=(6,6))
# 绘制 y=x^2 的图像，设置 color 为 red，线宽度是 1，线的样式是 --
plt.plot(x,y,color='red',linewidth=1.0,linestyle='--')

ax=plt.gca()
# 使用.spines设置边框：x轴；将右边颜色设置为 none。
# 使用.set_position设置边框位置：y=0的位置；（位置所有属性：outward，axes，data）
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 移动坐标轴
# 将 bottom 即是 x 坐标轴设置到 y=0 的位置。
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


plt.show()