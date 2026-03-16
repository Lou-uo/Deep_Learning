import pandas as pd

### 一维对象索引

## 访问元素
# 创建sr
v = [ 53, 64, 72, 82 ]
k = ['1号', '2号', '3号', '4号']
sr = pd.Series(v, index=k)
print(sr.loc['3号'])     # sr.loc为显式索引，但是这里显式索引与隐式索引完全不同不会混淆，可以省略
print(sr.loc[['1号','3号']])
print(sr.iloc[2])            # sr.iloc为隐式索引，其余同上
print(sr.iloc[[0, 2]], '\n')

## 访问切片
# 显式索引
print(sr.loc['1号':'3号'])
# 切片仅是视图(cut不是新建对象，只是一个引用)
cut = sr.loc['1号':'3号']
cut.loc['1号'] = 100
print(sr)
# 对象赋值仅是绑定(cut不是新建对象，只是一个引用)
cut = sr
cut.loc['3号'] = 200
print(sr)

# 隐式索引
print(sr.iloc[0:3])
cut = sr.iloc[0:3]
cut.iloc[0] = 100
print(sr)
cut = sr
cut.iloc[2] = 200
print(sr, '\n')
# n若想创建新变量，与NumPy一样，使用.copy()方法即可。
# 如果去掉.loc和.iloc,此时与NumPy中的索引语法完全一致。

### 二维对象的索引

# 字典创建法
i = [ '1号', '2号', '3号', '4号' ]
v1 = [53, 64, 72, 82]
v2 = [ '女', '男', '男', '女' ]
sr1 = pd.Series(v1, index=i)
sr2 = pd.Series(v2, index=i)
df = pd.DataFrame({ '年龄':sr1, '性别':sr2 })
print(df)
# 访问元素
print('显式索引：\n', df.loc['1号', '年龄'])
# 花式索引
print(df.loc[['1号', '3号'], ['性别', '年龄']])
# 修改元素
df.loc['3号', '年龄'] = 100
print(df, '\n')
# 访问元素
print('隐式索引：\n', df.iloc[0, 0])
# 花式索引
print(df.iloc[[0,2], [1,0]])
# 修改元素
df.iloc[2, 0] = 100
print(df, '\n')

# 数组创建法
v = [ [53, '女'],[64, '男'],[72,'男'],[82,'女']]
i = ['1号', '2号', '3号', '4号']
c = ['年龄', '性别']
df = pd.DataFrame(v, index=i, columns=c)
print(df)
# 切片
print(df.loc['1号':'3号', '年龄'])
# 提取二维对象的行
print(df.loc['3号', :])
# 提取矩阵对象的列
print(df.loc[:, '年龄'])
# 切片
print(df.iloc[0:3, 0])
# 提取二维对象的行
print(df.iloc[2, :])
# 提取二维对象的列
print(df.iloc[:, 0])


