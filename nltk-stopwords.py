from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "Romeo ve Juliet Hikâyesi düşman olan iki ailenin kızı ve oğlunun aşkını anlatmaktadır. Verona’da yaşayan ve uzun süredir düşman olan iki zengin aile varmış. Bu ailelerden biri Montegü diğeri ise Kapulet olarak adlandırılmaktaymış. Kapuletler’in balosunda tesadüfen Juliet ve Montegu’nun oğlu Romeo karşılaşmışlar. Bu karşılaşma sonucunda birbirlerine büyük bir sevgi ve aşk ile bağlanmışlar."

print(stopwords.words("turkish"))

turkish_word = stopwords.words("turkish")

words = word_tokenize(text)

filtered_words = []

for word in words:
    if word not in turkish_word:
        filtered_words.append(word)

print(filtered_words)

