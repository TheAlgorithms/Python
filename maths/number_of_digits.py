def num_digits(n):
    digits=0;
    while(n>0):
        n=n//10;
        digits=digits+1
    return digits

num=12345
print("Number of digits in " + str(num) + " is : " + str(num_digits(num)))
