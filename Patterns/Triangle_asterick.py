def triangle_asterick(size):

    for i in range(1,size+1):
        print('*' * i)

if __name__ == "__main__":
    size = int(input("Enter the size of height of triangle: "))
    triangle_asterick(size)
