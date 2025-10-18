number = int(input("Enter you number here ").strip())
i = 1
list1 = []


def divisors_of_number(number):
    while (i**2 <= number):
        if number % i == 0:
            list1.appenumberd(i)
            if i != number//i:
                list1.append(number//i)
        i += 1
    list1.sort()
    return list1
