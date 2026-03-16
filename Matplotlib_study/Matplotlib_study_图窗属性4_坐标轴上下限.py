import matplotlib.pyplot as plt
# %matplotlib inline
# Jupyter需要加上一句，python不需要

# 展示高清图(svg矢量图)
from matplotlib_inline import backend_inline
backend_inline.set_matplotlib_formats('svg')

# 准备数据
x = [1,2,3,4,5]
y = [1,8,27,64,125]

# ## 1、lim法
# # Matlab方法
# Fig1 = plt.figure()
# plt.plot(x,y)
# plt.xlim(1,5)
# plt.ylim(1,125)
# plt.show()
#
# # 面向对象方法
# Fig2, ax2 = plt.subplots()
# ax2.plot(x,y)
# ax2.set_xlim(1,5)
# ax2.set_ylim(1,125)
# plt.show()

## 2、axis法
## plt.axis('equql')使x、y轴等长
# Matlab方式
Fig3 = plt.figure()
plt.plot(x,y)
plt.axis([1,5,1,125])
plt.show()

# 面向对象方式
Fig4, ax4 = plt.subplots()
ax4.plot(x,y)
ax4.axis([1,5,1,125])
plt.show()
