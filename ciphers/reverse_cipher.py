def main():
    utput=''
    msg = input("Enter plain text or cipher text")
    i=len(msg)-1
    while i>=0:
        output = output + msg[i]
        i = i - 1
        
    print("The traslated text is \t " + output)
   
if __name__ == "__main__":
    main()
