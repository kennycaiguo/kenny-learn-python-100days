import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 数据集的加载和划分
iris = load_iris()
X, y = iris.data, iris.target

xtrain,xtest,ytrain,ytest = train_test_split(X,y,train_size=0.8,random_state=3)
# 将数据处理成数据集格式DMatrix格式
dm_train = xgb.DMatrix(xtrain,ytrain)
dm_test = xgb.DMatrix(xtest)

# 设置模型参数
params = {
    'booster': 'gbtree',           # 用于训练的基学习器类型
    'objective': 'multi:softmax',  # 指定模型的损失函数
    'num_class': 3,                # 类别的数量
    'gamma': 0.1,                  # 控制每次分裂的最小损失函数减少量
    'max_depth': 6,                # 决策树最大深度
    'lambda': 2,                   # L2正则化权重
    'subsample': 0.8,              # 控制每棵树训练时随机选取的样本比例
    'colsample_bytree': 0.8,       # 用于控制每棵树或每个节点的特征选择比例
    'eta': 0.001,                  # 学习率
    'seed': 10,                    # 设置随机数生成器的种子
    'nthread': 16,                 # 指定了训练时并行使用的线程数
}
# 训练模型，使用train接口而不是fit
model = xgb.train(params,dm_train,num_boost_round=200)
#预测
ypred = model.predict(dm_test)
# 输出模型评估报告
print(classification_report(ytest, ypred))

xgb.plot_importance(model)
plt.grid(False)
plt.show()