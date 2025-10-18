import random as r

print("Lets create a password for you :)")
print()
alphabets = [
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114,
    115,
    116,
    117,
    118,
    119,
    120,
    121,
    122,
    65,
    66,
    67,
    68,
    69,
    70,
    71,
    72,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["@", "#", "!", "$", "%", "^", "&", "*", "(", ")", "~"]
print("how many alphabets you want in your password ? ")
a = int(input())
print("how many numbers you want in your password? ")
n = int(input())
print("how many symbols you want in your password? ")
s = int(input())
password = []
for i in range(0, a):
    password.append(chr(r.choice(alphabets)))
for j in range(0, n):
    password.append(r.choice(nums))
for k in range(0, s):
    password.append(r.choice(symbols))
r.shuffle(password)
print("your required password is ", "".join(password))
