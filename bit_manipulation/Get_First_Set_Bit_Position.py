# Set Bit is "1" 
# We will be using 'and' operator and a mask(1) to solve this problem.

def Get_First_Set_Bit_Pos(x : int) -> int: 
    '''
        EXAMPLE : if input number is 8 Then binary representation of 8 : 00001000
                Position of first set bit is 4.

        TEST CASES : 1.) input : 11
                         output : 1

                EXPLANATION :      11 -> 00001011
                                First set bit comes at first position.

                    2.) input : 24
                        output : 4

                EXPLANATION :      24 -> 00011000
                                First set bit comes at fourth position.

                    3.) input : -4
                        output : ValueError: Integer Value Must Be A Positive Integer

                EXPLANATION : We will find the first set bit only for positive integers
    '''
    # make a count variable which will count the position of the first set bit

    count = 0           # initialise the value with zero

    # make a mask variable which will work as a mask

    mask = 1           # initialise the value with 1 as we will
                    # check the first bit first most

    if x<=0:
        raise ValueError("Integer Value Must Be A Positive Integer")

    # Run a loop till x is greater than zero
    while (x>0) :

        # Increase the count as we are checking the first bit
        count+=1

        # Check if the first bit is '1' or not
        if (x & mask) == 1 :
            # If the first bit is '1' then no need to go further 
            break

        # If the first bit is '0' then remove that bit by using Right Shift 
        # And repeat the same process till you don't find the first '1' .
        x = x>>1

    # Now return the count as this is the correct position of the first set bit.
    return count

num = int(input())
print(Get_First_Set_Bit_Pos(num))