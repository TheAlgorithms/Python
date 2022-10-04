#!/bin/python3

import sys
import socket
from datetime import datetime 

#defining target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])   #translate hostname to ipv4
else:
	 print("Invalid amount of arguments")
	 print("Synatx: python3 portscanner.py <ip>")

#add a pretty banner

print("-"* 50)
print("Scanning Target"+target) 
print("Time Started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(10,85):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(5)  #1 msec timeout
		result = s.connect_ex((target,port))   #returns erros indicator 0 if port open 1 if close
		#print("Checking port "+str(port))
		if result == 0:
			print("port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting Program")
	sys.exit()

except socket.gaierror:
	print("Hostname could not resolved")

except socket.error:
	sys.exit()



