def merge(a1, a2):
    s = []
    a1_idx = 0
    a2_idx = 0
    while a1_idx < len(a1) and a2_idx < len(a2):
        if a1[a1_idx] < a2[a2_idx]:
            s.append(a1[a1_idx])
            a1_idx+=1
        else:
            s.append(a2[a2_idx])
            a2_idx += 1

    if a1_idx == len(a1):
        s.extend(a2[a2_idx: ])
    else: 
        s.extend(a1[a1_idx: ])

    return s

def mergeSort(arr):
    if len(arr) < 2: return(arr)
    l = mergeSort(arr[ :len(arr)//2])
    r = mergeSort(arr[len(arr)//2: ])
    return merge(l,r)
