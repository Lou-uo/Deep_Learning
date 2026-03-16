from cgi import print_form

import numpy as np

# 创建整数型数组
arr1 = np.array( [1, 2, 3] )    # 元素若都为整数，则为整数数组

# 创建浮点型数组
arr2 = np.array( [ 1.0, 2, 3] ) # 内含浮点数，则为浮点数数组

# 使用print输出Numpy数组后，元素之间没逗号
# 1、与python列表区分；2、避免逗号与小数点之间的混淆

### 同化定理

# 整数型数组
arr3 = np.array( [ 1, 2, 3] )
arr3[0] = 100.9         # 插入浮点数，被截断，数组仍为整数型

# 浮点型数组
arr4 = np.array( [ 1.0, 2, 3] )
arr4[0] = 10            # 插入整数型，被升级，数组仍为浮点型

### 共同改变定理

# 整数型数组 --> 浮点型数组
arr5 = np.array( [ 1, 2, 3] )
arr6 = arr5.astype(float)

# 浮点型数组 --> 整数型数组
arr7 = np.array( [ 1.0, 2, 3] )
arr8 = arr7.astype(int)
