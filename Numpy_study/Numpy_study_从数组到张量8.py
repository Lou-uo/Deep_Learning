# 本次课属于《Python深度学习》系列视频，PyTorch作为当前首屈一指的深度学习库，
# 其将NumPy的语法尽数吸收，作为自己处理数组的基本语法，
# 且运算速度从使用CPU的数组进步到使用GPU的张量。

# NumPy和PyTorch的基础语法几乎一致，具体表现为：
# ① np对应torch;
# ② 数组array对应张量tensor;
# ③ NumPy的n维数组对应着PyTorch的n阶张量。

# 数组与张量之间可以相互转换：
# 数组arr转为张量ts: ts=torch.tensor(arr)；
# 张量ts转为数组arr: arr=np.array(ts)。

# PyTorch的语法修正补充，
# 在该文件夹的《Numpy_study_从数组到张量8的PyTorch语法修正补充.png》