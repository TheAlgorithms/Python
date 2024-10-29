#define function 
def hollow_left_triangle(rows):

    #change rows 
    for i in range(1, rows+1):
        counter = 0
        for j in range(i):
            # print characters at the end and start
            if j == 0 or j == i-1:
                print(chr(65 + counter), end='')
                counter += 1
            else:
                # print spaces in between
                if i != rows:
                    print(' ', end='')
                # print characters in the last row
                else:
                    print(chr(65 + counter), end='')
                    counter += 1
        print()

#rows to be spanned 
n = 7

#call the function 
hollow_left_triangle(n)
