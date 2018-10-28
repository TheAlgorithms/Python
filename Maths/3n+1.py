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
        print(a)#optional print
    print("It took {0} steps.".format(c))#optional finish
    return l , c
print(n31(43))
