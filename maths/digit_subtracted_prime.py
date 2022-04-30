"""
This follows OEIS entry A185107

https://oeis.org/A185107

Difference of digits of nth prime

It creates an array of nth prime numbers
with their separated digits subtracted from
each other, e.g. 11 [which is prime] being 1 and 1
separated and 0 subtracted from each other.
"""


def dig_sub_prime(max_num):
    """
    Difference of digits of nth prime

    >>> dig_sub_prime(55)

    >>> dig_sub_prime(72)

    >>> dig_sub_prime(1000)

    In order of respective function:
        1.) Checks to make sure that the max_num is
              an unsigned integer

        2.) Produces the array the numbers will be added to.
               One is used as an initiator to accomodate future steps.

        3.) Confirms how to select prime numbers for those
                below ten. Then it assigns appropriate numbers.

        4.) Produces a temporary array used for a range
               to be iterated over in the next function. Also
                produces a stabalizer used to stabalize the results.

        4.) Promotes a while loop to select the prime numbers
               above ten.A temporary array is produced as a range to
               be iterated over = its size is determined by
               a continuous loop where recorded number is
               the number from the last temporary array to start
               from, itr is the last itr that numArr was on, and
               stable is stabilizer. The stabilizer is needed as
               otherwise the range will cause an error.

         5.) The tempory array is iterated over using a forwards
                loop skipping most even numbers [as even numbers can't
                be prime]. Four if statements decide what is prime using
                obvious metrics. After the check, the number is added to
                num_arr while the itr is recorded.

         6.) The Try, Except block is used to deter a maximum recursion depth
                error. The function is recursed until the maximum number is reached.

         7.) The num_arr is iterated over with an appropriate digit subtraction.

    """
    if not isinstance(max_num, int):
        raise TypeError

    if max_num < 1:
        print("Not an Unsigned Integer or Positive Int")
        raise TypeError

    num_arr = [1] * max_num

    rng = max_num

    if max_num > 5:
        rng = 5

    for i in range(rng):
        match i:
            case 1:
                num_arr[1] = 2
            case 2:
                num_arr[2] = 3
            case 3:
                num_arr[3] = 5
            case 4:
                num_arr[4] = 7

    if max_num % 2 == 0:
        stable = 0
    else:
        stable = 1

    recorded_num = 10
    itr = 5

    while num_arr[-1] == 1:
        temp_arr = range(recorded_num + 1, max_num + stable + num_arr[itr - 1])

        for i in temp_arr[::2]:
            if i % 2 == 0:
                continue
            if i % 3 == 0:
                continue
            if i % 7 == 0:
                continue
            if i % 5 == 0:
                continue

            num_arr[itr] = i
            itr += 1

            if num_arr[-1] != 1:
                break

        recorded_num = temp_arr[-1]

    def digit_sub(i):
        if i < 10:
            return i
        return digit_sub(i // 10) - (i % 10)

    for i in range(max_num):
        num_arr[i] = digit_sub(i)

    return num_arr
