def bubbleSort( theSeq ):
    n = len( theSeq )

    for i in range( n - 1 ) :
        flag = 0

        for j in range(n - 1) :
            
            if theSeq[j] > theSeq[j + 1] : 
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                flag = 1

        if flag == 0:
            break

    return theSeq

el = [21,6,9,33,3] 

result = bubbleSort(el)

print (result)



"""
HERE,

1. Defines a function bubbleSort that accepts a parameter theSeq. The code does not output anything.
2. Gets the length of the array and assigns the value to a variable n. The code does not output anything
3. Starts a for loop that runs the bubble sort algorithm (n – 1) times. This is the outer loop. The code does not output anything
4. Defines a flag variable that will be used to determine if a swap has occurred or not. This is for optimization purposes. The code does not output anything
5. Starts the inner loop that compares all the values in the list from the first to the last one. The code does not output anything.
6. Uses the if statement to check if the value on the left-hand side is greater than the one on the immediate right side. The code does not output anything.
7. Assigns the value of theSeq[j] to a temporal variable tmp if the condition evaluates to true. The code does not output anything
8. The value of theSeq[j + 1] is assigned to the position of theSeq[j]. The code does not output anything
9. The value of the variable tmp is assigned to position theSeq[j + 1]. The code does not output anything
10. The flag variable is assigned the value 1 to indicate that a swap has taken place. The code does not output anything
11. Uses an if statement to check if the value of the variable flag is 0. The code does not output anything
12. If the value is 0, then we call the break statement that steps out of the inner loop.
13. Returns the value of theSeq after it has been sorted. The code outputs the sorted list.
14. Defines a variable el that contains a list of random numbers. The code does not output anything.
15. Assigns the value of the function bubbleSort to a variable result.
16. Prints the value of the variable result.
"""
