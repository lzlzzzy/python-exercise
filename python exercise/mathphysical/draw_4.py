import numpy as np
from scipy.integrate import quad

# 定义被积函数
def integrand(x):
    return np.cos(np.pi * x) * np.cos(2 * np.pi * x)

# 计算积分
result, error = quad(integrand, 0, 1)

print("积分结果:", result)
print("误差估计:", error)
