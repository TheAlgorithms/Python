from random import Random

class Guess:
    def makeEstimate(self, max, min = 0, trial = 1):
        estimate = min + ((max - min) >> 1)
        print('I guess', estimate)
        answer = input('"lower", "higher", or "right": ')
        if(answer == 'Guess lower'):
            return self.makeEstimate(estimate, min, trial + 1)
        elif(answer == 'Guess higher'):
            return self.makeEstimate(max, estimate + 1, trial + 1)
        elif(answer == 'A right guess'):
            return trial
        else:
            print('Invalid')
            exit()

try:
    N = int(input('Max: '))
except ValueError:
    print('Value must be a number')
    exit()
guesser = Guess()
trial = guesser.makeEstimate(N)
print('Guessed the correct number in', trial, 'tries')