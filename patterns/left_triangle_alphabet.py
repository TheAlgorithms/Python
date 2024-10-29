def left_triangle_pattern(rows):
    # goes to new lines 
    for i in range(rows):
        # print characters in the current line 
        for j in range(i + 1):
            print(chr(j + 65), end="")
        print()

# number of rows to span 
n = 7

# call the function
left_triangle_pattern(n)
