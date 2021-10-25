"""
This is the Test of SpinWords method.

TheFunction will spin your words

>>> spin_words("Hey wollef sroirraw")
'Hey fellow warriors'
"""

def spin_words(sentence):
    sentences = sentence.split(" ")

    for i in range(len(sentences)):
        if len(sentences[i]) >= 5:
            word = sentences[i]
            new_word = "".join([(word[len(word) - e])  for e in range(1,len(sentences[i]) + 1)])
            sentences.remove(sentences[i])
            sentences.insert(i, new_word)
    result = " ".join(sentences)
    return result


print(spin_words("Hey wollef sroirraw"))



if __name__ == "__main__":
    import doctest
    doctest.testmod()
