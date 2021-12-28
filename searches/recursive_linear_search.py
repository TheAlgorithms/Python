"""
This is a python implementation of recursive_linear_search algorithm

For doctests run following command:
python3 -m doctest -v recursive_linear_search.py

For manual testing run:
python3 recursive_linear_search.py

"""
def recursive_linear_search(array:list,target:int,index:int =0)-> int:
    """
    This a python implementation of recursive linear search algorithm. Where we are applying linear search algorithm with recursion.

    Parameters : 1>array : First parameter to the function is the array(searching space) (accepts both sorted and unsorted array).
                 
                 2>target : Second parameter to the function is target which is the element to be search in the array(argument 1).
                
                 3>index : Third parameter is default parameater to the function. Default value of it is 0 it is a starting position of our seraching.
    
    Output: This function will return the index (starting form zero) of the target(2nd argument) if found in the giving array (1st argument) else will return -1

    Exceptions : TypeError : This exception will be raised when the 1st argument(array) will be any other type rather than list,tuple or string.
                 
                 ValueError: This exception will be raised when the 1st argument of type string and 2nd argument(target) will be of type non-string.As you cannot search non-str element in str.
    Examples :
    >>>recursive_linear_search([1,2,3,4,5],5)
    4
    >>>recursive_linear_search([5,4,3,2,1],3)
    2
    >>recursive_linear_search([-1,4,3,-10,8],-1)
    0         
    """
    if type(array) not in (list,tuple,str) : raise TypeError("Invalid input(argument 1) only list,tuple,str allowed")

    if type(array)==str and type(target)!=str : raise ValueError("Invalid input(argument 2) cannot search non-str in str")
    
    if index==len(array): return -1

    if array[index]==target: return index

    return recursive_linear_search(array,target,index+1)

if __name__ == "__main__":
    array=list(map(int,input("Enter numbers separated by space:\n").strip().split(" ")))
    target=int(input("Enter the element you want to search in the array\n"))
    ans=recursive_linear_search(array,target)
    if ans==-1:
        print(f"{target} was not found in the given array")
    else:
        print(f"{target} was found on the {ans} index in the array {array}")
