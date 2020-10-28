def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i - 1
        nxt_element = InputList[i]
        # Compare the current element with next one

        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j + 1] = InputList[j]
            j = j - 1
        InputList[j + 1] = nxt_element


list = [19, 2, 31, 45, 30, 11, 121, 27]
insertion_sort(list)
print(list)

#op
#[2, 11, 19, 27, 30, 31, 45, 121]