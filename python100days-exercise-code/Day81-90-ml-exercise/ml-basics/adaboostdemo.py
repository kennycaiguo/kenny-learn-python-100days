from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report

iris = load_iris()
X,y = iris.data,iris.target

xtrain,xtest,ytrain,ytest = train_test_split(X,y,train_size=0.8,random_state=3)
# 初始化弱分类器（决策树桩）
base_estimator = DecisionTreeClassifier(max_depth=1)
# 初始化 AdaBoost 分类器
model = AdaBoostClassifier(base_estimator,n_estimators=50)
# 训练模型
model.fit(xtrain,ytrain)
# 预测
ypred = model.predict(xtest)

print(classification_report(ytest,ypred))