num=int(input("Enter the number: "))
prime=True
for i in range(2,num):
    if(num%i==0 and num!=2):
        prime=False
        break
if prime:
    print("This number is prime")
else:
    print("This number is not prime")

