import numpy as np

# 数组的转置
arr1 = np.arange(1, 4)
arr2 = arr1.reshape( (1, -1) )  # 升级为矩阵
arr3 = arr2.T                   # 转置为列矩阵
arr4 = arr1.reshape( (-1, 1) )  # 直接升级为列矩阵

# 向量的翻转(默认为列向量)
arr5 = np.arange(10)
arr5_ud = np.flipud(arr5)       # 向量只能上下翻转

# 矩阵的翻转
arr6 = np.arange(1,21).reshape(4,5)
#print( arr6 )

# 左右翻转
arr_lr = np.fliplr(arr6)
#print( arr_lr )

# 上下翻转
arr_ud = np.flipud(arr6)
#print( arr_ud )

# 矩阵的变形
arr7 = np.array([[1,2,3],[4,5,6]])
arr7_1 = arr7.reshape(6)    # 变形为向量
arr7_2 = arr7.reshape(1,-1) # 变形为矩阵

# 向量的拼接
arr8 = np.array([1,2,3])
arr9 = np.array([4,5,6])
arr_89 = np.concatenate([arr8,arr9])
#print( arr_89 )

# 矩阵的拼接
arr10 = np.array([[1,2,3],[4,5,6]])
arr11 = np.array([[7,8,9],[10,11,12]])
# 按行拼接(上下相接)
arr_1011_1 = np.concatenate([arr10,arr11])  # 默认参数axis=0
#print( arr_1011_1 )
# 按列拼接(左右拼接)
arr_1011_2 = np.concatenate([arr10,arr11],axis=1)
#print( arr_1011_2 )

# 向量的分裂
arr = np.arange(10,100,10)      # 起始,终止,步长
arr_1,arr_2,arr_3 = np.split(arr, [2,8]) # 在索引[2]和索引[8]的位置截断

# 矩阵的分裂
ar = np.arange(1,9).reshape(2,4)
ar_1,ar_2 = np.split(ar, [1]) # 按行分裂,默认参数axis=0
print(ar_1,'\n\n',ar_2,'\n')
ar_1,ar_2,ar_3 = np.split(ar, [1,3],axis=1) # 按列分裂
print(ar_1,'\n\n',ar_2,'\n\n',ar_3)
