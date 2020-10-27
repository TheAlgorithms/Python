def linear_search(lst,key):
    flag = 0
    for i in lst:
        if i == key:
            print("Found at position {}".format(lst.index(i)+1))
            flag = flag+1
    if flag == 0:
        print("Not Found")


# Driver Code
my_list = [1,5,3,4]
linear_search(my_list,5)
linear_search(my_list,2)


