from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix,ConfusionMatrixDisplay
from sklearn.metrics import roc_curve,auc,RocCurveDisplay

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

matplotlib.use('TkAgg')

iris = load_iris()
# print(iris.DESCR)
# 特征（150行4列的二维数组，分别是花萼长、花萼宽、花瓣长、花瓣宽）
x = iris.data
# 标签（150个元素的一维数组，包含0、1、2三个值分别代表三种鸢尾花）
y = iris.target
# print(y)
xtrain,xtest,ytrain,ytest = train_test_split(x,y,train_size=0.8,random_state=3)

# 手动实现knn
def euclidean_distance(u, v):
    return np.sqrt(np.sum(np.abs(u - v) ** 2))

def make_label(X_train, y_train, X_one, k):
     """
        根据历史数据中k个最近邻为新数据生成标签
        :param X_train: 训练集中的特征
        :param y_train: 训练集中的标签
        :param X_one: 待预测的样本（新数据）特征
        :param k: 邻居的数量
        :return: 为待预测样本生成的标签（邻居标签的众数）
     """
     # 计算x跟每个训练样本的距离
     distes = [euclidean_distance(X_one, X_i) for X_i in X_train]
     # 通过一次划分找到k个最小距离对应的索引并获取到相应的标签
     labels = y_train[np.argpartition(distes, k - 1)[:k]]
     # 获取标签的众数
     return stats.mode(labels).mode

def predict_by_knn(X_train, y_train, X_new, k=5):
    """
    KNN算法
    :param X_train: 训练集中的特征
    :param y_train: 训练集中的标签
    :param X_new: 待预测的样本构成的数组
    :param k: 邻居的数量（默认值为5）
    :return: 保存预测结果（标签）的数组
    """
    return np.array([make_label(X_train, y_train, X, k) for X in X_new])

# y_pred = predict_by_knn(xtrain,ytrain,xtest)
# print(y_pred == ytest)

# 用sklearn实现knn
# 1.创建模型
model = KNeighborsClassifier()
# 2.训练模型
model.fit(xtrain,ytrain)
# 3.模型预测
y_pred = model.predict(xtest)
# 模型评估
# print(y_pred == ytest)
# print(model.score(xtest,ytest))

# 输出分类模型混淆矩阵
# print('混淆矩阵: ')
# print(confusion_matrix(ytest,y_pred))
# 输出分类模型评估报告
# print('评估报告: ')
# print(classification_report(ytest,y_pred))

# 可视化的方式输出混淆矩阵
# disp_cm = ConfusionMatrixDisplay(confusion_matrix(ytest,y_pred),display_labels=iris.target_names)
# disp_cm.plot(cmap=plt.cm.Reds)
# plt.show()

gs = GridSearchCV(
    estimator=KNeighborsClassifier(),
    param_grid={
        'n_neighbors':[1,3,5,7,9,11,13,15],
        'weights':['uniform','distance'],
        'p':[1,2]
    },
    cv=5

)

gs.fit(xtrain,ytrain)

print('最优参数:', gs.best_params_)
print('评分:', gs.best_score_)

print(gs.predict(xtest))