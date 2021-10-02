x = str(input("Enter first word: "))
y = str(input("Enter Second word: "))

if sorted(x) == sorted(y):
    print("Anagrams")
else:
    print("Not Anagrams")
