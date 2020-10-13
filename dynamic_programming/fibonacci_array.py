def fibonacci(n):
    for i in range(n+1):
        fibo = [0, 1]
        if i == 0:
            print ("fibo( 0 ) = ", 0)
        elif i == 1:
            print ("fibo( 1 ) = ", 1)
        else:
            flag = True
            for j in range(2, i):
                if flag: # Replace first element fibonacci(n) + fibonacci(fibo[1])
                    fibo[0] = fibo[1] + fibo[0]
                else: # Replace second element fibonacci(n) + fibonacci(fibo[0])
                    fibo[1] = fibo[0] + fibo[1]
                flag = not flag
            print (fibo[0]+fibo[1])
                
if __name__ == "__main__":
    fibonacci(40)