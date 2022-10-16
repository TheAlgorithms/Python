def square_asterick(size):
    for i in range(size):
        print("*" * size)

if __name__ == "__main__":
    size = int(input("Enter Length of the square: "))
    square_asterick(size)