import ssl
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


"""
车 MPG 数据集最初由美国汽车协会提供，我们可以通过该数据集预测车辆的燃油效率，即每加仑燃料行驶的里程(Miles Per Gallon, MPG)
需要注意的是，scikit-learn 库没有内置该数据集，我们可以直接从 [UCI 机器学习仓库](https://archive.ics.uci.edu/dataset/9/auto+mpg) 网站下载数据集，
也可以通过执行下面的代码联网加载该数据集。
"""

ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_csv('https://archive.ics.uci.edu/static/public/9/data.csv')
# df.info()
"""
| 属性名称       | 描述                                                         |
| -------------- | ------------------------------------------------------------ |
| *car_name*     | 汽车的名称，字符串，这个属性对建模暂时没有帮助               |
| *cylinders*    | 气缸数量，整数                                               |
| *displacement* | 发动机排量（立方英寸），浮点数                               |
| *horsepower*   | 马力，浮点数，有空值需要提前处理                             |
| *weight*       | 汽车重量（磅），整数                                         |
| *acceleration* | 加速（0 - 60 mph所需时间），浮点数                           |
| *model_year*   | 模型年份（1970年 - 1982年），这里用的是两位的年份            |
| *origin*       | 汽车来源（1 = 美国, 2 = 欧洲, 3 = 日本），这里的`1`、`2`、`3`应该视为三种类别而不是整数 |
| *mpg*          | 车辆的燃油效率，每加仑行驶的里程（目标变量）                 |
"""
# car_name列对于建模没有作用，我们可以删除它
df.drop(columns=['car_name'],inplace=True)
# print(df.head())
# print(df.corr())
# 删除有缺失值的样本
df.dropna(inplace=True)
# 将origin字段处理为类别类型
df['origin'] = df['origin'].astype('category')
# 将origin字段处理为独热编码,可以用pandas来处理,也可以使用sklearn库中`preprocessing`模块的`OneHotEncoder`来处理
df = pd.get_dummies(df,columns=['origin'],drop_first=True) # 不要第一个
# print(df.head())
# mpg列是目标值,其他是特征值,我们来划分数据集
X,y = df.drop(columns=['mpg']),df['mpg'] # 注意,这里的drop不要把inplace设置为true,我们用一个新生成的df中文特征值,并不需要修改原来的数据

# 对特征进行选择和标准化处理
scaler = StandardScaler()
scaled_X = scaler.fit_transform(X.iloc[:, [1, 2, 3, 5]])

xtrain,xtest,ytrain,ytest = train_test_split(scaled_X,y,train_size=0.8,random_state=3)
# 梯度下降实现
model = SGDRegressor()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)

# 查看线性回归模型的参数（回归系数和截距）
# print(f"回归系数:{model.coef_}")
# print(f"截距:{model.intercept_}")

# 回归模型的评估
mse = mean_squared_error(ytest,ypred)
mae = mean_absolute_error(ytest,ypred)
r2 = r2_score(ytest,ypred)
print(f"mean_squared_error:{mse}")
print(f"mean_absolute_error:{mae}")
print(f"r2_score:{r2}")