import matplotlib.pyplot as plt
# %matplotlib inline
# Jupyter需要加上一句，python不需要

# 展示高清图(svg矢量图)
from matplotlib_inline import backend_inline
backend_inline.set_matplotlib_formats('svg')

# 准备数据
x = [1,2,3,4,5]
y = [1,8,27,64,125]

# Matlab方式
Fig1 = plt.figure()
plt.plot(x,y)
plt.title('This is the title')
plt.xlabel('This is the xlabel')
plt.ylabel('This is the ylabel')
plt.show()

# 面向对象方式
Fig2, ax2 = plt.subplots()
ax2.plot(x,y)
ax2.set_title('This is the title')
ax2.set_xlabel('This is the xlabel')
ax2.set_ylabel('This is the ylabel')
plt.show()



