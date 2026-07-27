from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=3)

# 手动实现贝叶斯算法，只是用来了解他的原理
def naive_bayes_fit(X, y):
    """
    :param X: 样本特征
    :param Y: 样本标签
    :returns: 二元组 - (先验概率, 似然性)
    """
    # 计算先验概率
    #
    cls_labels,cls_counts = np.unique(y,return_counts=True)
    # print(cls_labels,cls_counts) # [0 1 2] [40 40 40]
    prior_probs = pd.Series({k:v/y.size for k,v in zip(cls_labels,cls_counts)})
    #给特征值做一个拷贝
    X = np.copy(X)
      # 保存似然性计算结果的字典
    likelihoods = {}
    # 分箱
    for j in range(X.shape[1]):
        X[:,j] = pd.cut(X[:,j],bins=5,labels=np.arange(1,6))
        for i in prior_probs.index:
            x_prime = X[y==1,j]
            x_values,x_counts = np.unique(x_prime,return_counts=True)
            for k,value in enumerate(x_values):
                likelihoods[(i,j,value)] = x_counts[k]/x_prime.size

    return prior_probs, likelihoods            

def naive_bayes_predict(X, p_ci, p_x_ci):
    """
    朴素贝叶斯分类器预测
    :param X: 样本特征
    :param p_ci: 先验概率
    :param p_x_ci: 似然性
    :return: 预测的标签
    """
    # 对特征进行等宽分箱（离散化处理）
    X = np.copy(X)
    for j in range(X.shape[1]):
        X[:,j] = pd.cut(X[:,j],bins=5,labels=np.arange(1,6))
    # 保存每个样本对应每个类别后验概率的二维数组
    results = np.zeros((X.shape[0],p_ci.size))    
    cls_labels = p_ci.index.values
    for k in range(X.shape[0]):
        for i,label in enumerate(cls_labels):
            # 获得先验概率（训练的结果）
            prob = p_ci.loc[label]
            # 计算获得特征数据后的后验概率
            for j in range(X.shape[1]):
                prob *=p_x_ci.get((i,j,X[k,j]),0)
            results[k,i] = prob
    # 根据每个样本对应类别最大的概率选择预测标签
    return cls_labels[results.argmax(axis=1)]            


p_ci,p_x_ci = naive_bayes_fit(X_train, y_train)
# print('先验概率: ', p_ci, sep='\n')
# print('似然性: ', p_x_ci, sep='\n')
y_pred = naive_bayes_predict(X_test,p_ci,p_x_ci)
print(y_pred == y_test)