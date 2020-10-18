""" program to check grade based on the given value  """

while True:
    grade = int(input('enter value : '))

    if grade >= 100:
        print('your grad is A')
    elif grade >= 90:
        print('your grad is B')
    elif grade >= 80:
        print('your grad is C')
    elif grade >= 70:
        print('your grad is D')
    else:
        print('your grad is E')



