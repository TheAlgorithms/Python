'''

The "Middle Square Method" is a technique for generating
pseudorandom numbers. You start with a 4-digit number,
square it, make sure the result has 8 digits by padding
it with zeros on the left, select the 4 central digits
and treat them as decimal places of a number between 0
and 1. It is a simple approach, but it is important to
note that it does not produce true randomness and may
not be suitable for all applications.


'''

class MiddleSquareMethod:
    def __init__(self, seed, maxSample = 10):
        self.seed = seed
        self.maxSample = maxSample
    def makeRandom(self):
        seed = self.seed
        maxSample = self.maxSample
        # receive only four digits numbers
        if len(str(seed)) != 4:
            return 'Invalid value. The seed that have 4 algarismes'

        # instancing the list that will receive the results
        randValues = []

        vl = seed

        # making the calcs and append the pseudorandom value
        flag= True
        while flag:

            if len(randValues) >= maxSample:
                break;
            value = vl/10000

            if value in randValues:
                flag = False
                break

            randValues.append(value);

            vl = vl ** 2
            flag2 = True
            c = 0

            # making the capture of middle four digits
            while flag2:
                if len(str(vl)[c:len(str(vl))]) != 4:
                    c+=1
                else:
                    vl = int(str(vl)[c:len(str(vl))])
                    flag2 = False

        #   print('tamanho ', len(randValues))
        return randValues


if __name__ == "__main__":
    mms = MiddleSquareMethod(seed=3333, maxSample=10)
    print(mms.makeRandom())
