# This CLI script checks if entered ips are or
# aren`t blacklisted on different lists
# You need to get API key on blacklistchecker
# to make it work (it`s free 30 IPs per month)

import json
import logging
import sys

import requests
from IPy import IP

api_key = "key_CAMF5HI5t4ZzkmgGkioI1tius"


def test_ip(ip: str) -> tuple[str, list] | tuple[str, str] | None:
    result = requests.get(
        "https://api.blacklistchecker.com/check/" + ip, auth=(api_key, "")
    )
    result_dec = json.loads(result.content)
    print(result_dec)
    if result_dec.get("statusCode"):
        res = "limit exceeded"
        detects = "!"
        return (res, detects)
    elif result_dec.get("detections") != 0:
        res = ip
        blsts = result_dec.get("blacklists")
        detects = None
        detects = list(detects)
        for n in blsts:
            if n.get("detected") is True:
                detects.append(n.get("name"))
        return (res, detects)
    else:
        return ()


res_txt = "IP blacklists check returned next results:\n"
send_param = 0
if len(sys.argv) > 1:
    for x in sys.argv[1:]:
        try:
            IP(x)
        except Exception as ex:
            print("Argument isn`t a valid ip(" + x + ")\n")
            print(str(ex) + "\n Skipping argument")
            logging.exception("Caught an error")
        else:
            if test_ip(x) is not None:
                res, detec = test_ip(x)
                if res == "limit exceeded":
                    res_txt = res_txt + " LIMIT Exceeded!"
                    break
                else:
                    res_txt = (
                        res_txt
                        + str(res)
                        + " is detected in "
                        + str(detec)
                        + " blacklists \n \n"
                    )
else:
    print("Type in ip to check")
    x = input()
    try:
        IP(x)
    except Exception as ex:
        print("Argument isn`t a valid ip(" + x + ")")
        print(str(ex) + "\n")
        logging.exception("Caught an error")
        sys.exit()
    else:
        if test_ip(x) is not None:
            res, detec = test_ip(x)
            if res == "limit exceeded":
                res_txt = res_txt + "Limit Exceeded!\n"
            else:
                res_txt = (
                    res_txt
                    + str(res)
                    + " is detected in "
                    + str(detec)
                    + " blacklists \n \n"
                )
if len(res_txt) <= 43:
    print("IPs not blacklisted!")
    print(res_txt)
else:
    print("Blacklist check result is: \n" + res_txt)
