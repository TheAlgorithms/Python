'''
This is to implement the list functionality without using the list function.
We've created a iter object as an intermediate and appended the elements to an empty list.
We finally returned it.You can test it with your inputs to..

Note:Python's list method takes only one argument.But our method designed using Python takes variable number of argumnets
and return them collectively as a list. our code can handle higher order functions like map & filter also

Reviews are appriciated :)

Author: Rohit Babu Gaddeti

I'm a newbie ^_^
'''

def custom_list_method(*object):
    k=str(object)
    iter_obj = iter(object)   #converting to iter object
    result = []
    try:
        for element in iter_obj:
            if type(element).__name__ == 'map' or type(element).__name__ == 'filter' or \
                    (type(element).__name__ == 'str' and len(element) == 1):
                for char in element:
                    result.append(char)
            else:
                result.append(element)
    except Exception:
        pass

    return result