import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import os
import ast

# 读取CSV文件
filepath = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(os.path.join(filepath, 'data', 'word_freq.csv'), header=None, names=['label', 'features'])


# 对第二列进行处理
df['features'] = df['features'].apply(lambda x: ast.literal_eval(x.replace("'", '"')))
df['features'] = df['features'].apply(lambda x: [list(item) if isinstance(item, tuple) else item for item in x])

print(df)

# 分割数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(df['features'], df['label'], test_size=0.2, random_state=42)

# 使用词袋模型将文本转换为特征向量
vectorizer = CountVectorizer(tokenizer=lambda x: x)  # 使用一个简单的分词器，直接返回输入
X_train = vectorizer.fit_transform(X_train.apply(lambda x: ' '.join(map(str, x))))
X_test = vectorizer.transform(X_test.apply(lambda x: ' '.join(map(str, x))))

# 初始化朴素贝叶斯分类器
classifier = MultinomialNB()

# 训练模型
classifier.fit(X_train, y_train)

# 进行预测
y_pred = classifier.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')


# 新数据
new_data = ["tz"]  # 你的新数据，这里只有一个特征

# 将新数据转换为特征向量
new_data_vectorized = vectorizer.transform([' '.join(map(str, new_data))])

# 进行预测
prediction = classifier.predict(new_data_vectorized)

# 输出预测结果
print(f'预测结果: {prediction[0]}')