from ppadb.client import Client as AdbClient
import time
# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
time.sleep(5)
phone=[12345,1236778]
for i in phone:
    client.devices()[0].shell(f'am start -a android.intent.action.CALL -d tel:{i}')
    time.sleep(.5)
    x=int(client.devices()[0].shell('dumpsys telephony.registry').split('\n')[2][-1])!=0
    while x:
        x=int(client.devices()[0].shell('dumpsys telephony.registry').split('\n')[2][-1])!=0
        print(x)
    time.sleep(2)
    
    