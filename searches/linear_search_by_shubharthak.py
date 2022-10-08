from typing import List

def linear_search(arr: List[int], element: int) -> int:
    '''
    Returns the index of the element if found else return -1

    Params:
    
        arr(List): Sequence Array to search from
        element(int): Element to be search in the arr
    
    Returns:
       Index if found else -1     
    '''
    for i,v in enumerate(arr):
        if v == element:
            return i
    return -1 
def check_answer(ans: int, element: int) -> None:
    '''
    Print the answer

    Params:
        ans(int): index of the element to be searched
        element(int): element to be searched
    '''
    if ans != -1:
        print(f"Element {element} found at index {ans}")
    else:
        print(f"Element {element} is not present in the given List")
        
if __name__ == "__main__":
    arr = list(map(int,input("Please enter the elements seperated by space: ").split()))
    element = int(input("Please enter the element you want to search: "))
    check_answer(linear_search(arr, element), element)
