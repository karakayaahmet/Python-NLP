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

# modelin kayıt edilmesi
model.save("word2vec.model")

# modelin yüklenmesi
model = Word2Vec.load("word2vec.model")

def goruntule(model, word):
    word_vector = np.empty((0,100))
    word_labels = [word]

    yakin_kelimeler = model.wv.most_similar(word)
    word_vector = np.append(word_vector, np.array([model.wv[word]]), axis=0)

    for w, _ in yakin_kelimeler:
        word_labels.append(w)
        word_vector = np.append(word_vector, np.array([model.wv[w]]), axis=0)

    tsne = TSNE(random_state=0)
    y = tsne.fit_transform(word_vector) 

    x_coords = y[:, 0]
    y_coords = y[:, 1]

    plt.scatter(x_coords, y_coords)

    for label, x, y in zip(word_labels, x_coords, y_coords):
        plt.annotate(label, xy=(x, y), xytext=(5, -2), textcoords="offset points")

    plt.show()

goruntule(model, "ankara")

