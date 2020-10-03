from send_file import send_file
from receive_file import receive
def main():

    print("File transfer:")
    print("(R)eceive?")
    print("(T)rasnfer?")
    mode = input("? ").lower()
    if mode not in ('r', 't'):
        print("Invalid mode.")
        main()
    if mode == 'r':
        save = input('Save location? ')
        host = input("Override host (empty to use default)? ")
        port = input("Override port (empty to use default)? ")
        receive(save, host, port)
    elif mode == 't':
        fn = input("File to send? ")
        send_file(fn)

if __name__=="__main__":
    main()
