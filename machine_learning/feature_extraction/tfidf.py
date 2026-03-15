import numpy as np
import re
# to seprate words and normlize it


def decompose(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)

    return text.split()


# creating tfidf class
class TfIdfVectorizer:
    def __init__(self):
        self.vocab = None
        self.idf = None

    # these method to compute the tf for each word in given data
    def compute_tf(self, data):
        tf = []
        doc_words = []

        for document in data:
            words = decompose(document)

            freq = {}  # these dictionerie have for each unique words it number of apprition in one sentence

            for word in words:
                freq[word] = freq.get(word, 0) + 1

                if word not in doc_words:
                    doc_words.append(word)

            # calculating tf

            for word in freq:
                freq[word] /= len(words)

            tf.append(freq)

        # computing idf
        idf = {}

        n = len(data)

        for word in doc_words:
            df = sum(1 for doc in tf if word in doc)
            idf[word] = np.log((n + 1) / (1 + df)) + 1

        self.idf = idf
        tfidf = []

        self.idf = idf

        # computing tfidf for each word

        for doc_tf in tf:
            vector = [doc_tf.get(word, 0) * idf[word] for word in doc_words]
            tfidf.append(vector)

        self.vocab = doc_words

        return np.array(tfidf, dtype=float)

    def encode(self, data):
        if self.vocab is None or self.idf is None:
            raise ValueError("You should fit the model first")

        tfidf_matrix = []
        for doc in data:
            words = decompose(doc)
            freq = {}

            # Count term frequencies for words that exist in the vocabulary
            for word in words:
                if word in self.vocab:
                    freq[word] = freq.get(word, 0) + 1

            # Normalize TF by document length
            for word in freq:
                freq[word] /= len(words)

            # Align vector according to vocab and multiply by IDF
            vector = [freq.get(word, 0) * self.idf[word] for word in self.vocab]
            tfidf_matrix.append(vector)

        return np.array(tfidf_matrix, dtype=float)


if __name__ == "__main__":
    documents = ["the cat sat on the mat", "the dog chased the cat"]
    vectorizer = TfIdfVectorizer()
    tfidf_matrix = vectorizer.compute_tf(documents)
    print("Vocabulary:", vectorizer.vocab)
    print("TF-IDF Matrix:\n", tfidf_matrix)
