from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import numpy as np


iris = load_iris()
x,y = iris.data,iris.target
xtrain,xtest,ytrain,ytest  = train_test_split(x,y,train_size=0.8,random_state=3)

## 手动实现信息熵，信息增益，gini系数，计算信息增益比，计算给定特征后的基尼指数
def entropy(y):
    """
    计算信息熵
    :param y: 数据集的目标值
    :return: 信息熵
    """
    _, counts = np.unique(y, return_counts=True)
    prob = counts / y.size
    return -np.sum(prob * np.log2(prob))


def info_gain(x, y):
    """
    计算信息增益
    :param x: 给定的特征
    :param y: 数据集的目标值
    :return: 信息增益
    """
    values, counts = np.unique(x, return_counts=True)
    new_entropy = 0
    for i, value in enumerate(values):
        prob = counts[i] / x.size
        new_entropy += prob * entropy(y[x == value])
    return entropy(y) - new_entropy




# print(f'H(D)    ={ytrain}')
# print(f'g(D,A0)={info_gain(xtrain[:,0],ytrain)}')
# print(f'g(D,A1)={info_gain(xtrain[:,1],ytrain)}')
# print(f'g(D,A2)={info_gain(xtrain[:,2],ytrain)}')
# print(f'g(D,A3)={info_gain(xtrain[:,3],ytrain)}')

def info_gain_ratio(x, y):
    """
    计算信息增益比
    :param x: 给定的特征
    :param y: 数据集的目标值
    :return: 信息增益比
    """
    return info_gain(x, y) / entropy(x)

# print(f'R(D,A0) = {info_gain_ratio(xtrain[:, 0], ytrain)}')
# print(f'R(D,A1) = {info_gain_ratio(xtrain[:, 1], ytrain)}')
# print(f'R(D,A2) = {info_gain_ratio(xtrain[:, 2], ytrain)}')
# print(f'R(D,A3) = {info_gain_ratio(xtrain[:, 3], ytrain)}')

def gini_index(y):
    """
    计算基尼指数
    :param y: 数据集的目标值
    :return: 基尼指数
    """
    _,counts = np.unique(y,return_counts=True)
    return 1-np.sum((counts/y.size) **2)

def gini_with_feature(x, y):
    """
    计算给定特征后的基尼指数
    :param x: 给定的特征
    :param y: 数据集的目标值
    :return: 给定特征后的基尼指数
    """
    values,counts = np.unique(x,return_counts=True)
    gini = 0
    for value in values:
        prob = x[x==value].size/x.size
        gini +=prob*gini_index(y[x==value])
    return gini

# print(f'G(D)   ={gini_index(ytrain)}')    
# print(f'G(D,A0)={gini_with_feature(xtrain[:,0],ytrain)}')    
# print(f'G(D,A1)={gini_with_feature(xtrain[:,1],ytrain)}')    
# print(f'G(D,A2)={gini_with_feature(xtrain[:,2],ytrain)}')    
# print(f'G(D,A3)={gini_with_feature(xtrain[:,3],ytrain)}')    

# sklearn决策树分类器
# model = DecisionTreeClassifier()
#优化一下
model = DecisionTreeClassifier(
    criterion='log_loss', # 这里使用entropy没有优化
    ccp_alpha=0.01
)
#训练模型
model.fit(xtrain,ytrain)
# 预测结果
y_pred = model.predict(xtest)
print(classification_report(ytest,y_pred))

# 视化决策树
plt.figure(figsize=(12, 10))
plot_tree(
    decision_tree=model,               # 决策树模型
    feature_names=iris.feature_names,  # 特征的名称
    class_names=iris.target_names,     # 标签的名称
    filled=True                        # 用颜色填充
)
plt.show()