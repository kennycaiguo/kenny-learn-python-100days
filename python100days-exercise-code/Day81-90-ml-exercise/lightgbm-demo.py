import lightgbm as lgb
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 加载和划分数据集
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=3)

# 将数据转化为 LightGBM 的数据格式
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

# 设置模型参数
params = {
    'objective': 'multiclass',   # 多分类问题
    'num_class': 3,              # 类别数量
    'metric': 'multi_logloss',   # 多分类对数损失函数
    'boosting_type': 'gbdt',     # 使用梯度提升树算法
    'num_leaves': 31,            # 叶子节点数
    'learning_rate': 0.05,       # 学习率
    'feature_fraction': 0.75,    # 每次训练时随机选择特征的比例
    'early_stopping_rounds': 10  # 连续多少论没有性能提升就停止迭代
}
# 模型训练
model = lgb.train(params=params, train_set=train_data, num_boost_round=200, valid_sets=[test_data])
# 模型预测
y_pred = model.predict(X_test, num_iteration=model.best_iteration)
# 将预测结果处理成标签
y_pred_max = np.argmax(y_pred, axis=1)

# 查看模型评估报告
print(classification_report(y_test, y_pred_max))