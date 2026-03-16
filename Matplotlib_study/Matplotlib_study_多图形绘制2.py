# 画一幅图，请在一个代码块内完成，不得分块!!!

import matplotlib.pyplot as plt
# %matplotlib inline
# Jupyter需要加上一句，python不需要

# 展示高清图(svg矢量图)
from matplotlib_inline import backend_inline
backend_inline.set_matplotlib_formats('svg')


## 2.1 绘制多个线条
# 准备数据
x = [1,2,3,4,5]
y1 = [1,2,3,4,5]
y2 = [0,0,0,0,0]
y3 = [-1,-2,-3,-4,-5]

# # Matlab方式
# Fig = plt.figure(1)
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.plot(x,y3)
# plt.show()
#
# # 面向对象方式
# Fig2, ax2 = plt.subplots(1)
# ax2.plot(x,y1)
# ax2.plot(x,y2)
# ax2.plot(x,y3)
# plt.show()


## 2.2 绘制多个子图
# Matlab方式
Fig1 = plt.figure(1)
plt.subplot(3,1,1),plt.plot(x,y1)   # 3行1列第1个
plt.subplot(3,1,2),plt.plot(x,y2)   # 3行1列第2个
plt.subplot(3,1,3),plt.plot(x,y3)   # 3行1列第3个
plt.show()

# 面向对象方式
Fig2, ax2 = plt.subplots(3)
ax2[0].plot(x,y1)
ax2[1].plot(x,y2)
ax2[2].plot(x,y3)
plt.show()
