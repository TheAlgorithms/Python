def main():
    def n31(a):# a = initial number
        c = 0
        l = [a]
        while a != 1:
            if a % 2 == 0:#if even divide it by 2
                a = a // 2
            elif a % 2 == 1:#if odd 3n+1
                a = 3*a +1
            c += 1#counter
            l += [a]

        return l , c
    print(n31(43))
    print(n31(98)[0][-1])# = a
    print("It took {0} steps.".format(n31(13)[1]))#optional finish

if __name__ == '__main__':
    main()
