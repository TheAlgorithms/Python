# Pancake sort algorithm 
# Only can reverse array from 0 to i

def pancake_sort(arr):
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
    print(pancake_sort([0,10,15,3,2,9,14,13]))
