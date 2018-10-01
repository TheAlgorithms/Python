# Pancake sort algorithm 
# Only can reverse array from 0 to i

def pancakesort(arr):
    cur = len(arr)
    while cur > 1:
        # Find the maximum number in arr
        mi = arr.index(max(arr[0:cur]))
        # Reverse from 0 to mi 
        arr = arr[mi::-1] + arr[mi+1:len(arr)]
        # Reverse whole list 
        arr = arr[cur-1::-1] + arr[cur:len(arr)]
        cur -= 1
    return arr


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(pancakesort(unsorted))
