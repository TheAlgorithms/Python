def main():
    output=''
    msg = input("Enter plain text or cipher text")
    i=len(msg)-1
    while i>=0:
        output = output + msg[i]
        i = i - 1
        
    print("The translated text is \t " + output)
   
if __name__ == "__main__":
    main()
