import matplotlib.pyplot as plt
# %matplotlib inline
# Jupyter需要加上一句，python不需要

# 展示高清图(svg矢量图)
from matplotlib_inline import backend_inline
backend_inline.set_matplotlib_formats('svg')

# 准备数据
x = [1,2,3,4,5]
y1 = [1,2,3,4,5]
y2 = [0,0,0,0,0]
y3 = [-1,-2,-3,-4,-5]

# Matlab方式
Fig1 = plt.figure()
plt.plot(x,y1,label='y=x')
plt.plot(x,y2,label='y=0')
plt.plot(x,y3,label='y=-x')
plt.legend()
plt.show()

# 面向对象方式
Fig2, ax2 = plt.subplots()
ax2.plot(x,y1,label='y=x')
ax2.plot(x,y2,label='y=0')
ax2.plot(x,y3,label='y=-x')
plt.legend()
plt.show()
# legend还有三个常用的关键字参数：loc、frameon和 ncol
# plt.legend(loc='',frameon='',ncol='')
# >> loc用于表示图例位置，该关键字在 upper、center、lower中选一个，
# 在 left、center、right中选一个，用法如 loc='upper right',也可以 loc='best'。
# >> frameon用于表示图例边框，去边框是 frameon=False。
# >> ncol用于表示图例的列数，默认是1列，也可以通过 ncol=2调为2列。


