from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# 生成1000条样本数据，每个样本包含6个特征
X, y = make_classification(n_samples=1000, n_features=6, random_state=3)
# 将1000条样本数据拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=3)

# 创建和训练逻辑回归模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 对测试集进行预测并评估
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))