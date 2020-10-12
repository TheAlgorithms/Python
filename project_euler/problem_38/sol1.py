# Problem 38- Pandigital Multiples
# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def pan_digital_check(n):
    """
    Checks if a number(entered as a string here) is pandigital
    """
    flag = True
    if len(n) == 9:     #digits from 1 to 9
        for i in range(1, 10):
            if str(i) not in n:     #if any digit is not present, the string is not pandigital
                flag = False
                break
    else:
        flag = False
    return flag

def solution():
    #Since a pandigital is 9 characters long, if it were to be made after concatenation of successive multiples of a number, that number should
    #be less than 10000

    for n in range(10000, 8, -1):
        pand_creator = str(n)
        #print(pand_creator)
        for o in range(2, 6):       #2- because the first multiple is pand_creator itself and 6- because as given in the statement, the smallest number, 9, to form a pandigital 
            pand_creator += str(n * o)                        #requires 5 multiple concatenation. All numbers after it must require lesser multiple concatenations.
            #now check if pandigital is formed
            if(pan_digital_check(pand_creator)):
                #Add a print statement here to see all the possible pandigitals formed by multiple concatenation
                return pand_creator         #This will be the largest pandigital since we started from the largest possible pandigital creator

if __name__ == "__main__":
    print(f"The largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1 is: ", solution())       #Gives 932718654