import numpy as np

# 绝对值
arr_v = np.array([0,1,-2,3,-4,5])
abs_v = np.abs(arr_v)
print(abs_v, '\n')

# 三角函数
theta = np.arange(3) * np.pi / 2
sin_v = np.sin(theta)
cos_v = np.cos(theta)
tan_v = np.tan(theta)
print(sin_v, '\n' , cos_v, '\n' , tan_v, '\n')

# 指数函数
x = np.arange(1,4)
print(x, '\n', np.exp(x), '\n', 2**x, '\n', 10**x)

# 对数函数
x = np.array([1,10,100,1000])
print(x, '\n', np.log(x), '\n', np.log(x)/np.log(7), '\n', np.log10(x))

### ！！！聚合函数！！！
# 求最值
arr = np.random.random((2,3))
print(arr)
print('按维度一求最大值：', np.max(arr, axis=0))  # 输出每列中的最大值
print('按维度二求最小值：', np.min(arr, axis=1))  # 输出每行中的最大值
print('整体求最大值：', np.max(arr), '\n')

# 求和、求积(仅演示sum):np.sum(),np.prod()
arr = np.arange(10).reshape(2,5)
print(arr)
print('按维度一求和', np.sum(arr,axis=0))
print('按维度二求和', np.sum(arr,axis=1))
print('整体求和', np.sum(arr), '\n')

# 均值函数 np.mean() 与 标准差函数 np.std()
arr = np.arange(10).reshape(2,5)
print(arr)
print('按维度一求平均', np.mean(arr,axis=0))
print('按维度二求平均', np.mean(arr,axis=1))
print('整体求平均', np.mean(arr))

# 聚合函数的安全版本(忽略数组中的缺失值，避免报错)
# np.nansum(),np.nanprud()……加上nan即可。
