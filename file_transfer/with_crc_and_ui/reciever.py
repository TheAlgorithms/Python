import socket

HOST_ADDR = "localhost"
HOST_PORT = 31214
key = "1001"


def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append("0")
        else:
            result.append("1")
    return "".join(result)


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
    print("Remainder :", checkword)
    return checkword


def encodeData(data, key):
    l_key = len(key)
    remainder = mod2div(data, key)
    for i in remainder:
        if i != "0":
            print("Transfer of Frame failed !")
            return "NULL"
    print("Transfer of Frame successfull.")
    codeword = data
    return codeword


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST_ADDR, HOST_PORT))

recSize = int(s.recv(1024).decode())

recName = s.recv(1024).decode()


print("recieved size: ", recSize)
strngData = []

while recSize > 0:
    recdata = s.recv(1048576).decode()

    if len(recdata) == 0:
        break

    print("Received data from sender :", recdata + "\n size is: ", len(recdata))

    checked = encodeData(recdata, key)
    if checked == "NULL":
        s.send("NACK".encode())
        continue
    else:
        s.send("ACK".encode())
        recSize -= 1

    print("Checked recieved data : " + checked)
    maindata = checked[: -(len(key) - 1)]
    print("Data Recieved : " + maindata)
    arr = parts = [maindata[i : i + 8] for i in range(0, len(maindata), 8)]
    binary_data = bytes([int(binary_str, 2) for binary_str in arr])
    # print("Data to be stored in file :", binary_data.decode())
    strngData.append(binary_data)


bytedata = b"".join(strngData)

fl = open(recName, "wb")
fl.write(bytedata)
fl.close()

s.close()
