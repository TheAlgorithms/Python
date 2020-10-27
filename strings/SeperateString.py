def seperate(text, provided_list=None):
    """ This seperates each character of a string and sorts them into a list
    """
    if provided_list is None:
        seperated_text = []
    
    else:
        seperated_text = provided_list

    for x in text:
        seperated_text.append(x)
    
    return seperated_text

if '__main__' == __name__:
    test_text = "hello"
    test_list = ['t', 'e', 's', 't', ' ']
    print(seperate(test_text, test_list))
    print(seperate(test_text))
