# Fibonacci Sequence Using Recursion and Memoization

cache = dict() #Creates a dictionary that will store the results of the numbers already calculated to improve performance.
def fibonacci(n):
    """
    >>> [fibonacci(i) for i in range(12)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    aux = n

    if aux in cache: #Checks if this number has already been calculated before, to assess whether it is necessary to calculate its fibonacci value again.
        return cache[aux] #Existindo, o seu valor fibonacci é retornado

    if (n == 0) or (n == 1): #If it belongs to a base case, it stores the "n" in an auxiliary variable.("Ans -> Answer")
        ans = n
    else:
        ans = fibonacci(n-1) + fibonacci(n-2) #If it does not belong to a base case, he makes a recursive call, keeping his return in the variable "Ans"
    cache[aux] = ans #The answer is saved in the dictionary.

    return ans    #And finally, and returned to the user.


def main() -> None:
    lenght = int(input("Enter an integer greater than or equal to 0: "))
    print(f"The first {lenght} Fibbonaci sequence terms are:")
    print([fibonacci(n) for n in range(lenght)])


if __name__ == "__main__":
    main()
