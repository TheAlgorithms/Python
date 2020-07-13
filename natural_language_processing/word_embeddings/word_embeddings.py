import re
import glob
import os
from gensim.models import word2vec  # word2vec algorithm
import nltk
from nltk.corpus import stopwords  # list of words that we exclude from the corpus
from nltk.tokenize import word_tokenize  # document tokenization
from sklearn.manifold import TSNE  # for visualizing high-dimensional data
import matplotlib.pyplot as plt  # for plotting
import pandas as pd
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

"""
This is the class of Word Embeddings.
Model is trained with word2vec algorithm (https://youtu.be/c3yRH0XZN2g)
"""


class WordVectors(object):
    def __init__(self, model: word2vec.Word2Vec):
        """
        Init function which takes in a trained model
        """
        self._model = model
        self._wv = model.wv
        self._vocab = model.wv.vocab

    def analogy(self, x1: str, x2: str, y1: str) -> str:
        """
        Tries to find a word which has a similar relation to y1, as x2 has to x1
        >>> self.analogy("boy", "girl", "prince")
        "princess" (this is just a guess, model may return somemthing else)
        """
        x1, x2, y1 = x1.lower(), x2.lower(), y1.lower()
        error_msg = 'every word must be in the vocabulary'
        assert all(self.is_in_vocab(x) for x in (x1, x2, y1)), error_msg
        result = self._wv.most_similar(positive=[y1, x2], negative=[x1])[0][0]
        return result

    def n_similarity(self, list1: list, list2: list) -> float:
        """
        Returns similarity score between two lists of words
        >>> self.n_similarity(["boy", "prince"], ["girl", "princess"])
        0.9 (this is just a guess, model may return somemthing else)
        """
        list1 = [word.lower() for word in list1 if self.is_in_vocab(word)]
        list2 = [word.lower() for word in list2 if self.is_in_vocab(word)]
        error_msg = 'at least one word from each list must be in the vocabulary'
        assert list1 and list2, error_msg
        score = self._wv.n_similarity(list1, list2)
        return score

    def similarity(self, w1: str, w2: str) -> float:
        """
        Returns similarity score between two words
        >>> self.similarity("boy", "girl")
        0.75 (this is just a guess, model may return somemthing else)
        """
        w1, w2 = w1.lower(), w2.lower()
        error_msg = 'both words must be in the vocabulary'
        assert self.is_in_vocab(w1) and self.is_in_vocab(w2), error_msg
        score = self._wv.similarity(w1, w2)
        return score

    def closest_words(self, word: str) -> list:
        """
        Returns similar words for a given word
        >>> self.closest_words("girl")
        list of (word, score) pairs
        """
        word = word.lower()
        error_msg = 'the word must be in the vocabulary'
        assert self.is_in_vocab(word), error_msg
        close_words = self._wv.similar_by_word(word)
        return close_words

    def plot_closest_words(self, word: str, plot=True):
        """
        plots similar words for a given word on a 2d space
        """
        close_words = self.closest_words(word)
        words = [word for word, score in close_words]
        words.append(word.lower())
        vectors = self._wv[words]
        tsne = TSNE(n_components=2)
        X_tsne = tsne.fit_transform(vectors)
        df = pd.DataFrame(X_tsne, index=words, columns=['x', 'y'])
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.scatter(df['x'], df['y'])
        for word, pos in df.iterrows():
            ax.annotate(word, pos)
        if plot:
            plt.show()
        else:
            fig.savefig('figure.png')

    def is_in_vocab(self, word: str) -> bool:
        """
        Checks if model's vocabulary contains the word
        >>> self.is_in_vocab("boy")
        True
        """
        return word.lower() in self._vocab

    def save(self, filename='word2vec'):
        """
            Saves trained model
        """
        full_name = filename + '.model'
        self._model.save(full_name)

    @staticmethod
    def _parse_document(text: str) -> list:
        """
        Parses give text document and returns list of tokens
        """
        tokens = word_tokenize(text)
        splitted_tokens = []
        for token in tokens:
            splitted_tokens.extend(re.split('[^0-9a-zA-Z+.#]+', token))
        parsed = [word.lower() for word in splitted_tokens
                  if word and word not in stop_words]
        return parsed

    @classmethod
    def train(cls, file_dir: str, size=100, window=5,
              min_count=5, iterations=5):
        """
        Takes a path of directory which contains text documents
        and trains word2vec model on the data.
        Args:
            file_dir - path of the directory
            size - dimension of word embeddings
            window - window size for word2vec algorithm
            min_count - minimum number of occurrences for a word to be considered
            iterations - number of iterations on a whole corpus
        """
        documents = []
        full_path = os.path.join(file_dir, '*')
        print('parsing documents')
        for filename in glob.glob(full_path):
            try:
                with open(os.path.join(os.getcwd(), filename),
                          encoding="ISO-8859-1") as f:
                    text = f.read()
                parsed = WordVectors._parse_document(text)
                documents.append(parsed)
            except IOError:
                continue
        print('training started')
        if documents:
            model = word2vec.Word2Vec(documents, size=size, window=window,
                                      min_count=min_count, sg=1, iter=iterations)
            print('training finished')
            return cls(model)
        else:
            print('There is no data for training')
            return None

    @classmethod
    def load(cls, model_path: str):
        """
        Loads existing model
        """
        model = word2vec.Word2Vec.load(model_path)
        return cls(model)
