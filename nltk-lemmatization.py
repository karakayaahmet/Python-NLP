import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('omw-1.4')

lem = WordNetLemmatizer()

words = ["drive","driving","drives","driver","drove","droven"]

lem_words = []

for i in words:
    lem_words.append(lem.lemmatize(i))

print(lem_words)