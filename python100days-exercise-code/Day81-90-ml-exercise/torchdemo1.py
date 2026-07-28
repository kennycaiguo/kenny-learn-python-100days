from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import torch
import torch.nn as nn
import torch.optim as optim

# 加载鸢尾花数据集
iris = datasets.load_iris()
X, y = iris.data, iris.target

# 数据预处理（标准化）
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分训练集和测试集
xtrain, xtest, ytrain, ytest = train_test_split(X_scaled, y, train_size=0.8, random_state=3)

xtrain_tensor, xtest_tensor, ytrain_tensor, ytest_tensor = (
    torch.tensor(xtrain,dtype=torch.float32),
    torch.tensor(xtest,dtype=torch.float32),
    torch.tensor(ytrain,dtype=torch.long),
    torch.tensor(ytest,dtype=torch.long),
)

class IrisNN(nn.Module):
    """鸢尾花神经网络模型"""

    def __init__(self):
        """初始化方法"""
        # 调用父类构造器
        super(IrisNN, self).__init__()
        # 输入层到隐藏层（4个特征到32个神经元全连接）
        self.fc1 = nn.Linear(4, 32)
        # 隐藏层到输出层（32个神经元到3个输出全连接）
        self.fc2 = nn.Linear(32, 3)

    def forward(self, x):
        """前向传播"""
        # 隐藏层使用ReLU激活函数
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = IrisNN()
# 定义损失函数（交叉熵损失函数）
loss_fun = nn.CrossEntropyLoss()
# 使用Adam优化器（大多数任务表现较好）
optimizer = optim.Adam(model.parameters(),lr=0.001)    

# 训练模型（迭代256个轮次）
for _ in range(256):
    model.train()
    # 清除上一次的梯度
    optimizer.zero_grad()
    # 计算输出
    output = model(xtrain_tensor)
    # 计算损失
    loss = loss_fun(output, ytrain_tensor)
    # 反向传播
    loss.backward()
    # 更新权重
    optimizer.step()

# 评估模型
model.eval()
with torch.no_grad():
    output = model(xtest_tensor)
    # 获取预测得分最大值的索引（预测标签）
    _, y_pred_tensor = torch.max(output, 1)
    # 计算并输出预测准确率
    print(f'Accuracy: {accuracy_score(ytest_tensor, y_pred_tensor):.2%}')
    # 输出分类模型评估报告
    print(classification_report(ytest_tensor, y_pred_tensor))    