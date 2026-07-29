import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sympy import rotations
import xgboost as xgb

# 修改配置添加中文字体
plt.rcParams['font.sans-serif'].insert(0, 'SimHei',)
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

# 模型训练xgboost
# 将数据处理成数据集格式DMatrix格式
dm_train = xgb.DMatrix(xtrain, ytrain)
dm_valid = xgb.DMatrix(xvalid)

# 设置模型参数
params = {
    'booster': 'gbtree',             # 用于训练的基学习器类型
    'objective': 'binary:logistic',  # 指定模型的损失函数
    'gamma': 0.1,                    # 控制每次分裂的最小损失函数减少量
    'max_depth': 10,                 # 决策树最大深度
    'lambda': 0.5,                   # L2正则化权重
    'subsample': 0.8,                # 控制每棵树训练时随机选取的样本比例
    'colsample_bytree': 0.8,         # 用于控制每棵树或每个节点的特征选择比例
    'eta': 0.05,                     # 学习率
    'seed': 3,                       # 设置随机数生成器的种子
    'nthread': 16,                   # 指定了训练时并行使用的线程数
}

model = xgb.train(params,dm_train,num_boost_round=200)
ypred = model.predict(dm_valid)

### 模型评估

# 接下来我们加载真正的测试数据`test.csv`，通过前面训练好的模型来做出预测。我们可以将预测的结果保存成一个 CSV 文件，该文件共有两列，
# 一列是 PassengerID，一列是我们预测的结果。我们将该文件提交到 Kaggle 平台，可以获得最终模型的准确率评分。
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

passenger_id, xtest = test.index, xgb.DMatrix(test)
y_test_pred = (model.predict(xtest) > 0.5).astype('i8')

# 生成提交文件
result = pd.DataFrame({
    'PassengerId': passenger_id,
    'Survived': y_test_pred
})
result.to_csv('xgbsubmission.csv', index=False)

# 序列号模型，方便后期部署
joblib.dump(model,'xgbmodel.pkl')