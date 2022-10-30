#Program to find the current price of Bitcoin in USD 
import requests
import sys

#The program takes No of bitcoins as a command-line arguements
if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument ")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total_amt = bitcoin * value
    print(f"${total_amt:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit()
