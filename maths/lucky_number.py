def isLuckyNumber(num):
    for i in range(2,num+1):
        if num%i==0: 
            return False
        num -= num//i
    return True
def test():
    assert(isLuckyNumber(5)==False)
    assert(isLuckyNumber(19)==True)
    assert(isLuckyNumber(13)==True)
    assert(isLuckyNumber(200)==False)
    print("All test cases have successfully passed\n")
def user_test():
    num = int(input())
    if isLuckyNumber(num):
        print("Yes, it is a lucky number\n")
    else:
        print("No, it is not a lucky number\n")
if __name__=='__main__':
    test()
    #user_test()