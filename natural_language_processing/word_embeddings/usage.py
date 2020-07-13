from word_embeddings import WordVectors
import os


def main():
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
    print(f'similarity between {word1} and {word2} is {score}')

    # word analogies
    x1 = 'boy'
    x2 = 'prince'
    y1 = 'girl'
    y2 = model.analogy(x1, x2, y1)

    print(f'{x1} <--> {x2}  |  {y1} <--> {y2}')

    print(model.closest_words(word='request'))
    # plot closest words
    model.plot_closest_words(word='request', plot=False)  # download the plot


if __name__ == "__main__":
    main()
