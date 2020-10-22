"""

Word clouds (also known as text clouds or tag clouds) work in a simple way: 
the more a specific word appears in a source of textual data (such as a speech, blog post, or database), 
the bigger and bolder it appears in the word cloud.

"""



from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


stopwords = set(STOPWORDS)
novel=open('gcloud.txt', 'r').read()        #replace gcloud.txt with your text file in same folder

novel_wc=WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stopwords
)

novel_wc.generate(novel)
plt.imshow(novel_wc, interpolation='bilinear')
plt.axis('off')
plt.show()
