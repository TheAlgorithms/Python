

'''
Fibonacci sequence with get golden ratio 1.618
'''

a, b = 0, 1

for data in range(0, 20):
    a, b = b, a + b

    print('number {} = {}'.format(a, b/a))
