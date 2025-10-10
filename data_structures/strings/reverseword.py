def reverse_words(sentence):
    words = sentence.split()
    stack = []
    for word in words:
        stack.append(word)
    reversed_sentence = " ".join(stack[::-1])
    return reversed_sentence


# Example
print(reverse_words("Data Structures in Python"))
