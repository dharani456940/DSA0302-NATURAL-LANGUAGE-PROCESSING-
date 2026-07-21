from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

text = "The boys are playing games happily"

words = word_tokenize(text)

stemmer = PorterStemmer()

print("Word\tStem")

for word in words:
    print(word,"\t",stemmer.stem(word))