#!/usr/bin/env python

def get_digits(n):
    return list(map(int, str(n)))

def classify(n):
    return ''.join(sorted(str(n)))

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

def main():
    print(len([x for x in map(chain, list(range(1, 10000000))) if x]))

if __name__ == "__main__":
    main()
