# # **Importing datasets**


# Read text from the uploaded file
with open('./data/brown.train.txt', 'r') as file:
    train_text = file.read()

with open('./data/brown.test.txt', 'r') as file:
    test_text = file.read()

with open('./data/brown.dev.txt', 'r') as file:
    dev_text = file.read()

print("Text from the file(s):")

print(train_text[:500], " ...\n\n")
print(test_text[:500], " ...\n\n")
print(dev_text[:500], " ...\n\n")

# # **Text Cleaning**
# 
# - In this section, the input corpus is cleaned and **all non-alphanumeric** symbols are dropped
# 
# - `<start>` and `<stop>` tags are added at the *start* and *end* of every sentence


import math
import re as RegularExpression
from collections import Counter


def clean_text(corpus):
    # Convert to lowercase and remove punctuation
    corpus = corpus.lower()
    corpus = corpus.replace("'", " ").replace("-", " ")
    
    cleaned_corpus = RegularExpression.sub(r'[^a-zA-Z0-9\s\n]', ' ', corpus)

    return cleaned_corpus


def add_start_stop_tags (text):
    sentences = text.split("\n")

    sentences = ['<start> ' + sentence.strip() + ' <stop>' 
                    for sentence in sentences if sentence.strip() != ""]
    
    return "\n".join(sentences)


def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Loading training, dev and test corpus

train_corpus = read_text_from_file('./data/brown.train.txt') 
dev_corpus = read_text_from_file('./data/brown.dev.txt') 
test_corpus = read_text_from_file('./data/brown.test.txt') 

TRAIN_TEXT = add_start_stop_tags(clean_text(train_corpus))
DEV_TEXT = add_start_stop_tags(clean_text(dev_corpus))
TEST_TEXT = add_start_stop_tags(clean_text(test_corpus))

print ("Train Text: ", TRAIN_TEXT[:1000], " ...\n\n")
print ("Dev Text:   ", DEV_TEXT[:1000], " ...\n\n")
print ("Test Text:  ", TEST_TEXT[:1000], " ...\n\n")

# # **Vocabulary Generation**
# 
# - This is done to handle **out of vocabulary words** in test data. 
# - All words not in vocabulary are replaced by `<unk>` to train *unk_probabilities* and then used for test data.


def generate_vocabulary (text, threshold = 0):
    text_words = text.split()

    word_counts = Counter (text_words)

    vocabulary = {word for word, count in word_counts.items() if count > threshold}
    # out_of_vocabulary = [word for word, count in word_counts.items() if count <= threshold]
    
    return vocabulary


VOCAB = generate_vocabulary(TRAIN_TEXT, threshold=1)

VOCAB_SIZE = len(VOCAB)

print (VOCAB)
print (VOCAB_SIZE)


def add_unks(text):
    text_sentences = text.split("\n")

    # print (text[:500], "\n\n\n")

    for i in range(len(text_sentences)):
        words = text_sentences[i].split()
        words = [word if word in VOCAB else '<UNK>' for word in words]

        # print (words)

        text_sentences[i] = ' '.join(words)
        # print (">> ", sentence)

    text = '\n'.join(text_sentences)
    # print (text[:500], "\n\n\n")
    return text

# Adding <UNK> to Training & Test Data

TRAIN_TEXT = add_unks(text = TRAIN_TEXT)
TEST_TEXT = add_unks(text = TEST_TEXT)

print (TRAIN_TEXT[:1000], " ...\n\n")
print (TEST_TEXT[:1000], " ....\n\n")


# count of <UNK> in Training Data and Test Data

print (TRAIN_TEXT.count('<UNK>'))
print (TEST_TEXT.count('<UNK>'))

# # **Model Training**
# 
# All probabilites are computed as **log_probabilities** to avoid underflow and speed up computation.


def train_ngram_model (N):
    words = TRAIN_TEXT.split()

    # building n-grams 
    ngrams = [tuple(words[i:i+N]) for i in range (len(words)-N+1)]

    # storing frequencies of n-grams
    ngram_counts = Counter (ngrams)

    # total n-grams (not unique)
    total_ngrams = len(ngrams)

    log_probabilities = {ngram : math.log(count / total_ngrams) 
                            for ngram, count in ngram_counts.items()}

    return log_probabilities


# Training Unigram, Bigram and Trigram Models

UNIGRAM = train_ngram_model(1)
BIGRAM = train_ngram_model(2)
TRIGRAM = train_ngram_model(3)

