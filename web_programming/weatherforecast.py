import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
serviceurl="http://api.openweathermap.org/data/2.5/weather?q="
key="&APPID=" #ADD YOUR KEY
Valid="True"
while Valid.lower()== "true":
    address=input("Enter the location:")
    if len(address)<1: exit(0)
    url=serviceurl+address+key

    print("Retrieving",url)
    uh=urllib.request.urlopen(url,context=ctx)
    data=uh.read().decode()
    print("Retrieved",len(data),'characters')

    try:
        js=json.loads(data)
    except:
        js=None
    
    if not js or 'cod' not in js or js['cod']!=200:
        print("===========Failure to Retrieve===========")
        print(data)
        exit(0)
        continue
    print(js)
    Valid=input('Do you want to continue?')
