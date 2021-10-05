"""


A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?


"""




# the list of numbers divisible by 89
list1 = []

def main(ii):
    """this function will continue up the chain until it reaches 1 or 89"""
    val = 0
    x = str(ii)
    for i in x:
        val = val + int(int(i)*int(i))
    if val==0:
        return val
    if val==int(1):
        return val
    if val==89:
        return val
    else:
        return main(val)



for i in range(0,10000000):
    if main(i)==89:
        list1.append(i)


print(len(list1))