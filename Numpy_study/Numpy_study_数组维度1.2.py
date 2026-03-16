import numpy as np
from numpy.array_api import reshape

arr1 = np.ones(3)           # 传入形状3
#print(arr1)                 # 造出一维数组
#print(arr1.shape)

arr2 = np.ones((1, 3))      # 传入形状(1,3)
#print(arr2)                 # 造出二维数组
#print(arr2.shape)

arr3 = np.ones((1, 1, 3))   # 传入形状(1,1,3)
#print(arr3)                 # 造出三维数组
#print(arr3.shape)

### 不同维度数组之间的转换

# 创建一维数组
arr4 = np.arange(10)
#print(arr4)

# 升级为二维数组
arr5 = arr4.reshape(2, -1)  # -1是电脑会自己匹配
#print(arr5)

# 创建二维数组
arr6 = np.arange(10).reshape(2,5)
print(arr6)

# 降级为一维数组
arr7 = arr6.reshape(1, -1)
print(arr7)