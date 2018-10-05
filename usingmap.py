terms=12
result=list(map(lambda x: 2**x,range(terms)))
for i in range(terms):
    print('2 raised to power {0} is : {1}'.format(i,result[i]))