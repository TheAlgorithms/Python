def absVal(num):
    """
    Function to fins absolute value of numbers.
    >>>absVal(-5)
    5
    >>>absVal(0)
    0
    """
    if num < 0:
        return -num
    else:
        return num

def main():
    print(absVal(-34)) # = 34

if __name__ == '__main__':
    main()
