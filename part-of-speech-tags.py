import nltk 

text = "Fatih Sultan Mehmet 1453'te İstanbulu fethetmiştir."

tokenized = nltk.word_tokenize(text)

print(nltk.pos_tag(tokenized))