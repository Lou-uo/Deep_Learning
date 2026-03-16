import matplotlib.pyplot as plt
# %matplotlib inline
# Jupyter需要加上一句，python不需要

# 展示高清图(svg矢量图)
from matplotlib_inline import backend_inline
backend_inline.set_matplotlib_formats('svg')

# 准备数据
x = [ 1, 2, 3, 4, 5 ]       # 数据的x值
y = [ 1, 8, 27, 64, 125 ]   # 数据的y值

# Matlab方式
Fig1 = plt.figure(1)        # 创建新图窗，()中的数字只是图窗的序号
plt.plot(x, y)        # plot函数：先描点，再连线
plt.show()

# 面向对象方式
Fig2 = plt.figure(2)
ax2 = plt.axes()    # 坐标轴
ax2.plot(x, y)
plt.show()

# 保存图像
# Fig1 = plt.savefig(r'E:\123123\我的图.svg')