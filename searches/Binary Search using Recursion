def bsearch(list, idx0, idxn, val):

    if (idxn < idx0):
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)
# Compare the search item with middle most value

        if list[midval] > val:
            return bsearch(list, idx0, midval-1,val)
        elif list[midval] < val:
            return bsearch(list, midval+1, idxn, val)
        else:
            return midval

list = [8,11,24,56,88,131]
print(bsearch(list, 0, 5, 24))
print(bsearch(list, 0, 5, 51))
