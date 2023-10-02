######################################
# This CLI script checks if entered ips are or aren`t blacklisted on different lists
# After configuration it can even send an email report
# You need to get API key on blacklistchecker to make it work (it`s free 30 IPs per month)
######################################


import requests
import sys
from IPy import IP
import smtplib
from email.message import EmailMessage
import json
import logging

api_key = ""
subject = ""
mail_from = ""
mail_to = ""
smtp_user = ""
smtp_passw = ""
smtp_serv = ""
smtp_port = 587


def test_ip(ip: str) -> str, str | None:
    detects = []
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
        for n in blsts:
            if n.get("detected") == True:
                detects.append(n.get("name"))
        return (res, detects)
    else:
        return ()


res_txt = "IP blacklists check returned next results:\n"
send_param = 0
if len(sys.argv) > 1:
    for x in sys.argv[1:]:
        if x in "-y-Y":
            send_param = 1
        else:
            try:
                IP(x)
            except Exception as ex:
                print("Argument isn`t a valid ip(" + x + ")\n Skipping argument")
                logging.exception("Caught an error")
            else:
                if test_ip(x):
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
        logging.exception("Caught an error")
        sys.exit()
    else:
        if test_ip(x):
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
    if send_param == 1:
        mailed = "Y"
    else:
        print("Send e-mail report? (default No)")
        mailed = input()
    if mailed in "Yy" and mailed != "":
        msg = EmailMessage()
        msg.set_content(res_txt)
        msg["Subject"] = subject
        msg["From"] = mail_from
        msg["To"] = mail_to
        try:
            smtp_server = smtplib.SMTP(smtp_server, smtp_port)
            smtp_server.ehlo()
            smtp_server.login(smtp_user, smtp_passw)
            smtp_server.send_message(msg)
            smtp_server.close()
            print("Email sent successfully to " + msg["to"] + "!")
        except Exception as ex:
            print("Something went wrong! ¦.", ex)
    print("Blacklist check result is: \n" + res_txt)
