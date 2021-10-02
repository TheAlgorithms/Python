secret_word = "Giraffe"
guess=""
out_of_guess = False
guess_limit = 3
guess_count =0
while guess != secret_word and not out_of_guess:
    if guess_count < guess_limit:
        guess = input("Enter your Guess: ")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("You lost as you lost all your chances")
else:
    print("You won")