def n31(a):# a = initial number
    counter = 0
    path = [a]
    while a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3*a +1
        counter += 1
        path += [a]
    return path , counter

def main():
    num = 43
    path , length = n31(num)
    print("The Collatz sequence of {0} took {1} steps. \nPath: {2}".format(num,length, path))

if __name__ == '__main__':
    main()
