binary_input = input("Enter binary number: ")
binary=[]
decimal=0
for i in range (0,len(binary_input)):
    binary.append(int(binary_input[i]))
binary.reverse()
for itr in range(len(binary)):
    if(binary[itr] == 1):
        binary[itr]=binary[itr]*(2**itr)
for i in binary:
    decimal+=i
print("Decimal number is: ",decimal)