
# find out the Armstrong number

def find_amrstrong_num():
    # take input from the user
    num = int(input("Enter a number: "))
    # initialize sum
    sum = 0
    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
            sum += digit ** 3
                temp //= 10
            # display the result
if num == sum:
    print(num,"It is an Armstrong number")
    else:
        print(num,"It is not an Armstrong number")


def main():
    find_amrstrong_num()

if __name__ == '__main__':
    main()
