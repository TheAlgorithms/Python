import random
import textwrap
import tkinter as tk
import socket
import threading
import select
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from tkinter.messagebox import showinfo


window = tk.Tk()
window.title("Sender")

topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="Connect", command=lambda: start_server())
btnStart.pack(side=tk.LEFT)
btnStop = tk.Button(
    topFrame, text="Stop", command=lambda: stop_server(), state=tk.DISABLED
)
btnStop.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))

middleFrame = tk.Frame(window)
lblHost = tk.Label(middleFrame, text="Host: X.X.X.X")
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text="Port:XXXX")
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))

clientFrame = tk.Frame(window)
lblLine = tk.Label(clientFrame, text="**********Error List**********").pack()
scrollBar = tk.Scrollbar(clientFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(clientFrame, height=15, width=40)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(
    yscrollcommand=scrollBar.set,
    background="#F4F6F7",
    highlightbackground="grey",
    state="disabled",
)
clientFrame.pack(pady=(5, 10))
# btnFSend = tk.Button(clientFrame, height=2, text="Send File", command=lambda :send_file() )
# btnFSend.pack(side=tk.BOTTOM)


def update_progress_label():
    return f"Current Progress: {pb['value']:0,.2f}%"


bottomFrame = tk.Frame(window)
pb = ttk.Progressbar(bottomFrame, orient="horizontal", mode="determinate", length=260)
pb.pack(side=tk.TOP)
value_label = ttk.Label(bottomFrame, text=update_progress_label())
value_label.pack(side=tk.TOP)
btnFSend = tk.Button(
    bottomFrame, height=2, text="Send File", command=lambda: send_file()
)
btnFSend.pack(side=tk.BOTTOM)
bottomFrame.pack(side=tk.BOTTOM, pady=(5, 10))


HOST_ADDR = "localhost"
HOST_PORT = 31214
key = "1001"
s = None


def start_server():
    global s, HOST_ADDR, HOST_PORT
    btnStart.config(state=tk.DISABLED)
    btnStop.config(state=tk.NORMAL)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST_ADDR, HOST_PORT))
    s.listen(5)

    lblHost["text"] = "Host: " + HOST_ADDR
    lblPort["text"] = "Port: " + str(HOST_PORT)


def stop_server():
    global s
    btnStart.config(state=tk.NORMAL)
    btnStop.config(state=tk.DISABLED)
    s.close()


def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append("0")
        else:
            result.append("1")
    return "".join(result)


def randIndGen(m, k):
    chk = int(random.random() * 100) % 2
    if chk == 1:
        ind = int(random.random() * 1000) % (m + k - 1)
        print("Error introduced at index : " + str(ind))
        return ind
    print("No error intoduced.")
    return -1


# crc algo -> https://en.wikipedia.org/wiki/Cyclic_redundancy_check
def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]
    while pick < len(dividend):
        if tmp[0] == "1":
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor("0" * pick, tmp) + dividend[pick]
        pick += 1
    if tmp[0] == "1":
        tmp = xor(divisor, tmp)
    else:
        tmp = xor("0" * pick, tmp)
    checkword = tmp
    print("Additional redundant bits :", checkword)
    return checkword


def encodeData(data, key):
    l_key = len(key)
    appended_data = data + "0" * (l_key - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword


rate = -1


def progress():
    global rate
    if rate == -1:
        pb["value"] = 0
        value_label["text"] = update_progress_label()
    elif pb["value"] < 100:
        pb["value"] += rate
        value_label["text"] = update_progress_label()

    bottomFrame.update()


def update_err_names_display(err_lst, totaErr, extraData, tsize):
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete("1.0", tk.END)

    for i in range(len(err_lst)):
        c = "Error in frame: " + str(i) + " & Times: " + str(err_lst[i])
        tkDisplay.insert(tk.END, c + "\n")

    a1 = "Total File Size: " + str(tsize) + " KB"
    tkDisplay.insert(tk.END, a1 + "\n")
    a = "Total Errors: " + str(totaErr)
    tkDisplay.insert(tk.END, a + "\n")
    b = "Total Extra Data Sent: " + str(extraData) + " KB"
    tkDisplay.insert(tk.END, b + "\n")
    tkDisplay.config(state=tk.DISABLED)


def send_file():
    global rate
    filename = askopenfilename()

    fname = filename.split("/")
    nname = fname[len(fname) - 1]

    print(filename)

    c, addr = s.accept()

    f = open(filename, "rb")
    data = f.read()
    # print("Data in the file :", data.decode())
    binary_digits = [bin(byte)[2:].zfill(8) for byte in data]
    data = "".join(binary_digits)
    print("Data in binary format :", data)

    n = -1
    while n > len(data) or n == -1:
        n = input("Enter the number of characters to be sent at a time : ")
        n = int(n)
        n = n * 8
        if n > len(data):
            print("Not Possible")

    parts = textwrap.wrap(data, n)
    print("Parts :", parts)

    print("datasize", len(data))
    sizeSe = len(data) // n

    c.send(str(sizeSe).encode())

    c.send(nname.encode())

    ErrorRep = [0] * sizeSe
    totalErrors = 0

    i = 0
    rate = 100 / sizeSe
    while i < sizeSe:
        binary = encodeData(parts[i], key)

        b_arr = list(binary)

        print("size of barray: ", len(b_arr))
        print("size of prta: ", len(parts[i]))
        print("size of barray: ", len(binary))
        print("size of key: ", len(key))

        ind = randIndGen(len(parts[i]), len(key))
        print()
        print("error ind: ", ind)
        print()
        if ind != -1:
            if b_arr[ind] == "1":
                b_arr[ind] = "0"
            else:
                b_arr[ind] = "1"

        b_data = "".join(b_arr)

        c.send(b_data.encode())

        msg = c.recv(1024).decode()

        if msg == "ACK":
            print("Frame sent successfully.")
            progress()
            i += 1
        elif msg == "NACK":
            print("Error sending frame :", i)
            print("Resending Frame...", i)
            ErrorRep[i] += 1
            totalErrors += 1

    print("Total Errors: ", totalErrors)

    print()
    t = sizeSe * n / (8 * 1024)
    calc = totalErrors * n / (8 * 1024)

    update_err_names_display(ErrorRep, totalErrors, calc, t)
    for i in range(len(ErrorRep)):
        print("Error in frame: ", i, " & Times: ", ErrorRep[i])

    print("Total Extra Data Sent: ", calc, "MB")
    rate = -1
    progress()
    showinfo(message="The progress completed!")

    stop_server()


window.mainloop()
