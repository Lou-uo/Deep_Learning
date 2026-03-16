import pandas as pd
import numpy as np

### 一维对象的创建

## 1、字典创建法（不推荐
# 创建字典
dict_v = { 'a':0, 'b':0.25, 'c':0.5, 'd':0.75, 'e':1 }
print(dict_v)
# 用字典创建对象
sr = pd.Series( dict_v )
print(sr, '\n')

## 2、数组创建法
# 先定义键与值
v = [0, 0.25, 0.5, 0.75, 1]
k = ['a', 'b', 'c', 'd', 'e']

# 用列表创建对象(第一个参数：列表、数组、张量均可)
sr = pd.Series(v, index=k)  # index可以省略，索引从0开始
print(sr, '\n')

### 一维对象的属性

# 查看values的属性(Numpy数组)
print(sr.values)
# 查看index属性
print(sr.index, '\n')

### 二维对象的创建

# 1、字典创建法
# 创建sr1：各个病人的年龄
v1 = [ 53, 64, 72, 82 ]
k = [ '1号', '2号', '3号', '4号' ]
sr1 = pd.Series(v1, index=k)
# 创建sr2：各个病人的性别
v2 = [ '女', '男', '男', '女']
k = [ '1号', '2号', '3号', '4号' ]
sr2 = pd.Series(v2, index=k)
# 创建df二维对象
df = pd.DataFrame({'年龄':v1, '性别':v2})
print(df, '\n')

# 2、数组创建法
# 设定键值
v = np.array([ [53, '女'], [64, '男'], [72, '男'], [82, '女'] ])  # 字符串型数组
i = [ '1号', '2号', '3号', '4号' ]
c = [ '年龄', '性别' ]
df = pd.DataFrame(v, index=i, columns=c)
print(df)
print(df.values)
print(df.index)
print(df.columns, '\n')

# 提取完整的数组
arr = df.values
# 提取第[0]列，并转化为一个整数型数组(从object到整数型)
arr = arr[:,0].astype(int)  # 数组只能容纳一种变量类型
print(arr)
