# This CLI script checks if entered ips are or
# aren`t blacklisted on different lists
# You need to get API key on blacklistchecker
# to make it work (it`s free 30 IPs per month)

import json
import re
import sys
from typing import Any

import requests

api_key = "key_CAMF5HI5t4ZzkmgGkioI1tius"


def test_ip(ip: str) -> Any:
    """
    This function tests if an IP is blacklisted on different lists.
    It returns a tuple with the IP and a list of the\
    blacklists where it was detected.
    >>> test_ip('8.8.8.8')
    {'statusCode': 401, 'error': 'Too Many Requests',\
 'message': 'You do not have enough credits on your\
 account. Please upgrade to make another request.'}
    ('limit exceeded!', [])
    >>> test_ip('127.0.0.1')
    {'statusCode': 401, 'error': 'Too Many Requests',\
 'message': 'You do not have enough credits on your\
 account. Please upgrade to make another request.'}
    ('limit exceeded!', [])
    """
    link = f"https://api.blacklistchecker.com/check/{ip}"
    result = requests.get(link, auth=(api_key, ""))
    result_dec = json.loads(result.content)
    print(result_dec)
    detects: list[str] = []
    if result_dec.get("statusCode") == 401:
        res = "limit exceeded!"
        return (res, detects)
    elif result_dec.get("detections") != 0:
        res = ip
        blsts = result_dec.get("blacklists")
        for n in blsts:
            if n.get("detected") is True:
                detects.append(n.get("name"))
        return (res, detects)


def isip(ip: str) -> bool:
    """
    Check if a given string is a valid IP address.
    >>> isip('192.168.0.1')
    True
    >>> isip('10.0.0.256')
    False
    >>> isip('127.0.0.1')
    True
    >>> isip('google.com')
    False
    >>> isip('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
    False
    """
    match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip)
    if not bool(match):
        return False
    return all(0 <= int(octet) <= 255 for octet in ip.split("."))


res_txt = "IP blacklists check returned next results:\n"
send_param = 0
if len(sys.argv) > 1:
    for x in sys.argv[1:]:
        if isip(x) is not True:
            print(f"IP {x} is incorrect\n")
        else:
            if test_ip(x) is not None:
                res, detec = test_ip(x)
                if res == "limit exceeded":
                    res_txt = res_txt + " LIMIT Exceeded!"
                    break
                else:
                    res_txt += f"{res} is detected in {detec} blacklists \n \n"
else:
    print("Type in ip to check")
    x = input()
    if isip(x) is not True:
        print(f"IP {x} is incorrect\n")
    else:
        if test_ip(x) is not None:
            res, detec = test_ip(x)
            if res == "limit exceeded":
                res_txt = res_txt + "Limit Exceeded!\n"
            else:
                res_txt += f"{res} is detected in {detec} blacklists \n \n"
if len(res_txt) <= 43:
    print("IPs not blacklisted!")
    print(res_txt)
else:
    print("Blacklist check result is: \n" + res_txt)
