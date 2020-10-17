str = input()

vowels = []

for letter in str:
    if letter in ["a", "e", "i","o","u"]:
        vowels.append(letter)

new_str = ""
for letter in str:
    if letter in ["a", "e", "i","o","u"]:
        lett = vowels.pop()
        new_str += lett
    else:
        new_str += letter
print(new_str)
        
