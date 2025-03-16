import time
set_time=int(input("enter the time"))
for i in range(set_time,0,-1):
     second=i%60
     minuit=int(i/60)%60
     hour=int(i/3600)
     print(f"{hour:02}:{minuit:02}:{second:02}")
     time.sleep(1)
print("your time is over")     