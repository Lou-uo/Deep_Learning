import numpy as np

# 创建数组
arr = np.arange(1,7).reshape(2,3)
# 数组与数字作比较
print(arr >= 4, '\n')

# 创建同维数组
arr1 = np.arange(1,6)
arr2 = np.flipud(arr1)  # 列矩阵上下翻转
# 同维度数组作比较
print(arr1 > arr2, '\n')

# 多个条件 python(and or not) -- numpy(& | ~) -- 与 或 非

## np.sum():统计布尔型数组里True的个数
# 创建一个形状为10000的标准正态分布数组
arr = np.random.normal(0,1,10000)
# 统计该分布中绝对值小于1的元素个数
num = np.sum(np.abs(arr) < 1)
print(num, '\n')

## np.any():只要布尔型数组含有True，就返回True
# 创建同维数组
arr1 = np.arange(1,10)
arr2 = np.flipud(arr1)
# 统计这两个数组里是否有共同元素
print(np.any(arr1 == arr2), '\n')

## np.all():当布尔型数组里全是True时，才返回True
# 模拟英语六级的成绩，创建100000个样本
arr = np.random.normal(500,70,100000)
# 判断是否所有考试的分数都高于250
print(np.all(arr > 250), '\n')

### 布尔型数组作为掩码！！！
# 创建数组
arr = np.arange(1,13).reshape(3,4)
# 数组与数字作比较
print(arr > 4)
# 筛选出arr > 4的元素
print(arr[arr > 4], '\n')

# 创建同维数组
arr1 = np.arange(1,10)
arr2 = np.flipud(arr1)
# 同维数组作比较
print(arr1 > arr2)
# 筛选出arr1 > arr2位置上的元素
print(arr1[arr1 > arr2])
print(arr2[arr1 > arr2], '\n')

# 模拟英语六级的成绩，创建1000个样本
arr = np.random.normal(500,70,1000)
# 找出六级成绩超过650的元素所在位置
print(np.where(arr > 650)[0])  # 返回元组的第一个元素
# 找出六级成绩最高分的元素所在位置
print(np.where(arr == np.max(arr))[0])
