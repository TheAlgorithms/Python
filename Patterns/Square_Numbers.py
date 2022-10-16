def numbered_square(size):
    for i in range(1,size + 1):
        [print(num,end = " ") for num in range(1,i + 1)]
        print()

if __name__ == "__main__":
    size = int(input("Enter Length of the square: "))
    numbered_square(size)