from flask import Flask,jsonify,request
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import xgboost as xgb
import numpy as np


xgbmodel = joblib.load("./xgbmodel.pkl")
scaler = StandardScaler()

title_mapping = {
    'Mr': 0, 'Miss': 1, 'Mrs': 2, 'Master': 3, 'Dr': 4, 'Rev': 5, 'Col': 6, 'Major': 7, 
    'Mlle': 8, 'Ms': 9, 'Lady': 10, 'Sir': 11, 'Jonkheer': 12, 'Don': 13, 'Dona': 14, 'Countess': 15
}

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

# print(xgbmodel.predict(xtest))

# web服务
app = Flask(__name__)

@app.route("/predict",methods=['POST'])
def predict():
    query_df = pd.DataFrame(request.json)
    #使用我们上面加载的模型
    ypred = (xgbmodel.predict(xgb.DMatrix(query_df))>0.5).tolist()
    return jsonify({'message': 'OK', 'result': ypred})

app.run(debug=True)