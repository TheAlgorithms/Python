def emojiconverotr(words) :
    message = words.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "☹"

    }
    output = ""
    for word in message:
        output += emojis.get(word, word) + " "
    print(output)


words = input("> ")
emojiconverotr(words)
