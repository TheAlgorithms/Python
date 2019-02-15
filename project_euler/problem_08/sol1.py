import sys
def main():
    LargestProduct = -sys.maxsize-1
    number=input().strip()
    for i in range(len(number)-12):
        product=1
        for j in range(13):
            product *= int(number[i+j])
        if product > LargestProduct:
            LargestProduct = product
    print(LargestProduct)


if __name__ == '__main__':
    main()
