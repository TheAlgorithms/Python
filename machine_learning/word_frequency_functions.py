import string
import math

def term_frequency(term, document):
    """
    Return the number of times a term occurs within a given document.
    
    :param term: The term to search for.
    :param document: The document to search within.
    :return: An integer representing the number of times the term is found within the document.
    """
    # Remove punctuation and split the document into words
    document = document.translate(str.maketrans('', '', string.punctuation)).lower()
    words = document.split()
    
    return words.count(term.lower())

def document_frequency(term, corpus):
    """
    Calculate the number of documents in a corpus that contain a given term.
    
    :param term: The term to search for.
    :param corpus: A collection of documents separated by newlines.
    :return: A tuple containing the number of documents containing the term and the total number of documents in the corpus.
    """
    # Remove punctuation and split the corpus into documents
    corpus = corpus.lower().translate(str.maketrans('', '', string.punctuation))
    documents = corpus.split('\n')
    
    term = term.lower()
    doc_count = sum(1 for doc in documents if term in doc)
    
    return doc_count, len(documents)

def inverse_document_frequency(df, n, smoothing=False):
    """
    Return a float denoting the importance of a word.
    
    :param df: The Document Frequency.
    :param n: The total number of documents in the corpus.
    :param smoothing: If True, apply smoothing to IDF.
    :return: The IDF value.
    """
    if smoothing:
        return 1.0 + math.log10((n + 1) / (df + 1))
    
    if df == 0:
        raise ZeroDivisionError("DF must be greater than 0.")
    
    return math.log10(n / df)

def tf_idf(tf, idf):
    """
    Combine the term frequency and inverse document frequency functions to calculate the originality of a term.
    
    :param tf: The Term Frequency.
    :param idf: The Inverse Document Frequency.
    :return: The TF-IDF value.
    """
    return tf * idf

def calculate_tf_idf(term, document, corpus):
    """
    Calculate the TF-IDF score for a term within a document across a corpus.
    
    :param term: The term to calculate TF-IDF for.
    :param document: The document in which to calculate the TF-IDF.
    :param corpus: A collection of documents separated by newlines.
    :return: The TF-IDF score for the term within the document.
    """
    tf = term_frequency(term, document)
    df, n = document_frequency(term, corpus)
    idf = inverse_document_frequency(df, n)
    return tf_idf(tf, idf) 
