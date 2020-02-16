# Finding Square Roots Using Newton's(Newton–Raphson) Method
n = input("Enter a number to find square root: ")
try:
    n = float(n)
except ValueError as err:
    print(err)
    print("Sorry, input should be number, nor ", type(n))
    exit(-1)

epsilon = 0.01
guess = n / 2.0
num_guesses = 0

while abs(guess * guess - n) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess ** 2) - n) / (2 * guess))

print("Number of guesses: ", num_guesses)
print("Square root of ", n, " is ", guess)
