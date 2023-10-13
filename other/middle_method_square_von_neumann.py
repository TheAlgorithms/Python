"""
Test cases

>>> MiddleSquareMethod(seed=3333, max_sample=10).make_random()
[0.3333, 0.8889, 0.4321, 0.1041, 0.3681, 0.9761, 0.7121, 0.8641, 0.6881, 0.8161]

>>> MiddleSquareMethod(seed=333, max_sample=10).make_random()
'Invalid value. The seed that have 4 digits'
"""

# The "Middle Square Method" is a technique for generating
# pseudorandom numbers.
# Link: https://en.wikipedia.org/wiki/Pseudorandom_number_generator


class MiddleSquareMethod:
    def __init__(self, seed: int, max_sample: int = 10) -> None:
        self.seed = seed
        self.max_sample = max_sample

    def make_random(self) -> list[any]:
        seed = self.seed
        max_sample = self.max_sample
        # receive only four digits numbers
        if len(str(seed)) != 4:
            return "Invalid value. The seed that have 4 digits"

        # instancing the list that will receive the results
        rand_values: list = []

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

    # print(MiddleSquareMethod(seed=3333, max_sample=10).make_random())
    doctest.testmod()
