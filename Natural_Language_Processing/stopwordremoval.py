# Stopword Removal: Removing common words (e.g., "the," "and") from text.
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

filtered_words = [word for word in words if word.lower() not in stop_words]
print(filtered_words)
