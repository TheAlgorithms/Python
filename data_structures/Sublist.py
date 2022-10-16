def sublist (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists
 
#main
l1 = [1, 2, 3]
print(sublist(l1))
