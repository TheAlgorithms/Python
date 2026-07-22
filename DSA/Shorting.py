def shorting(list):

    l = len(list)

    for i in range (l):
        mini_index = i

        for j in range(i+1 , l):
            if list[j] < list[mini_index]:
                mini_index = j

        list[i], list[mini_index] = list[mini_index], list[i]

    return list

if __name__ == "__main__":
    list = [45,23,56,87,34,29,75]
    shorted_list = shorting(list)
    print("list is ",shorted_list)