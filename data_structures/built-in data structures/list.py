# create a list
create_list = [1, "l", 6.0, "list"]
print("creating a list = ", create_list)

# create an empty list
empty_list = []
print("an empty list = ", empty_list)

# list index
list_indexing = ["l", "i", "s", "t", 2, 5]
print(list_indexing[1])
print(list_indexing[3])

# create a nested list
nested_list = [
    [
        "l",
        "i",
    ],
    [6, 9],
    ["list1", "list2"],
    "nested_list",
]
print("a nested list = ", nested_list)

# nested indexing
nested_list = [
    [
        "l",
        "i",
    ],
    [6, 9],
    ["list1", "list2"],
    "nested_list",
]
print(nested_list[0][1])
print(nested_list[1][0])
print(nested_list[2][1])

# negative indexing
list_indexing = ["l", "i", "s", "t", 2, 5]
print(list_indexing[-1])
print(list_indexing[-4])

# list slicing
# syntax Lst[Initial : End : IndexJump]
slicing = ["l", "i", "s", "t", 2, 5, 7.0, "list"]

# positive indexing
# includes elements beginning to end
print(slicing[::])

# elements from index 0th to 3rd, exclude 4th element
print(slicing[:4:])

# elements beginning from index 5th
print(slicing[5::])

# negative indexes
# elements beginning to 3rd
print(slicing[:-4:])

# elements beginning from index 1st to 4th
print(slicing[-7:5:])

slicing = ["l", "i", "s", "t", 2, 5, 7.0, "list"]
# slicing with index jump
print(slicing[2:7:2])

print(slicing[::-1])

print(slicing[::-2])

print(slicing[::3])

# list built-in methods
# append() - Adds an element at the end of the list
append_list = ["Chase", "your", "stars"]
append_list.append("Life is short")
print("adding an element at the end of the list using append() = ", append_list)

# clear() - Removes all the elements from the list
clear_list = ["we", "grow", "through", "what", "we", "go", "through"]
clear_list.clear()
print("removes all the elements from the list using clear() method = ", clear_list)

# copy() - Returns a copy of the list
copy_list = ["simple", "life", "is", "happy", "life", "10"]
lets_copy = copy_list.copy()
print("copy list = ", copy_list)
print("copied list = ", lets_copy)

# count() - Returns the number of elements with the specified value
count_list = ["Everyday", "is", "a", "a", "second", "chance"]
counting = count_list.count("a")
print("no of times the value a appeared in the list = ", counting)

# extend() - Add the elements of a list, to the end of the current list
extend_list1 = ["one", "day", "or", "day", "one"]
extend_list2 = ["you", "decide"]
extend_list1.extend(extend_list2)
print("adding elements to the end of extend_list = ", extend_list1)

# index() - Returns the index of the first element with the specified value
index_list = ["life", "is", "short"]
indexing = index_list.index("short")
print("returns the index of the first occurrence of the value = ", indexing)

# insert() - Adds an element at the specified position
insert_list = ["I", "am", "Bunny"]
insert_list.insert(2, "Honey")
print("adding Honey at index 2 = ", insert_list)

# pop() - Removes the element at the specified position
pop_list = ["I", "M", "Possible", "Impossible"]
pop_list.pop(3)
print("removing the element Impossible = ", pop_list)

# remove() - Removes the first item with the specified value
remove_list = ["All", "we", "have", "is", "Now", "Future"]
remove_list.remove("Future")
print("removing the 'Future' element from the list = ", remove_list)

# reverse() - Reverses the order of the list
reverse_list = ["set", "yourself", "free"]
reverse_list.reverse()
print("reversing the order of the list = ", reverse_list)

# sort() - Sorts the list
sort_list = ["look", "at", "people", "with", "the", "eyes", "of", "your", "heart"]
sort_list.sort()
print("sorting the list in ascending order = ", sort_list)

# list comprehension
# syntax - new_List = [expression(element) for element in oldList if condition]
quote = ["All", "we", "have", "is", "Now"]
upper_quote = [x.upper() for x in quote]
print(upper_quote)
