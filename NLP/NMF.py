import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import random

npr = pd.read_csv('sample.csv')

tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')

dtm = tfidf.fit_transform(npr['column'])

#NMF - Non-Negative Matric Factorization

nmf_model = NMF(n_components=7,random_state=42)

# This can take awhile, we're dealing with a large amount of documents!
nmf_model.fit(dtm)

#Displaying Topics

len(tfidf.get_feature_names())

for i in range(10):
    random_word_id = random.randint(0,54776)
    print(tfidf.get_feature_names()[random_word_id])


len(nmf_model.components_)

nmf_model.components_

single_topic = nmf_model.components_[0]

# Top 10 words for this topic:
single_topic.argsort()[-10:]

top_word_indices = single_topic.argsort()[-10:]

for index in top_word_indices:
    print(tfidf.get_feature_names()[index])

for index,topic in enumerate(nmf_model.components_):
    print(f'THE TOP 15 WORDS FOR TOPIC #{index}')
    print([tfidf.get_feature_names()[i] for i in topic.argsort()[-15:]])
    print('\n')
