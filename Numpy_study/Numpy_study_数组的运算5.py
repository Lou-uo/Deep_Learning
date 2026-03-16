import numpy as np

arr = np.arange(1,9).reshape(2,4)
# 矩阵中每个元素都会参与运算
print(arr+10)
print(arr-10)
print(arr*10)
print(arr/10)   # 变成浮点型
print(arr**2)
print(arr//2)
print(arr%6, '\n')

# 矩阵元素之间的运算(不是矩阵级的运算)
arr1 = np.arange(-1,-9,-1).reshape(2,4)
arr2 = -arr1;
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)
print(arr1**arr2, '\n')

# 向量被广播！！
arr1 = np.array([-100,0,100])
arr2 = np.random.random((10,3))  # 10行3列(0,1)分布的随机矩阵
print(arr1 * arr2, '\n')      # 向量arr1沿列方向广播10次

# 列矩阵被广播
arr1 = np.arange(3).reshape(3,1)
arr2 = np.ones( (3,5) )
print(arr1 * arr2, '\n')      # 列矩阵arr1沿行方向广播5次

# 行矩阵与列矩阵同时被广播
arr1 = np.arange(3)
arr2 = np.arange(3).reshape(3,1)
print(arr1 * arr2, '\n')      # arr1按列方向，arr2按行方向被广播

# 向量之间的乘积(前一个为行矩阵，后一个列矩阵)
arr1 = np.arange(5)
arr2 = np.arange(5)
print( np.dot(arr1, arr2) , '\n')     # 输出一个标量

# 向量与矩阵乘积(前面的向量为行矩阵)
arr1 = np.arange(5)
arr2 = np.arange(15).reshape(5,3)
print( np.dot(arr1, arr2) , '\n')

# 矩阵与向量乘积(后面的向量为列矩阵)
arr1 = np.arange(15).reshape(3,5)
arr2 = np.arange(5)
print( np.dot(arr1, arr2) , '\n' )

# 矩阵与矩阵的乘积(线性代数)
arr1 = np.arange(10).reshape(5,2)
arr2 = np.arange(16).reshape(2,8)
print( np.dot(arr1, arr2) , '\n')
