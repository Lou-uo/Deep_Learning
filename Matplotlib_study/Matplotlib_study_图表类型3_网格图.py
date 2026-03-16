# https://matplotlib.org/stable/plot_types/index.html
# (1) 二维图：（两个向量）
# plot()线型图  scatter()散点图  bar()条形图
# stem()杆图  step()阶梯图  fill_between()误差图  stackplot()堆叠图
# (2) 网格图：（一个矩阵）
# imshow()图像展示  contour()等高线  contourf()填充等高线
# (3) 统计图：（数据分析）
# hist()直方图

# 3.3 网格图
import matplotlib.pyplot as plt
# %matplotlib inline
# Jupyter需要加上一句，python不需要

# 展示高清图(svg矢量图)
from matplotlib_inline import backend_inline
backend_inline.set_matplotlib_formats('svg')

# 准备数据
import numpy as np
x = np.linspace(0,10,100)
l = np.sin(x) * np.cos(x).reshape(-1,1)

# Matlab方式
Fig1 = plt.figure()
plt.imshow(l)
plt.colorbar()  # 配置颜色条
plt.show()

# # 面向对象方式
# Fig2, ax2 = plt.subplots()
# ax2.imshow(l)
# plt.show()


