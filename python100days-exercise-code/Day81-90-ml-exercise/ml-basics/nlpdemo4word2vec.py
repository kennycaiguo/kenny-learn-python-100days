import re

from datasets import load_dataset
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

# 加载 IMDB 数据集
# imdb = load_dataset('imdb') # 会报错
imdb = load_dataset('stanfordnlp/imdb')
# 直接将 50000 条评论用作语料
temp = [imdb['unsupervised'][i]['text'] for i in range(50000)]
# 用正则表达式对评论文本进行简单处理
corpus = [re.sub(r'[^\w\s]', '', x) for x in temp]

# 预处理语料库（英文分词）
sentences = [sentence.lower().split() for sentence in corpus]
# 训练 Word2Vec 模型
# sentences - 输入语料库（句子构成的列表，每个句子是一个或多个单词的列表）
# vector_size - 词向量的维度（维度越高能够表示的信息越多）
# windows - 上下文窗口大小（模型在训练时使用的上下文单词的范围）
# min_count - 忽略频率低于此值的单词（过滤掉在语料库中出现次数较少的单词）
# workers - 训练时使用的 CPU 核心数量
# seed - 随机数种子（用于初始化模型的权重）
model = Word2Vec(sentences, vector_size=100, window=10, min_count=2, workers=4, seed=3)

# 通过模型获取 king 和 queen 的词向量
king_vec, queen_vec = model.wv['king'], model.wv['queen']

# 计算两个词向量的余弦相似度
cos_similarity = cosine_similarity([king_vec], [queen_vec])
print(f'king 和 queen 的余弦相似度: {cos_similarity[0, 0]:.2f}')

# 通过词向量进行推理（king - man + woman ≈ queen）
man_vec, woman_vec = model.wv['man'], model.wv['woman']
result_vec = king_vec - man_vec + woman_vec
# 查找与计算结果最相似的三个词
similar_words = model.wv.similar_by_vector(result_vec, topn=3)
print(f'跟 king - man + woman 最相似的词:\n {similar_words}')

# 查找与 dog 最相似的五个词
dog_similar_words = model.wv.most_similar('dog', topn=5)
print(f'跟 dog 最相似的词:\n {dog_similar_words}')