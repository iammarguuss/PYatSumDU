import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

text = "This ebook is for the use of anyone anywhere in the United States and most other parts of the world at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this ebook or online at www.gutenberg.org. If you are not located in the United States, you will have to check the laws of the country where you are located before using this eBook"

tokens = word_tokenize(text)

lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(token) for token in tokens]

stemmer = PorterStemmer()
stemmed = [stemmer.stem(token) for token in lemmatized]

stop_words = set(stopwords.words('english') + list(string.punctuation))
filtered_tokens = [token for token in stemmed if token.lower() not in stop_words]

processed_text = ' '.join(filtered_tokens)

with open('textus.txt', 'w', encoding='utf-8') as f:
    f.write(processed_text)

print("Reverse text was saved.")