def spin_words(sentence):
    sentences = sentence.split(" ")

    for i in range(len(sentences)):
        if len(sentences[i]) >= 5:
            word = sentences[i]
            newWord = "".join([(word[len(word) - e])  for e in range(1,len(sentences[i]) + 1)])
            sentences.remove(sentences[i])
            sentences.insert(i, newWord)
    
    return " ".join(sentences)

print(spin_words("Hey wollef sroirraw"))