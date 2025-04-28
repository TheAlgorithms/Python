"""
A pure Python implementation of Functions

A Function in python is a reusable piece of code that takes N parameters and can be called as many times as we want.
Functions are important because:
    1) They make our code clean
    2) They make our code small
    3) It improves performance
For example : A function to add two numbers a and b will have two parameters a and b

"""


def addition(a, b):
    """
    A function in python is created with a keyword 'def' in all small , followed with the name of the function for example in here addition
    and in the brackets we pass on the parameter's value the function will work upon

    """
    return a + b

    """
    The return keyword as the name suggests returns the result of the function in here it returns the value of addition of a and b

    """


print(addition(4, 5))

"""
To call a function you type in the function's name and pass on the values that you want your function to pass
For example : Result for this case will be 9 as  4 + 5 here automatically the function assumes a = 4 and b = 5
another way to call a function is to specify the values for example print(addition(a=4 ,b= 5))

"""


"""

Another function for example can be to print every item in a list
For example

"""


def each_item_in_list(list):
    for item in list:
        print(item)
        """
        Here the function takes takes the parameter 'list' and this function when called upon will print every item of the list
        """


each_item_in_list([1, 2, 3, 4, 5, 6])

"""
Upon calling the function the result will be
1
2
3
4
5
6
"""
