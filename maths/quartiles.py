def median(list):
    """
    Returns the median of a list. 
    Ex.: list = [1,2,3,4,5,6] 
    median = 11.5
    """ 
    media = 0
    for i in list:
        media = media + i
    media = media/len(list)
    return media

def FirstQuartile(list):
    """
    Returns the first quartile of a list. 
    Ex.: list = [1,2,3,4,5,6] 
    first quartile = 2
    """ 
    quartile1 = median(list[:len(list)//2])   
    return quartile1

def SecondQuartile(list):
    """
    Returns the second quartile of a list. 
    Ex.: list = [1,2,3,4,5,6] 
    second quartile = 3.5
    """ 
    quartile2 = median(list)   
    return quartile2

def ThirdQuartile(list):
    """
    Returns the third quartile of a list. 
    Ex.: list = [1,2,3,4,5,6] 
    third quartile = 5
    """ 
    quartile3 = median(list[len(list)//2:])   
    return quartile3

def main():
    a = [1,3,5,7,9,11]
    print(FirstQuartile(a)) # = 3
    print(SecondQuartile(a)) # = 6
    print(ThirdQuartile(a)) # = 9


if __name__ == '__main__':
    main()
