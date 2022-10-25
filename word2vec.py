import numpy as np
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

f = open("hurriyet.txt","r",encoding="utf-8")
text = f.read()
t_list = text.split("\n")
corpus = []
for cumle in t_list:
    corpus.append(cumle.split())

print(corpus[:10])

model = Word2Vec(corpus, window=5, min_count=5, sg=1 )

print(model.wv["ankara"])

print(model.wv.most_similar("hollanda"))

print(model.wv.most_similar("pazartesi"))