# Tokenization 

import nltk
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.corpus import stopwords
import re
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer

nltk.download()
nltk.download('punkt')

paragraph="""I have three visions for India. In 3000 years of our history people from all over the world have come and invaded us, captured our lands, conquered our minds. From Alexander onwards the Greeks, the Turks, the Moguls, the Portuguese, the British, the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture and their history and tried to enforce our way of life on them. Why? Because we respect the freedom of others. That is why my FIRST VISION is that of FREEDOM. I believe that India got its first vision of this in 1857, when we started the war of Independence. It is this freedom that we must protect and nurture and build on. If we are not free, no one will respect us.We have 10 percent growth rate in most areas. Our poverty levels are falling. Our achievements are being globally recognised today. Yet we lack the self-confidence to see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect? MY SECOND VISION for India is DEVELOPMENT. For fifty years we have been a developing nation. It is time we see ourselves as a developed nation. We are among top five nations in the world in terms of GDP.I have a THIRD VISION. India must stand up to the world. Because I believe that unless India stands up to the world, no one will respect us. Only strength respects strength. We must be strong not only as a military power but also as an economic power. Both must go hand-in-hand. My good fortune was to have worked with three great minds. Dr.Vikram Sarabhai, of the Dept. of Space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material. I was lucky to have worked with all three of them closely and consider this the great opportunity of my life."""

## Tokenize Sentences
sentences=nltk.sent_tokenize(paragraph)

## Tokenize Words
words=nltk.word_tokenize(paragraph)

# Stemming
sentences=nltk.sent_tokenize(paragraph)
stemmer=PorterStemmer()
for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words=[stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words)

### Note: Problem with stemming is that some of the words that are created may not have meaning. For example: histori, lucki, etc. in above example.


# Lemmartization
sentences=nltk.sent_tokenize(paragraph)
lemmatizer=WordNetLemmatizer()
for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words=[lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words)

### Note: Problem with lemmatization is that it takes more time as it takes words in such a manner that it will have meaning. For example: history, lucky, etc. in above example.


# Bag Of Words

"""
sent1: He is a good boy.	|stop words		sent1: good boy
sent2: He is a good girl.	|==================>	sent2: good girl
sent3: Boy and girl are good. 	|lowering sentences	sent3: boy  girl good

					  f1	   f2	   f3
				________________________________________	
Words	|Frequency|		|	| good	|  boy	|  girl	|  o/p	|
________|_________|  Vectors	|_______|_______|_______|_______|_______|
good	|3	  |============>|sent1	|   1	|   1	|   0	|	|
boy	|2	  |   BOW	|sent2	|   1	|   0	|   1	|	|	
girl	|2 	  |		|sent3	|   1	|   1	|   1	|	|
				|_______|_______|_______|_______|_______|

o/p => Independent Feature
f1,f2 and f3 => Dependent Feature

Disadvantage:
=>In sent1 the frequencies of good and boy are 1 which means both are given same weightage but here the more weightage must be given to the word good.
This problem is solved by TF-IDF(Term Frequency and Inverse Document Frequency).

Application:
=> If there is sentiment analysis then we can go ahead with BOW but if the dataset is big then it is recommended to use WordVec.
"""
## Cleaning Text
ps=PorterStemmer()
wordnet=WordNetLemmatizer()
"""
For Stemming
"""
sentences=nltk.sent_tokenize(paragraph)
corpus=[]
for i in range(len(sentences)):
    review=re.sub('[^a-zA-Z]',' ',sentences[i])
    review=review.lower()
    review=review.split()
    review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)
"""
For Lemmatization
"""
sentences=nltk.sent_tokenize(paragraph)
corpus=[]
for i in range(len(sentences)):
    review=re.sub('[^a-zA-Z]',' ',sentences[i])
    review=review.lower()
    review=review.split()
    review=[wordnet.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)

## Creating the Bag of Words
cv=CountVectorizer()
x=cv.fit_transform(corpus).toarray()

# TF-IDF

"""
Formulas:

Term Frequency(TF)= Number of repeat words in sentence/ Number of words in sentence
Inverse Document Frequency(IDF) = log( Number of sentences/ Number of sentences containing words)
Finally, TF*IDF

From previous example in Bag Of Words
sent1-> good	boy
sent2-> good	girl
sent3-> boy	girl	good
				_______________TF_______________    	_______IDF_______	________________________________________________________
|Words	|Frequency|		|	| sent1	| sent2	| sent3	|  	| Words	|  IDF	 |	|	|  f1	|     f2	|     f3	|  o/p	|
|_______|_________|   Vectors	|_______|_______|_______|_______|	|_______|________|	|_______|_______|_______________|_______________|_______|	
|	|	  |============>| good	|  1/2	|  1/2	|  1/3	|	| good	|log(3/3)|   =	|	| good	|     boy	|    girl	|	|
| good	|   3	  |    TF-IDF	| boy	|  1/2 	|   0	|  1/3 	|   *	| boy	|log(3/2)|	| sent1	|   0	| (1/2)*log(3/2)|      0	|	|
| boy	|   2	  |		| girl	|   0	|  1/2	|  1/3	|	| girl	|log(3/2)|	| sent2	|   0	|      0	| (1/2)*log(3/2)|	|
| girl	|   2	  |		|_______|_______|_______|_______|	|_______|________|	|_sent3_|___0___|_(1/3)*log(3/2)|_(1/3)*log(3/2)|_______|
"""
cv=TfidfVectorizer()
x=cv.fit_transform(corpus).toarray() 
