def word_count(txt):
    x = txt.split()
    return len(x)

def char_count(txt):
    return len(txt)

txt = input("Input your text to count all word\n>>> ")
print(word_count(txt), "word(s) ", char_count(txt), "character(s)")
