import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision import datasets
import matplotlib.pyplot as plt

# 展示高清图
from matplotlib_inline import backend_inline
backend_inline.set_matplotlib_formats('svg')

#   制作数据集

# 设定下载参数
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(0.1307, 0.3081)
])

# 下载训练集与测试集
train_Data = datasets.MNIST(
    root = 'E:/Deep_Learning/DL/CNN_study',
    train = True,       # 表示下载的是训练集
    download = True,    # 如果在文件夹中没有检索到，则进行下载
    transform = transform
)

test_Data = datasets.MNIST(
    root = 'E:/Deep_Learning/DL/CNN_study',
    train = False,       # 表示下载的是测试集
    download = True,     # 如果在文件夹中没有检索到，则进行下载
    transform = transform
)

# 批次加载器
train_loader = DataLoader(dataset=train_Data, batch_size=256, shuffle=True)     # shuffle用于在每个epoch内先洗牌再分批
test_loader = DataLoader(dataset=test_Data, batch_size=256, shuffle=False)

# 搭建神经网络
class CNN(nn.Module):
    def __init__(self):
        super(CNN,self).__init__()
        self.net = nn.Sequential(
            # C1:卷积层
            nn.Conv2d(1,6,kernel_size=5,padding=2),nn.Tanh(),
            nn.AvgPool2d(kernel_size=2,stride=2),		# S2:平均汇聚
            nn.Conv2d(6,16,kernel_size=5),nn.Tanh(),	# C3:卷积层
            nn.AvgPool2d(kernel_size=2,stride=2),		# S4:平均汇聚
            nn.Conv2d(16,120,kernel_size=5),nn.Tanh(),	# C5:卷积层
            nn.Flatten(),								# 图像铺平成一维
            nn.Linear(120,84),nn.Tanh(),				# F5:全连接层
            nn.Linear(84,10)							# F6:全连接层
        )

    def forward(self, x):
        '''前向传播'''
        y = self.net(x)     # x即输入数据
        return y            # y即输出数据

# 查看网络结构
X = torch.rand(size = (1, 1, 28, 28))
for layer in CNN().net:
    X = layer(X)
    # print( layer.__class__.__name__, 'output shape: \t', X.shape ) # 查看每一层的情况

# 创建子类的实例
model = CNN()
# model = CNN().to('cuda:0')

# 损失函数的选择（交叉熵损失）
loss_fn = nn.CrossEntropyLoss() # 自带softmax激活函数

# 优化算法的选择
learning_rate = 0.01   # 设置学习率
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=learning_rate
)

# 训练模型
epochs = 5
losses = []     # 记录损失函数变化的列表

for epoch in range(epochs):
    for (x, y) in train_loader: # 获取小批次的x与y
#        x, y = x.to('cuda:0'), y.to('cuda:0')  #  把小批次搬到GPU上
        Pred = model(x)             # 一次前向传播（BGD）
        loss = loss_fn(Pred, y)     # 计算损失函数
        losses.append(loss.item())  # 记录损失函数的变化
        optimizer.zero_grad()       # 清理上一轮滞留的梯度
        loss.backward()             # 一次反向传播
        optimizer.step()            # 优化内部参数

Fig = plt.figure()
plt.plot(range(len(losses)), losses)
# plt.show()

# 测试网络
correct = 0
total = 0

with torch.no_grad():       # 关闭梯度计算功能
    for x, y in test_loader:    # 获取小批次的x与y
#        x, y = x.to('cuda:0'), y.to('cuda:0')  #  把小批次搬到GPU上
        Pred = model(x)          # 一次前向传播(小批量)
#   a,b=torch.max(Pred.data,dim=1)的意思是，找出Pred每一行里的最大值，
# 数值赋给a,所处位置赋给b。因此上述代码里的pred就相当于把独热编码
# 转换回了普通的阿拉伯数字，这样一来可以直接与y进行比较。
#   由于此处pred与y是一阶张量，因此correct行的结尾不能加.all(1)e]
        _, pred = torch.max(Pred.data, dim=1)
        correct += torch.sum( (pred == y) )   # 预测正确的样本
        total += y.size(0)                       # 全部的样本数量

print(f'测试集精准度:{100*correct/total} % ')
