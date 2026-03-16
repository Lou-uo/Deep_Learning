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
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.grid(color='#A2A2D0', linestyle='--', linewidth=0.5)
plt.show()
