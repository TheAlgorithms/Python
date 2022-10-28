# Python3 program for above approach

# function that tries every possible
# solution by calling itself recursively
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

    # checks whether the it is going
    # out of bound
    if curr_position == n:
        return

    # checks that the numbers of elements
    # left are not less than the number of
    # elements required to form the solution
    if (int(n / 2) - no_of_selected_elements) > (n - curr_position):
        return

    # consider the cases when current element
    # is not included in the solution
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

    # add the current element to the solution
    no_of_selected_elements += 1
    curr_sum = curr_sum + arr[curr_position]
    curr_elements[curr_position] = True

    # checks if a solution is formed
    if no_of_selected_elements == int(n / 2):

        # checks if the solution formed is better
        # than the best solution so far
        if abs(int(Sum / 2) - curr_sum) < min_diff[0]:
            min_diff[0] = abs(int(Sum / 2) - curr_sum)
            for i in range(n):
                soln[i] = curr_elements[i]
    else:

        # consider the cases where current
        # element is included in the solution
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

    # removes current element before returning
    # to the caller of this function
    curr_elements[curr_position] = False


# main function that generate an arr
def tugOfWar(arr, n):

    # the boolean array that contains the
    # inclusion and exclusion of an element
    # in current set. The number excluded
    # automatically form the other set
    curr_elements = [None] * n

    # The inclusion/exclusion array
    # for final solution
    soln = [None] * n

    min_diff = [999999999999]

    Sum = 0
    for i in range(n):
        Sum += arr[i]
        curr_elements[i] = soln[i] = False

    # Find the solution using recursive
    # function TOWUtil()
    TOWUtil(arr, n, curr_elements, 0, soln, min_diff, Sum, 0, 0)

    # Print the solution
    print("The first subset is: ")
    for i in range(n):
        if soln[i] == True:
            print(arr[i], end=" ")
    print()
    print("The second subset is: ")
    for i in range(n):
        if soln[i] == False:
            print(arr[i], end=" ")


# Driver Code
if __name__ == "__main__":

    arr = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
    n = len(arr)
    tugOfWar(arr, n)
