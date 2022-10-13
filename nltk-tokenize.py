from lib2to3.pgen2 import token
from nltk.tokenize import sent_tokenize, word_tokenize

text = "Günlerdir gündem eski bir TSK mensubu, Mehmet Ali Çelebi. Tanınmış bir isim. Türk Silahlı Kuvvetleri’nde teğmenken Ergenekon soruşturması kapsamında tutuklandı."

word_tokenler = word_tokenize(text)

print(word_tokenler)

sent_tokenler = sent_tokenize(text)

print(sent_tokenler)

for token in word_tokenize(text):
    print(token)

for token in sent_tokenize(text):
    print(token)

    