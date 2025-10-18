number = int(input("Enter you number here ").strip())


def divisors_of_number(number):
    i = 1
    list1 = []
    # by observation we can go till i reaches square root of n
    while i**2 <= number:
        if number % i == 0:
            list1.append(i)
            # added the number to list
            if i != number // i:
                # if i is the divisor then n/i will also be a divsior
                list1.append(number // i)
                # added the number to list
        i = i + 1
        # i is increased by 1
    list1.sort()
    return list1
