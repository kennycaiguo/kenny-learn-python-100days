import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

iris = load_iris()
X,y = iris.data,iris.target

# 创建KMeans对象
model = KMeans(
    n_clusters=3,       # k值（簇的数量）
    max_iter=30,        # 最大迭代次数
    n_init=10,          # 初始质心选择尝试次数
    init='k-means++',   # 初始质心选择算法
    algorithm='elkan',  # 是否使用三角不等式优化
    tol=1e-4,           # 质心变化容忍度
    random_state=3      # 随机数种子
)

model.fit(X)
print(model.labels_)
print(model.cluster_centers_)
print(model.inertia_)