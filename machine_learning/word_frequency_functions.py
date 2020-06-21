import string
from math import log10

""" Here I've implemented several word frequency functions
    that are commonly used in information retrieval: Term Frequency,
    Document Frequency, and TF-IDF (Term-Frequency*Inverse-Document-Frequency)
    are included.

    Term Frequency is a statistical function that
    returns a number representing how frequently
    an expression occurs in a document.This
    indicates how significant a particular term is in
    a given document.

    Document Frequency is a statistical function that returns
    an integer representing
    the number of documents in a corpus that a term occurs in
    (where the max integer returned would be the number of
    documents in the corpus).

    Inverse Document Frequency is mathematically written as
    log10(N/df), where N is the number of documents in your
    corpus and df is the Document Frequency. If df is 0, a
    ZeroDivisionError will be thrown.

    Term-Frequency*Inverse-Document-Frequency is a measure
    of the originality of a term. It is mathematically written
    as tf*log10(N/df). It compares the number of times
    a term appears in a document with the number of documents
    the term appears in. If df is 0, a ZeroDivisionError will be thrown.
"""


def term_frequency(term, document):
    """
    A function that returns the number of times a term occurs within
    a given document.
    @params: term, the term to search a document for, and document,
            the document to search within
    @returns: an integer representing the number of times a term is
            found within the document

    @examples:
    >>> document = "To be, or not to be"
    >>> term = "to"
    2

    >>> document = "Natural Language Processing is a subfield of Artificial Intelligence
                    concerned with interactions between computers and human languages"
    >>> term = "NLP"
    0
    """
    # strip all punctuation and newlines and replace it with ''
    document_without_punctuation = document.translate(
        str.maketrans("", "", string.punctuation)
    ).replace("\n", "")
    tokenize_document = document_without_punctuation.split(" ")  # word tokenization
    term_frequency = len(
        [word for word in tokenize_document if word.lower() == term.lower()]
    )
    return term_frequency


def document_frequency(term, corpus):
    """
    A function that calculates the number of documents in a corpus that contain a
    given term
    @params : term, the term to search each document for, and corpus, a collection of
             documents. Each document should be separated by a newline.
    @returns : the number of documents in the corpus that contain the term you are
               searching for and the number of documents in the corpus
    @examples :
    >>> corpus =
                "This is the first document in the corpus.\n
                ThIs is the second document in the corpus.\n
                THIS is the third document in the corpus."
    >>> term = "first"
    1
    >>> term = "document"
    3
    >>> term = "this"
    3
    """
    corpus_without_punctuation = corpus.translate(
        str.maketrans("", "", string.punctuation)
    )  # strip all punctuation and replace it with ''
    documents = corpus_without_punctuation.split("\n")
    lowercase_documents = [document.lower() for document in documents]
    document_frequency = len(
        [document for document in lowercase_documents if term.lower() in document]
    )  # number of documents that contain the term
    return document_frequency, len(documents)


def inverse_document_frequency(df, N):
    """
    A function that returns an integer denoting the importance
    of a word. This measure of importance is
    calculated by log10(N/df), where N is the
    number of documents and df is
    the Document Frequency.
    @params : df, the Document Frequency, and corpus,
    a collection of documents separated
             by a newline.
    @returns : log10(N/df)
    @examples :
    >>> df = 1
    >>> corpus =
                "This is the first document in the corpus.\n
                ThIs is the second document in the corpus.\n
                THIS is the third document in the corpus."
    log10(3/1) = .477
    >>> df = 3
    log10(3/3) = log10(1) = 0
    >>> df = 0
    log10(3/0) -> throws ZeroDivisionError
    """
    try:
        idf = round(log10(N / df), 3)
        return idf
    except ZeroDivisionError:
        print("The term you searched for is not in the corpus.")


def tf_idf(tf, idf):
    """
    A function that combines the term frequency
    and inverse document frequency functions to
    calculate the originality of a term. This
    'originality' is calculated by multiplying
    the term frequency and the inverse document
    frequency : tf-idf = TF * IDF
    @params : tf, the term frequency, and idf, the inverse document
    frequency
    """
    return round(tf * idf, 3)
