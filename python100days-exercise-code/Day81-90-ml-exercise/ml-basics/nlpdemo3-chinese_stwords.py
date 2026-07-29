from sklearn.feature_extraction.text import CountVectorizer
import jieba

stop_words_list = []

#停用词
with open('./stopwords/cn_stopwords.txt') as file_obj:
    stop_words_list = file_obj.read().split('\n')

# 文档列表
documents = [
    '我在四川大学读书',
    '四川大学是四川最好的大学',
    '大学校园里面有很多学生',
]


cv = CountVectorizer(
    tokenizer=lambda x: jieba.cut(x),
    token_pattern=None,
    stop_words=stop_words_list

)
# 创建词袋模型
x = cv.fit_transform(documents)
# 输出词汇表和词频向量
print('词汇表:\n', cv.get_feature_names_out())
print('词频向量:\n', x.toarray())