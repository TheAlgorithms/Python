"""

The "Middle Square Method" is a technique for generating
pseudorandom numbers. You start with a 4-digit number,
square it, make sure the result has 8 digits by padding
it with zeros on the left, select the 4 central digits
and treat them as decimal places of a number between 0
and 1. It is a simple approach, but it is important to
note that it does not produce true randomness and may
not be suitable for all applications.]

This is the "Middle Square Method" module.

The example module supplies one function, MiddleSquareMethod(seed, max_sample).make_Random().  For example,

>>> MiddleSquareMethod(seed=3333, max_sample=10).make_Random()
[0.3333, 0.8889, 0.4321, 0.1041, 0.3681, 0.9761, 0.7121, 0.8641, 0.6881, 0.8161]

>>> MiddleSquareMethod(seed=333, max_sample=10).make_Random()
'Invalid value. The seed that have 4 digits'
"""


class MiddleSquareMethod:
    def __init__(self, seed: int, max_sample: int = 10) -> None:
        self.seed = seed
        self.max_sample = max_sample
<<<<<<< HEAD
    def make_Random(self):
=======

    def makeRandom(self):
>>>>>>> 8268f3a409eff031e038854cceda95fd145fb2fc
        seed = self.seed
        max_sample = self.max_sample
        # receive only four digits numbers
        if len(str(seed)) != 4:
            return "Invalid value. The seed that have 4 digits"

        # instancing the list that will receive the results
        rand_values = []

        vl = seed

        # making the calcs and append the pseudorandom value
        flag = True
        while flag:
            if len(rand_values) >= max_sample:
                break
            value = vl / 10000

            if value in rand_values:
                flag = False
                break

            rand_values.append(value)

            vl = vl**2
            flag2 = True
            c = 0

            # making the capture of middle four digits
            while flag2:
                if len(str(vl)[c : len(str(vl))]) != 4:
                    c += 1
                else:
                    vl = int(str(vl)[c : len(str(vl))])
                    flag2 = False

        #   print('tamanho ', len(rand_values))
        return rand_values


if __name__ == "__main__":
    import doctest
<<<<<<< HEAD
    # print(MiddleSquareMethod(seed=3333, max_sample=10).make_Random())
=======

    # print(MiddleSquareMethod(seed=3333, max_sample=10).makeRandom())
>>>>>>> 8268f3a409eff031e038854cceda95fd145fb2fc
    doctest.testmod()
