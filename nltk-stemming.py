from nltk.stem import PorterStemmer
ps = PorterStemmer()

words = ["drive","driving","drove","driver","drives"]

stem_words = []

for i in words:
    stem_words.append(ps.stem(i))

print(stem_words)

