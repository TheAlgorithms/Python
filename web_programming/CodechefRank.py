#!/usr/bin/python3
# To find the python interpreter, when we execute it without python3

"""
To use:
    ./codechef_rank.py <contest-name>
"""

import json
import sys

import requests

id = "<codechef_id>"  # Replace with your codechef id


main_url = "https://www.codechef.com/api/rankings/"
contest_name = sys.argv[1]
# contest_name= input("Enter Contest Name: ")
# contest_name="SEP221C"
# print(contest_name)

url = main_url + contest_name

dict = {}
headers = {
    "authority": "www.codechef.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    # Requests sorts cookies= alphabetically
    "cookie": "_fbp=fb.1.1655306318354.66392898; pg_mm2_cookie_a=85654c31-1e1e-48ec-9f8b-0e71d258436a; twk_uuid_627c0f75b0d10b6f3e71c35d=%7B%22uuid%22%3A%221.H3NO5nd4jOeziibZm2mRXYSI3644LExvXsLy2XAJpeX6oKXKytIrDYkyJ5vtWMPxtdPxOmdp3K4GQf06bf07sXMb0lg4y6VSxlwRr20XGemYXnB479arAdNf5nK9agSM1Md8X1QD9MJkd5ss%22%2C%22version%22%3A3%2C%22domain%22%3A%22codechef.com%22%2C%22ts%22%3A1658326231790%7D; twk_uuid_62397c18a34c2456412c3b26=%7B%22uuid%22%3A%221.H3NMbQzCA5paUeWeHE3S0JdRNNp3WPDuQiFonJ8fJcBrCBAVhTuKUuCbnUKDAgn6QnnQCk4SSwVYleQBJh3z5Upe5NDi9N1RJ0vwflOcLcDwPvkQv50vgNeCcKHWYawcCZU7Rm3m7IMpr6Jl%22%2C%22version%22%3A3%2C%22domain%22%3A%22codechef.com%22%2C%22ts%22%3A1658577496450%7D; _gcl_au=1.1.2141587503.1663165531; FCNEC=%5B%5B%22AKsRol8OKyH-AI_Th8_GaKuT9ARaiyCq5e15MDMmxkCXSOaOOQc2UAg2I7F5xFYcIEao5-R20KCVuy_ekbbJy9ZIXib62nHbQUKxH9JgmNqqvIcNRLtM4hizhC_y2xN4sebGbvmvaBJ_J0P4e_paYSlHUuZgbAYYKg%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; __gads=ID=f702a7a3ed66e141-22854ff149d70012:T=1655306346:RT=1663955229:S=ALNI_MbdnlQ1SgroV8Of5xn4KSpxKrSbKQ; SESS93b6022d778ee317bf48f7dbffe03173=db040399023abeee64d5a77e3d26f067; uid=3137718; __gpi=UID=000006ad96536525:T=1655306346:RT=1666190266:S=ALNI_MYP3iUpXkfMGriNtcMwBbc3u6ExUw; _gid=GA1.2.808286290.1666497045; _clck=17nqn5c|1|f5y|0; _gat_UA-141612136-1=1; _ga_C8RQQ7NY18=GS1.1.1666536681.133.1.1666537079.0.0.0; _ga=GA1.2.306524194.1655306320; _clsk=1qfm2v3|1666537080268|6|0|i.clarity.ms/collect",
    "referer": "https://www.codechef.com/rankings/START43d?filterBy=Institution%3DMaharaja%20Agrasen%20Institute%20of%20Technology%2C%20New%20Delhi&itemsPerPage=100&order=asc&page=1&sortBy=rank",
    "sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",
    "x-csrf-token": "9032eae6fad31fa3844a43d624be7d73fa8304fd3920bea6a5c177a8e25721be",
    "x-requested-with": "XMLHttpRequest",
}

params = {
    "filterBy": "Institution=Maharaja Agrasen Institute of Technology, New Delhi",
    "itemsPerPage": "100",
    "order": "asc",
    "page": "1",
    "sortBy": "rank",
}

# print(url)
r = requests.get(url, params=params, headers=headers).json()
# print(r)
users = r["list"]
c = 1
for i in users:
    v = []
    rank_var = i["rank"]
    score_var = i["score"]
    user_id_var = i["user_handle"]
    v.append(rank_var)
    v.append(score_var)
    v.append(user_id_var)
    dict[c] = v
    c += 1

"""
To get coloured text, using ANSI

\033[1;31m -> RED
\033[1;32m -> GREEN
\033[1;37m -> WHITE

"""
print("\033[1;31mS.No. \t User ID \t \t \t \tRank \t \tScore")  #
for i in dict:
    if len(dict[i][2]) < 8 and dict[i][2] == id:
        print(f"\033[1;32m {i}\t{dict[i][2]}\t\t\t\t\t{dict[i][0]}\t\t{dict[i][1]}")
    elif len(dict[i][2]) < 8:
        print(f"\033[1;37m {i}\t{dict[i][2]}\t\t\t\t\t{dict[i][0]}\t\t{dict[i][1]}")
    elif dict[i][2] == id:
        print(f"\033[1;32m {i}\t{dict[i][2]}\t\t\t\t{dict[i][0]}\t\t{dict[i][1]}")
    else:
        print(f"\033[1;37m {i}\t{dict[i][2]}\t\t\t\t{dict[i][0]}\t\t{dict[i][1]}")
