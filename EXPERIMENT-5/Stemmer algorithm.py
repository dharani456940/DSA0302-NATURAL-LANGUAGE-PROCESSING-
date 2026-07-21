from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing","running","studies","flies","better"]

for word in words:
    print(word,"->",ps.stem(word))