
def is_prime(n):
    """function to find if the given
    number is prime"""
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


i = 0   # iterator for the numbers

gap = 1   # gap for every four iterations

ratio = 1 # ratio of lenght of primes to length of diagonals

primes = []  # prime numbers on the diagonal

all_numbers = [1]  # all the numbers, including 1

# While loop, to loop until we reach the last number
while ratio > 0.1:
    for j in range(4):
        # generating the value of n for 2n+1
        i += gap
        # generating the odd number
        present_number = 2*i + 1
        # appending the number to all_numbers
        all_numbers.append(present_number)
        # appending to prime if the number is prime
        if is_prime(present_number):
            primes.append(2*i + 1)
    # changing the value of ratio at the end of loop
    ratio = float(len(primes))/len(all_numbers)
    # increasing the gap after every 4 numbers
    gap += 1
    
if __name__ == "__main__":
    print( int((2*i+1)**0.5))
