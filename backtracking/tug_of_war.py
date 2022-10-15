"""
           Given a  set of n integers, divide the set in two subsets of
           n/2 sizes each such that  the absolute difference of the sum
           of two subsets is as minimum as possible. If n is even, then
           sizes of two subsets must be strictly  n/2 and if n  is odd,
           then size of one subset must be (n-1)/2 and size of other su
           bset must be (n+1)/2.

"""

""" EXAMPLE """
"""   
          let given set  be {3, 4, 5, -3, 100, 1, 89, 54, 23, 20}, the
          size of set is 10. Output for  this set should be {4, 100, 1
          , 23, 20} and {3, 5, -3, 89, 54}. Both output subsets are of
          size 5 and sum of elements in  both subsets is same (148 and
          148).
          Let us consider another example where n is odd. Let given se
          t be {23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4}. The outpu
          t subsets should be {45, -34, 12, 98, -1} and {23, 0, -99, 4
          , 189, 4}. The sums of elements in two subsets are 120 and 1
          21 respectively.
          The following solution tries every possible subset of half s
          ize. If one subset of half size is formed, the remaining ele
          ments form the other subset. We initialize current set as em
          pty and one by one build it. There are two possibilities for
          every element, either it  is part of current set, or it is p
          art of the remaining elements (other subset). We consider bo
          th possibilities for every element. When the size of current
          set  becomes  n/2, we check whether this solutions is better
          than the best solution available so far. If it is, then we u
          pdate the best solution.
"""
def TOWUtil(arr, n, curr_elements, no_of_selected_elements,
            soln, min_diff, Sum, curr_sum, curr_position):

    if (curr_position == n):
        return

    if ((int(n / 2) - no_of_selected_elements) >
            (n - curr_position)):
        return

    TOWUtil(arr, n, curr_elements, no_of_selected_elements,
            soln, min_diff, Sum, curr_sum, curr_position + 1)

    no_of_selected_elements += 1
    curr_sum = curr_sum + arr[curr_position]
    curr_elements[curr_position] = True

    if (no_of_selected_elements == int(n / 2)):

        if (abs(int(Sum / 2) - curr_sum) < min_diff[0]):
            min_diff[0] = abs(int(Sum / 2) - curr_sum)
            for i in range(n):
                soln[i] = curr_elements[i]
    else:

        TOWUtil(arr, n, curr_elements, no_of_selected_elements,
                soln, min_diff, Sum, curr_sum, curr_position + 1)

    curr_elements[curr_position] = False



def tugOfWar(arr, n):

    curr_elements = [None] * n

    soln = [None] * n

    min_diff = [999999999999]

    Sum = 0
    for i in range(n):
        Sum += arr[i]
        curr_elements[i] = soln[i] = False

    TOWUtil(arr, n, curr_elements, 0,
            soln, min_diff, Sum, 0, 0)

    print("The first subset is: ")
    for i in range(n):
        if (soln[i] == True):
            print(arr[i], end=" ")
    print()
    print("The second subset is: ")
    for i in range(n):
        if (soln[i] == False):
            print(arr[i], end=" ")


if __name__ == '__main__':

    arr = [23, 45, -34, 12, 0, 98,
           -99, 4, 189, -1, 4]
    n = len(arr)
    tugOfWar(arr, n)

