from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import random

npr = pd.read_csv('sample.csv')

#Preprocessing

cv = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
dtm = cv.fit_transform(npr['column'])

#Latent Dirichlet Allocation

LDA = LatentDirichletAllocation(n_components=7,random_state=42)

# This can take awhile, we're dealing with a large amount of documents!
LDA.fit(dtm)

#Showing Stored Words

len_name = len(cv.get_feature_names())

for i in range(10):
    random_word_id = random.randint(0,(len_name-1))
    print(cv.get_feature_names()[random_word_id])

#Showing Top Words per Topic

len(LDA.components_)

print(LDA.components_)

len(LDA.components_[0])

single_topic = LDA.components_[0]

# Returns the indices that would sort this array.
single_topic.argsort()

# Top 10 words for this topic:
single_topic.argsort()[-10:]

top_word_indices = single_topic.argsort()[-10:]

for index in top_word_indices:
    print(cv.get_feature_names()[index])

for index,topic in enumerate(LDA.components_):
    print(f'THE TOP 15 WORDS FOR TOPIC #{index}')
    print([cv.get_feature_names()[i] for i in topic.argsort()[-15:]])
    print('\n')




