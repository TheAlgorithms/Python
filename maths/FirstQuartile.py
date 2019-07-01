import statistics as st

def FirstQuartile(list):
    """
    Returns the first quartile of a list. 
    Ex.: list = [1,2,3,4,5,6] 
    first quartile = 2
    """ 
    quartile1 = st.median(list[:len(list)//2])   
    return quartile1

def main():
    a = [1,3,5,7,9,11]
    print(FirstQuartile(a)) # = 3


if __name__ == '__main__':
    main()

"""
print FirstQuartile
"""
