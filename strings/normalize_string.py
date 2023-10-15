import re

"""
// Normalization enhances data accuracy and integrity, simplifying database navigation

// This program takes the input string and normalize it.
// This program removes whitespaces, numbers, punctuations from the string
"""

# English stop words
stop_words = [
    "a",
    "an",
    "needn",
    "couldn't",
    "very",
    "yours",
    "all",
    "be",
    "should",
    "are",
    "his",
    "with",
    "once",
    "which",
    "been",
    "between",
    "your",
    "only",
    "here",
    "does",
    "why",
    "them",
    "shan't",
    "herself",
    "have",
    "shouldn",
    "doing",
    "out",
    "our",
    "myself",
    "there",
    "most",
    "d",
    "from",
    "hadn't",
    "themselves",
    "that'll",
    "for",
    "she's",
    "can",
    "its",
    "below",
    "the",
    "to",
    "any",
    "it",
    "after",
    "down",
    "into",
    "we",
    "no",
    "other",
    "who",
    "wasn",
    "wasn't",
    "own",
    "did",
    "couldn",
    "few",
    "ain",
    "not",
    "up",
    "so",
    "aren't",
    "didn't",
    "same",
    "it's",
    "more",
    "hadn",
    "haven't",
    "will",
    "needn't",
    "ll",
    "my",
    "just",
    "because",
    "doesn't",
    "s",
    "him",
    "her",
    "theirs",
    "their",
    "too",
    "hers",
    "until",
    "m",
    "over",
    "under",
    "you'll",
    "isn't",
    "what",
    "about",
    "mightn't",
    "yourself",
    "that",
    "me",
    "ours",
    "then",
    "mustn",
    "of",
    "re",
    "don",
    "than",
    "won't",
    "as",
    "hasn't",
    "or",
    "being",
    "in",
    "such",
    "you're",
    "through",
    "won",
    "ourselves",
    "she",
    "nor",
    "himself",
    "do",
    "t",
    "both",
    "again",
    "each",
    "off",
    "at",
    "o",
    "shan",
    "am",
    "this",
    "aren",
    "now",
    "you've",
    "wouldn't",
    "mightn",
    "shouldn't",
    "before",
    "haven",
    "they",
    "when",
    "some",
    "don't",
    "you'd",
    "should've",
    "where",
    "but",
    "yourselves",
    "by",
    "you",
    "and",
    "has",
    "isn",
    "on",
    "didn",
    "against",
    "having",
    "further",
    "how",
    "he",
    "wouldn",
    "weren",
    "was",
    "is",
    "itself",
    "those",
    "mustn't",
    "i",
    "were",
    "doesn",
    "these",
    "above",
    "y",
    "ma",
    "ve",
    "while",
    "whom",
    "had",
    "during",
    "if",
    "weren't",
    "has",
]


def normalize_string(text: str) -> list:
    """
    Function for normalizing the string
    @params : unnormalized string/text
    returns : list of text/words
    """

    # transforming all uppercase to lowercase
    text_lower = text.lower()

    # removing numbers from the string
    remove_numbers = re.sub(r"\d+", "", text_lower)

    # removing the punctuations
    remove_punctuation = re.sub(r"[^\w\s]", "", remove_numbers)

    # removing whitespaces
    remove_whitespace = remove_punctuation.strip()

    # splitting the string into words
    words = remove_whitespace.split()

    # filtering words and removing the stop words
    filtered_words = [word for word in words if word.lower() not in stop_words]
    remove_stop_words = " ".join(filtered_words)

    normalized_text = remove_stop_words.split()

    # returing the list
    return normalized_text


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    text_1 = "        Code is the poetry of logical minds,        "

    text_2 = "where semicolons dance to the rhythm of algorithms, and"

    text_3 = "bugs are the elusive mysteries waiting to "

    text_4 = "be unraveled by the persistent programmer's keen eye."

    normalized_text = normalize_string(text_1 + text_2 + text_3 + text_4)

    print(normalized_text)
