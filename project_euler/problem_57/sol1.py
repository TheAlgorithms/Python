def solution(fractions_number: int = 1000) -> int:
    '''
    A function that solve project Euler problen 57.
    It calculate-
    how many fractions has a numerator with more digits than the denominator,
    In the first 1000 fractions that their sum is equal to the square of 2.
    You can change the number 1000 by changing the fractions_number variable.
    >>> main()
    153
    >>> main(2000)
    306
    '''
    answer = 0
    count = 1
    numerators = [1, 1]
    denominators = [0, 1]
    while count < fractions_number:
        # the next two line are the algorithm itself
        # finding the next fraction by calculating-
        # numerator equals 2 times the last numerator + 1 time the one before
        numerators.append(2*numerators[count]+numerators[count-1])
        # denominator equals 2 times the last denominator + 1 time the one before
        denominators.append(2*denominators[count] + denominators[count-1])
        # compare the length of the two by turningthem to strings
        if len(str(numerators[-1])) > len(str(denominators[-1])):
            answer += 1
        count += 1
    print(answer)


if __name__ == '__main__':
    solution()
