from random import Random


class Guess:
    def makeEstimate(self, max, min=0, trial=1):
        estimate = min + ((max - min) >> 1)
        print("I guess", estimate)
        answer = input('"lower?", "higher?", or "correct?": ')
        if answer == "lower":
            return self.makeEstimate(estimate, min, trial + 1)
        elif answer == "higher":
            return self.makeEstimate(max, estimate + 1, trial + 1)
        elif answer == "correct":
            return trialgit
        else:
            print("Invalid answer")
            exit()


try:
    N = int(input("Max: "))
except ValueError:
    print("Value must be a number")
    exit()
guesser = Guess()
trial = guesser.makeEstimate(N)
print("Guessed the correct number in", trial, "tries")
