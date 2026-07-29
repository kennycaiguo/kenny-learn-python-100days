import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


def distance(u, v, p=2):
    """计算两个向量的距离"""
    return np.sum(np.abs(u - v) ** p) ** (1 / p)


def init_centroids(X, k):
    """随机选择k个质心"""
    index = np.random.choice(np.arange(len(X)), k, replace=False)
    return X[index]


def closest_centroid(sample, centroids):
    """找到跟样本最近的质心"""
    distances = [distance(sample, centroid) for i, centroid in enumerate(centroids)]
    return np.argmin(distances)


def build_clusters(X, centroids):
    """根据质心将数据分成簇"""
    clusters = [[] for _ in range(len(centroids))]
    for i, sample in enumerate(X):
        centroid_index = closest_centroid(sample, centroids)
        clusters[centroid_index].append(i)
    return clusters


def update_centroids(X, clusters):
    """更新质心的位置"""
    return np.array([np.mean(X[cluster], axis=0) for cluster in clusters])


def make_label(X, clusters):
    """生成标签"""
    labels = np.zeros(len(X))
    for i, cluster in enumerate(clusters):
        for j in cluster:
            labels[j] = i
    return labels


def kmeans(X, *, k, max_iter=1000, tol=1e-4):
    """KMeans聚类"""
    # 随机选择k个质心
    centroids = init_centroids(X, k)
    # 通过不断的迭代对数据进行划分
    for _ in range(max_iter):
        # 通过质心将数据划分到不同的簇
        clusters = build_clusters(X, centroids)
        # 重新计算新的质心的位置
        new_centroids = update_centroids(X, clusters)
        # 如果质心几乎没有变化就提前终止迭代
        if np.allclose(new_centroids, centroids, rtol=tol):
            break
        # 记录新的质心的位置
        centroids = new_centroids
    # 给数据生成标签
    return make_label(X, clusters), centroids

iris = load_iris()
X,y = iris.data,iris.target
label,centers = kmeans(X,k=3)

colors = ['#FF6969', '#050C9C', '#365E32']
markers = ['o', 'x', '^']

plt.figure(dpi=200)
for i in range(len(centers)):
    samples = X[label==i]
    plt.scatter(samples[:, 2], samples[:, 3], marker=markers[i], color=colors[i])
    plt.scatter(centers[i, 2], centers[i, 3], marker='*', color='r', s=120)
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.show()    