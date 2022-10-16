def triangle_Numbers(size):
    for i in range(1,size + 1):
        # Using List comprehension.
        # Benefits: List comprehension is faster than for loops.
        # So it is beneficial in the case of time complexity.
        [print(num,end=" ") for num in range(1,i + 1)]
        print()

if __name__ == "__main__":
    size = int(input("Enter Size of Numbered Triangle: "))
    triangle_Numbers(size)
