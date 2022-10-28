def TOWUtil(
    arr,
    n,
    curr_elements,
    no_of_selected_elements,
    soln,
    min_diff,
    Sum,
    curr_sum,
    curr_position,
):

    if curr_position == n:
        return

    if (int(n / 2) - no_of_selected_elements) > (n - curr_position):
        return

    TOWUtil(
        arr,
        n,
        curr_elements,
        no_of_selected_elements,
        soln,
        min_diff,
        Sum,
        curr_sum,
        curr_position + 1,
    )

    no_of_selected_elements += 1
    curr_sum = curr_sum + arr[curr_position]
    curr_elements[curr_position] = True

    if no_of_selected_elements == int(n / 2):

        if abs(int(Sum / 2) - curr_sum) < min_diff[0]:
            min_diff[0] = abs(int(Sum / 2) - curr_sum)
            for i in range(n):
                soln[i] = curr_elements[i]
    else:

        TOWUtil(
            arr,
            n,
            curr_elements,
            no_of_selected_elements,
            soln,
            min_diff,
            Sum,
            curr_sum,
            curr_position + 1,
        )

    curr_elements[curr_position] = False


def tugOfWar(arr, n):

    curr_elements = [None] * n

    soln = [None] * n

    min_diff = [999999999999]

    Sum = 0
    for i in range(n):
        Sum += arr[i]
        curr_elements[i] = soln[i] = False

    TOWUtil(arr, n, curr_elements, 0, soln, min_diff, Sum, 0, 0)

    print("The first subset is: ")
    for i in range(n):
        if soln[i] == True:
            print(arr[i], end=" ")
    print()
    print("The second subset is: ")
    for i in range(n):
        if soln[i] == False:
            print(arr[i], end=" ")


if __name__ == "__main__":

    arr = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
    n = len(arr)
    tugOfWar(arr, n)
