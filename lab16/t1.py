import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('stopwords')

file_id = 'blake-poems.txt'
text = gutenberg.raw(file_id)

tokens = nltk.word_tokenize(text)
print(f"Общее количество слов в тексте: {len(tokens)}")

fdist = FreqDist(tokens)
top10_words = fdist.most_common(10)

import matplotlib.pyplot as plt
words, counts = zip(*top10_words)
plt.figure(figsize=(10, 5))
plt.bar(words, counts)
plt.title('Top 10 Most Frequent Words')
plt.show()

stop_words = set(stopwords.words('english') + list(string.punctuation))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

fdist_filtered = FreqDist(filtered_tokens)
top10_filtered_words = fdist_filtered.most_common(10)

words_filtered, counts_filtered = zip(*top10_filtered_words)
plt.figure(figsize=(10, 5))
plt.bar(words_filtered, counts_filtered, color='green')
plt.title('Top 10 Most Frequent Words without Stopwords and Punctuation')
plt.show()
