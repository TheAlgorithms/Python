def pig_latin(sentence):
    sentence = sentence.lower()
    length = len(sentence)
    if sentence[0] in "aeiou":
        result = sentence + "way"
    else:
        for i in range(length):
            if sentence[i] in "aeiou":
                break
        result = sentence[i:] + sentence[:i] + "ay"
    return result


statement = input("Enter a string: ")
answer = pig_latin(statement)

print('The PIG LATIN of the entered string is "{}"'.format(answer))
