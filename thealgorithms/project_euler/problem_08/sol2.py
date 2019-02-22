from functools import reduce

def main():
    number=input().strip()
    print(max([reduce(lambda x,y: int(x)*int(y),number[i:i+13]) for i in range(len(number)-12)]))
    
if __name__ == '__main__':
    main()