print (list(UNIGRAM.items())[:20], "\n")
print (list(BIGRAM.items())[:20], "\n")
print (list(TRIGRAM.items())[:20], "\n")

# # **Model Evaluation**


def calculate_probability (sentence, N):
    # Model cannot predict the sentence
    if len(sentence) < N:
        return float('-inf')

    # print (sentence)

    model = UNIGRAM if N == 1 else (BIGRAM if N == 2 else TRIGRAM)

    sentence_words = sentence.split()
    sentence_ngrams = [tuple(sentence_words[i:i+N]) for i in range (len(sentence_words) - N+1)]

    sentence_probability = 0.00
    err_ngram = ""

    for s_ngram in sentence_ngrams:
        word_probability = model.get(s_ngram, float('-inf'))
        if word_probability == float('-inf'):
            return float('-inf'), s_ngram

        sentence_probability += word_probability

    return sentence_probability, ""
        


def calculate_perplexity (probability, word_n):
    return math.exp(-probability / word_n)

# ### **Unigrams**


# Model Testing - Unigrams

test_sentences = TEST_TEXT.split("\n")

perplexities = []
possible_sentences = 0

for t_sentence in test_sentences:
    probability, err_ngram = calculate_probability(t_sentence, 1)

    if probability == float('-inf'):
        # print ("Error NGram: ", err_ngram)
        continue

    perplexity = calculate_perplexity (probability, len(t_sentence))

    perplexities.append(perplexity)
    possible_sentences += 1

try:
    avg_perplexity = sum(perplexities) / len(perplexities)
    print ("Average Perplexity: ", avg_perplexity)
except:
    print ("Average Perplexity: UNDEFINED")

print ("Possible Sentences: ", possible_sentences)
print ("Total Sentences   : ", len(test_sentences))

# ### **Bigrams**


# Model Testing - Bigrams

test_sentences = TEST_TEXT.split("\n")

perplexities = []
possible_sentences = 0

for t_sentence in test_sentences:
    probability, err_ngram = calculate_probability(t_sentence, 2)

    if probability == float('-inf'):
        # print ("Error NGram: ", err_ngram)
        continue

    perplexity = calculate_perplexity (probability, len(t_sentence))

    perplexities.append(perplexity)
    possible_sentences += 1

try:
    avg_perplexity = sum(perplexities) / len(perplexities)
    print ("Average Perplexity: ", avg_perplexity)
except:
    print ("Average Perplexity: UNDEFINED")

print ("Possible Sentences: ", possible_sentences)
print ("Total Sentences   : ", len(test_sentences))

# ### **Trigrams**


# Model Testing - Bigrams

test_sentences = TEST_TEXT.split("\n")

perplexities = []
possible_sentences = 0

for t_sentence in test_sentences:
    probability, err_ngram = calculate_probability(t_sentence, 3)

    if probability == float('-inf'):
        # print ("Error NGram: ", err_ngram)
        continue

    perplexity = calculate_perplexity (probability, len(t_sentence))

    perplexities.append(perplexity)
    possible_sentences += 1

try:
    avg_perplexity = sum(perplexities) / len(perplexities)
    print ("Average Perplexity: ", avg_perplexity)
except:
    print ("Average Perplexity: UNDEFINED")

print ("Possible Sentences: ", possible_sentences)
print ("Total Sentences   : ", len(test_sentences))

# # **Results**
# 
# ## Choosing Vocabulary from `brown.dev.txt`:
# ### **Unigram**
# ```
# Average Perplexity:  3.0363977961227344
# Possible Sentences:  5550
# Total Sentences   :  5718
# ```
# 
# ### **Bigram**
# ```
# Average Perplexity:  4.741656694984936
# Possible Sentences:  718
# Total Sentences   :  5718
# ```
# 
# ### **Trigram**
# ```
# Average Perplexity:  3.2690758284554344
# Possible Sentences:  230
# Total Sentences   :  5718
# ```
# 
# ## Choosing Vocabulary from `brown.train.txt`:
# ### **Unigram**
# ```
# Average Perplexity:  3.199074872193928
# Possible Sentences:  5718
# Total Sentences   :  5718
# ```
# 
# ### **Bigram**
# ```
# Average Perplexity:  4.90519939698445
# Possible Sentences:  533
# Total Sentences   :  5718
# ```
# 
# ### **Trigram**
# ```
# Average Perplexity:  3.271041087203471
# Possible Sentences:  180
# Total Sentences   :  5718
# ```
