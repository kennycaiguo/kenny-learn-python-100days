from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report

iris = load_iris()
X,y = iris.data,iris.target

xtrain,xtest,ytrain,ytest = train_test_split(X,y,train_size=0.8,random_state=3)
# 初始化 GBDT 分类器
model = GradientBoostingClassifier()
# 训练模型
model.fit(xtrain,ytrain)
# 预测
ypred = model.predict(xtest)
# 输出评估报告
print(classification_report(ytest, ypred))