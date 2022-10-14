from re import T
import nltk

nltk.download('maxent_ne_chunker')

text = "i have been learning english."

tokenized = nltk.word_tokenize(text)

tagging = nltk.pos_tag(tokenized)

named_ent = nltk.ne_chunk(tagging)

print(named_ent.draw())
