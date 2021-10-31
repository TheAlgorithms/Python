# program to check whether number is prime or not

# take user input
num = int(input('enter number'))

# check for factors between 2 to num-1
for i in range(2,num):
    
    # if a factor exists then not prime
    if num % i==0:
        print('the number is not prime')
        break
    # if factor does not exist then number is prime
    else:
        print ('the number is prime')