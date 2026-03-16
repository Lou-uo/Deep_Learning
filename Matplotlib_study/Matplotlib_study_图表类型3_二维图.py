# https://matplotlib.org/stable/plot_types/index.html
# (1) 二维图：（两个向量）
# plot()线型图  scatter()散点图  bar()条形图
# stem()杆图  step()阶梯图  fill_between()误差图  stackplot()堆叠图
# (2) 网格图：（一个矩阵）
# imshow()图像展示  contour()等高线  contourf()填充等高线
# (3) 统计图：（数据分析）
# hist()直方图

# 3.2 二维图
import matplotlib.pyplot as plt
# %matplotlib inline
# Jupyter需要加上一句，python不需要

# 展示高清图(svg矢量图)
from matplotlib_inline import backend_inline
backend_inline.set_matplotlib_formats('svg')

# 准备数据
x = [1,2,3,4,5]
y1 = [0,1,2,3,4]
y2 = [1,2,3,4,5]
y3 = [2,3,4,5,6]
y4 = [3,4,5,6,7]
y5 = [4,5,6,7,8]

# ## 1、设置颜色
# # Matlab方式
# Fig1 = plt.figure()
# plt.plot(x,y1,color='#7CB5EC')
# plt.plot(x,y2,color='#F7A35C')
# plt.plot(x,y3,color='#A2A2D0')
# plt.plot(x,y4,color='#F6675D')
# plt.plot(x,y5,color='#47ADC7')
# plt.show()

# # 面向对象方式
# Fig2, ax2 = plt.subplots()
# ax2.plot(x,y1,color='#7CB5EC')
# ax2.plot(x,y2,color='#F7A35C')
# ax2.plot(x,y3,color='#A2A2D0')
# ax2.plot(x,y4,color='#F6675D')
# ax2.plot(x,y5,color='#47ADC7')
# plt.show()


# ## 2、设置风格
# # Matlab方式
# Fig1 = plt.figure()
# plt.plot(x,y1,color='#7CB5EC',linestyle='-')    # 默认
# plt.plot(x,y2,color='#F7A35C',linestyle='--')   # -----
# plt.plot(x,y3,color='#A2A2D0',linestyle='-.')   # -.-.-.
# plt.plot(x,y4,color='#F6675D',linestyle=':')    # .....
# plt.plot(x,y5,color='#47ADC7',linestyle=' ')    # 隐藏线（可以做出散点图）
# plt.show()

# # 面向对象方式
# Fig2, ax2 = plt.subplots()
# ax2.plot(x,y1,linestyle='-')
# ax2.plot(x,y2,linestyle='--')
# ax2.plot(x,y3,linestyle='-.')
# ax2.plot(x,y4,linestyle=':')
# ax2.plot(x,y5,linestyle=' ')
# plt.show()

# ## 3、设置粗细(0.5~3为宜)
# # Matlab方式
# Fig1 = plt.figure()
# plt.plot(x,y1,linewidth=0.5)
# plt.plot(x,y2,linewidth=1)
# plt.plot(x,y3,linewidth=1.5)
# plt.plot(x,y4,linewidth=2)
# plt.plot(x,y5,linewidth=2.5)
# plt.show()

## 4、设置标记
# Matlab方式
Fig1 = plt.figure()
# 点（可以做成散点图，且效率比plt.scatter()高）
plt.plot(x,y1,marker='.',markersize=6,linestyle='')
plt.plot(x,y2,marker='o',markersize=7)   # 圆
plt.plot(x,y3,marker='^',markersize=8)   # 上三角
plt.plot(x,y4,marker='s',markersize=9)   # square
plt.plot(x,y5,marker='D',markersize=10)   # diamond
plt.show()

