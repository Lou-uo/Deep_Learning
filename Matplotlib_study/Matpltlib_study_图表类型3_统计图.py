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

# 创建10000个标准正态分布的样本
import numpy as np
data = np.random.randn(10000)

# # Matlab方式
# Fig1 = plt.figure()
# plt.hist(data)
# plt.show()

# # 面向对象方式
# Fig2, ax2 = plt.subplots()
# ax2.hist(data)
# plt.show()


# ## 1、区间个数
# ## bins关键字参数即区间划分的数量，默认为10，现将其改为30
# # Matlab方式
# Fig1 = plt.figure()
# plt.hist(data,bins=30)
# plt.show()

# ## 2、透明度
# ## Alpha关键字表示透明度，默认为1，现将其改为0.5
# # Matlab方式
# Fig1 = plt.figure()
# plt.hist(data,alpha=0.5)
# plt.show()

# ## 3、图表类型
# ## histtype表示类型，默认是'bar'，现将其改为'stepfilled'，图形浑然一体
# Fig1 = plt.figure()
# plt.hist(data,histtype='stepfilled')
# plt.show()

# ## 4、直方图颜色
# # Matlab方式
# Fig1 = plt.figure()
# plt.hist(data,color='#A2A2D0')
# plt.show()

# ## 5、边缘颜色
# # Matlab方式
# Fig1 = plt.figure()
# plt.hist(data,edgecolor='#FFFFFF')
# plt.show()

## 综合应用
# 创建三个正态分布
x1 = np.random.normal(3,1,1000)
x2 = np.random.normal(6,1,1000)
x3 = np.random.normal(9,1,1000)

# Matlab方式
Fig1 = plt.figure()
plt.hist(x1,bins=30,alpha=0.5,color='#7CB5EC',edgecolor='#FFFFFF')
plt.hist(x2,bins=30,alpha=0.5,color='#A2A2D0',edgecolor='#FFFFFF')
plt.hist(x3,bins=30,alpha=0.5,color='#47ADC7',edgecolor='#FFFFFF')
plt.show()

# 面向对象方式
Fig2, ax2 = plt.subplots()
ax2.hist(x1,bins=30,alpha=0.5,color='#7CB5EC',histtype='stepfilled')
ax2.hist(x2,bins=30,alpha=0.5,color='#A2A2D0',histtype='stepfilled')
ax2.hist(x3,bins=30,alpha=0.5,color='#47ADC7',histtype='stepfilled')
plt.show()
