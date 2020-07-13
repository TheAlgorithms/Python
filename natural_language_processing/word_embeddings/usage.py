from word_embeddings import WordVectors
import os

# directory of your corpus
corpus_dir = 'corpus/'

# load the model if it exists
if os.path.exists('word2vec.model'):
    model = WordVectors.load('word2vec.model')
# create a new one
else:
    model = WordVectors.train(corpus_dir)
    model.save()


# similarity between two words
word1 = 'merge'
word2 = 'unify'
score = model.similarity(word1, word2)
print('similarity between {} and {} is {}'.format(word1, word2, score))

# word analogies
x1 = 'boy'
x2 = 'prince'
y1 = 'girl'
y2 = model.analogy(x1, x2, y1)
print('{} <--> {}  |  {} <--> {}'.format(x1, x2, y1, y2))

# closest words
word = 'request'
close_words = model.closest_words(word)
print(close_words)

# plot closest words
word = 'request'
model.plot_closest_words(word, plot=False) # download the plot
