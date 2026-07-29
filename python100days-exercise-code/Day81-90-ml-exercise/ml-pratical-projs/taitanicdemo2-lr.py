import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sympy import rotations

# 修改配置添加中文字体
plt.rcParams['font.sans-serif'].insert(0, 'SimHei')
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./t_data/data.csv', index_col='PassengerId')
# print(df.head())

# 特征工程
# 1.空值处理
df["Age"] = df.Age.fillna(df.Age.median()) # 用中位数填充年龄的缺失值
df['Embarked'] = df.Embarked.fillna(df.Embarked.mode()[0]) # 用众数来填充登船港口
# 客舱号处理方式是二值化，有客舱号的记为`1`，没有客舱号的记为`0`
df['Cabin'] = df.Cabin.replace(r'.+', '1', regex=True).replace(np.nan, 0).astype('i8')

# 处理完缺失值后，我们对年龄和船票价格两个字段进行特征缩放，通过`StandardScaler`实现标准化
scaler = StandardScaler()
df[['Fare','Age']] = scaler.fit_transform(df[['Fare','Age']] )
# 还需要对性别和登船港口两个字段进行独热编码处理，可以使用 pandas 库中的`get_dummies`函数或 scikit-learn 库的`OneHotEncoder`处理，两者处理的结果类似
df = pd.get_dummies(df,columns=['Sex','Embarked'],drop_first=True)
# 我们继续处理乘客姓名字段，根据姓名中的称谓衍生出一个新的特征；此外，对于`SibSp`和`Parch`两个字段，我们可以将其衍生为家庭成员数量的新特征
title_mapping = {
    'Mr': 0, 'Miss': 1, 'Mrs': 2, 'Master': 3, 'Dr': 4, 'Rev': 5, 'Col': 6, 'Major': 7, 
    'Mlle': 8, 'Ms': 9, 'Lady': 10, 'Sir': 11, 'Jonkheer': 12, 'Don': 13, 'Dona': 14, 'Countess': 15
}

df['Title'] = df['Name'].map(
    lambda x:x.split(',')[1].split('.')[0].strip()
).map(title_mapping).fillna(-1)

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
# 我们可以把不必要的字段全部删除掉，数据的准备工作就基本完成了
df.drop(columns=['Name','SibSp','Parch','Ticket'], inplace=True)

# 模型训练
## 1.数据集划分
X,y = df.drop(columns='Survived'),df.Survived
xtrain,xvalid,ytrain,yvalid = train_test_split(X,y,train_size=0.9,random_state=3)

## 1>逻辑回归
model = LogisticRegression(penalty='l1', tol=1e-6, solver='liblinear')
## 训练模型
model.fit(xtrain,ytrain)
## 模型预测
ypred = model.predict(xvalid)
print(classification_report(yvalid,ypred))

test = pd.read_csv('t_data/test.csv', index_col='PassengerId')
# 处理缺失值
test['Age'] = test.Age.fillna(test.Age.median())
test['Fare'] = test.Fare.fillna(test.Fare.median())
test['Embarked'] = test.Embarked.fillna(test.Embarked.mode()[0])
test['Cabin'] = test.Cabin.replace(r'.+', '1', regex=True).replace(np.nan, 0).astype('i8')
# 特征缩放
test[['Fare', 'Age']] = scaler.fit_transform(test[['Fare', 'Age']])
# 处理类别
test = pd.get_dummies(test, columns=['Sex', 'Embarked'], drop_first=True)
# 特征构造
test['Title'] = test['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip()).map(title_mapping).fillna(-1)
test['FamilySize'] = test['SibSp'] + test['Parch'] + 1
# 删除多余特征
test.drop(columns=['Name', 'Ticket', 'SibSp', 'Parch'], inplace=True)

# 使用逻辑回归模型
passenger_id, X_test = test.index, test
y_test_pred = model.predict(X_test)

# 生成提交文件
result = pd.DataFrame({
    'PassengerId': passenger_id,
    'Survived': y_test_pred
})
result.to_csv('submission.csv', index=False)