"""
  Test cases:
  find_minimum_change(987)
  500 100 100 100 100 50 20 10 50 2
  find_minimum_change(500)
  500
  find_minimum_change(0)
  The total value cannot be zero or negetive
  find_minimum_change(-96)
  The total value cannot be zero or negetive
  find_minimum_change(56)
  50 5 1 
"""


def find_minimum_change(V):
    # store value of v as an integer so
    # that it can be used for comparision
    total_value = int(V)

    # All denominations of Indian Currency
    denominations = [1, 2, 5, 10, 20, 50, 100, 500, 2000]
    # find the total length of array,to transverse array
    length = len(denominations)
    # Initialize Result
    answer = []

    # Traverse through all denominations
    i = length - 1  # array values range in [0,n-1]

    # repeat until i is not 0
    while i >= 0:
        # Find denominations that takes "total_value" to zero
        while int(total_value) >= int(denominations[i]):
            # if denomination > current total_value then (total_values - denominations[i])
            total_value -= int(denominations[i])
            answer.append(denominations[i])  # append the answer in the "answers" array

        i -= 1  # decrement i to lower denomination

    # Print result
    for i in range(len(answer)):
        print(answer[i], end=" ")


# Driver Code
if __name__ == "__main__":
    # get input from user to make the change they want
    n = input("Enter the change you want to make in Indian Currency: ")
    if int(n) == 0 or int(n) < 0:  # it cannot be 0 or negetive
        print("The total value cannot be zero or negetive.")
    else:
        print("Following is minimal number", "of change for", n, ": ", end="")
        find_minimum_change(n)
