"""
Checking valid Ip Address.
A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-254

for example: 192.168.23.1, 192.254.254.254, 192.168.76.45 are valid IP address
             192.168.255.0, 255.192.3.121, 192.0.1.255 are Invalid IP address
"""
def check_valid_IP(ip):
    """
    print "Valid IP adddress" If IP is valid.
    or
    print "Invalid IP address" If IP is Invalid.

    >>> check_valid_IP(192.168.0.23)
    192.168 is an valid IP address

    >>> check_valid_IP(192.255.15.8)
    192.168 is an valid IP address
    
    """
    ip1 = (ip.replace(".", " "))
    list1 = [int(i) for i in ip1.split() if i.isdigit()]
    count = 0
    for i in list1:
        if i > 254:
            count += 1
            break
    if count:
        return "Invalid"
    else:
        return "Valid"
if __name__ == "__main__":
    ip = input()
    output = check_valid_IP(ip)
    if output == "Invalid":
        print(f"{ip} is an {check_valid_IP(ip)} IP address")
    else:
        print(f"{ip} is a {check_valid_IP(ip)} IP address")
