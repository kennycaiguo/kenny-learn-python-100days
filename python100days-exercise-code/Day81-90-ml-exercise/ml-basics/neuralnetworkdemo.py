from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier

iris = load_iris()

X,y = iris.data,iris.target
xtrain,xtest,ytrain,ytest = train_test_split(X,y,train_size=0.8,random_state=3)

# 创建多层感知机分类器模型
model = MLPClassifier(
    solver='lbfgs',
    learning_rate='adaptive',
    activation='relu',
    hidden_layer_sizes=(32,32,32) # 隐藏层不要只放1层，效果很差的。
)
#训练模型
model.fit(xtrain,ytrain)
#模型预测
ypred = model.predict(xtest)
# 模型评估
print(classification_report(ytest,ypred))