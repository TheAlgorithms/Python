import json, re, glob, os 
from gensim.models import word2vec  # word2vec algorithm
from nltk.tokenize import word_tokenize # document tokenization
from nltk.corpus import stopwords # list of words that we exclude from the corpus
from sklearn.manifold import TSNE # for visualizing high-dimensional data
import matplotlib.pyplot as plt # for plotting
import pandas as pd

stop_words = set(stopwords.words('english'))

"""
This is the class of Word Embeddings.
Model is trained with word2vec algorithm (https://youtu.be/c3yRH0XZN2g)
"""
class WordVectors(object):
    def __init__(self, model):
        """
        Init function which takes in a trained model
        """
        self._model = model
        self._wv = model.wv
        self._vocab = model.wv.vocab
    
    def analogy(self, x1, x2, y1):
        """
        Tries to find a word which has a similar relation to y1, as x2 has to x1
        """
        x1, x2, y1 = x1.lower(), x2.lower(), y1.lower()
        assert self.is_in_vocab(x1) and self.is_in_vocab(x2) and self.is_in_vocab(y1), \
                                        'every word must be in the vocabulary'
        result = self._wv.most_similar(positive=[y1, x2], negative=[x1])[0][0]
        return result
    
    def n_similarity(self, list1, list2):
        """
        Returns similarity score between two lists of words
        """
        list1 = [word.lower() for word in list1 if self.is_in_vocab(word)]
        list2 = [word.lower() for word in list2 if self.is_in_vocab(word)]
        
        assert list1 and list2, 'at least one word from each list must be in the vocabulary'
        score = self._wv.n_similarity(list1, list2)
        return score
    
    def similarity(self, w1, w2):
        """
        Returns similarity score between two words
        """
        w1, w2 = w1.lower(), w2.lower()
        assert self.is_in_vocab(w1) and self.is_in_vocab(w2), 'both words must be in the vocabulary'
        score = self._wv.similarity(w1, w2)
        return score
    
    def closest_words(self, word):
        """
        Returns similar words for a given word
        """
        word = word.lower()
        assert self.is_in_vocab(word), 'the word must be in the vocabulary'
        close_words = self._wv.similar_by_word(word)
        return close_words
    
    def plot_closest_words(self, word, plot=True):
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
    
    def is_in_vocab(self, word):
        """
        Checks if model's vocabulary contains the word
        """
        return word.lower() in self._vocab

        
    def save(self, filename='word2vec'):
        """
        Saves trained model
        """
        full_name = filename + '.model'
        self._model.save(full_name)
                
    @staticmethod
    def _parse_document(text):
        """
        Parses give text document and returns list of tokens
        """
        tokens = word_tokenize(text)
        splitted_tokens = []
        for token in tokens:
            splitted_tokens.extend(re.split('[^0-9a-zA-Z+.#]+', token))
        parsed = [word.lower() for word in splitted_tokens if word and word not in stop_words]
        return parsed
        
        
    @classmethod
    def train(cls, file_dir, size=100, window=5, min_count=5, iterations=5):
        """
        Takes a path of directory which contains text documents and trains word2vec model on the data.
        Args:
            file_dir - path of the directory
            size - dimension of word embeddings
            window - window size for word2vec algorithm
            min_count - minimum number of occurences for a word to be considered
            iterations - number of iterations on a whole corpus
        """
        documents = []
        full_path = os.path.join(file_dir, '*')
        print('parsing documents')
        for filename in glob.glob(full_path):
            try:
                with open(os.path.join(os.getcwd(), filename), encoding = "ISO-8859-1") as f:
                    text = f.read()
                parsed = WordVectors._parse_document(text)
                documents.append(parsed)
            except:
                continue
        print('training started')
        if documents:
            model = word2vec.Word2Vec(documents, size=size, window=window, min_count=min_count, sg=1, 
                                  iter=iterations)
            print('training finished')
            return cls(model)
        else:
            print('There is no data for training')
            return None
    
    
    @classmethod
    def load(cls, model_path):
        """
        Loads existing model
        """
        model = word2vec.Word2Vec.load(model_path)
        return cls(model)
    
        