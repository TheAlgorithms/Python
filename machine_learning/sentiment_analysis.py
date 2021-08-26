from textblob import TextBlob

def emotions(text):
    """
    Args:
        text (string): A paragraph of text or a single sentence.   

    Returns:
        [string]: Feelings of the text.

    Test 1: 
        text = "I am happy"
        emotion = "positive"
    Test 2:
        text = "I am sad"
        emotion = "negative"
    Test 3:
        text = "I like to contribute"
        emotion = "neutral"
    """
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "positive"
    elif sentiment < 0:
        return "negative"
    else:
        return "neutral"

def main():
    text = input("Enter the text: ")
    emotion = emotions(text)
    print("The emotion of the text is: " + emotion)
main()

