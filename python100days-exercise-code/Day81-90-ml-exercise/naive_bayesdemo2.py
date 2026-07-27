from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=3)

model = GaussianNB()
model.fit(X_train,y_train)
y_prd = model.predict(X_test)

# print(classification_report(y_test,y_prd))
# 看看朴素贝叶斯模型给每个样本对应到每个标签给出的概率值
print(model.predict_proba(X_test).round(2))