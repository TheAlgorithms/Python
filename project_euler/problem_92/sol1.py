"""
Problem: A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

Example:
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

#!/usr/bin/env python


def get_digits(n):
    return list(map(int, str(n)))


def classify(n):
    return "".join(sorted(str(n)))


terminators = {}


def chain(start):
    n = start
    prev = None
    sequence = []
    while prev != 1 and prev != 89:
        key = classify(n)
        sequence.append(key)
        try:
            if terminators[key]:
                for number in sequence:
                    terminators[number] = True
                return True
            elif terminators[key] == False:
                for number in sequence:
                    terminators[number] = False
                return False
        except Exception as e:
            pass

        prev = n
        n = sum(d ** 2 for d in get_digits(n))

    if prev == 89:
        for number in sequence:
            terminators[number] = True
        return True
    else:
        for number in sequence:
            terminators[number] = False
        return False


def main(starting_range: int, ending_range: int) -> int:
    """
    >>> main(1,10000000)
    8581146
    >>> main(2,100)
    80
    >>> main(-2,9)
    Traceback (most recent call last):
      File "sol1.py", line 65, in <module>
        print(main(-2,1000))
      File "sol1.py", line 62, in main
        return len([x for x in map(chain, range(starting_range, ending_range)) if x])
      File "sol1.py", line 62, in <listcomp>
        return len([x for x in map(chain, range(starting_range, ending_range)) if x])
      File "sol1.py", line 43, in chain
        n = sum(d ** 2 for d in get_digits(n))
      File "sol1.py", line 16, in get_digits
        return list(map(int, str(n)))
    ValueError: invalid literal for int() with base 10: '-'
    """
    return len([x for x in map(chain, range(starting_range, ending_range)) if x])


if __name__ == "__main__":
    print(main(1, 10000000))
