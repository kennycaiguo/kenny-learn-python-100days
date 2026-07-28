from sklearn.feature_extraction.text import CountVectorizer

# 文档列表
documents = [
    'I love programming.',
    'I love machine learning.',
    'I love apple.'
]

cv = CountVectorizer()
# 创建词袋模型
x = cv.fit_transform(documents)
# 输出词汇表和词频向量
print('词汇表:\n', cv.get_feature_names_out())
print('词频向量:\n', x.toarray())