import re   #for use of regular expressions we import re

def extractMax(input):
    numbers = re.findall('\d+',input)   # The function findall() is very usefull and by the expression '\d+' we are checking for all the substrings ending and beginning with a number(int)
    # here "numbers" is a list created at the time of function call which will store the substrings which are numbers(int).

    if not numbers:
        print("No numbers are present in given string!!")
    else:
        print("The largest Number present is :",max(numbers))                                   # max is also a inbuilt function which gives us maximum value out of a list

"""End of Function """

try:
    test_cases = int(input("Enter the number of test cases you want to check for?:  "))
    for test_number in range(test_cases):
        print("This is test case number ",test_number+1)
        sentence = input("Enter the string to check for: ")  # we take string input in a str variable named as sentence
        extractMax(sentence)  # function is called by reference to string sentence we created  (inputed)
except BaseException as e:
    print(e)