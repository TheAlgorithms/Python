# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-10-04 15:54:06
# @Last Modified by:   prateek
# @Last Modified time: 2020-10-04 16:18:22


# Server file

import socket 
import sys

# Create a socket to join two componenets
def create_socket():
	try :
		global host
		global port
		global s 

		host=""
		port = 9090
		s = socket.socket()
	except socket.error as msg:
		print('Error in creating socket '+str(msg))

# Binding the socket and listening for connections

def bind_socket():
	try :
		global host;
		global port;
		global s;

		print('Binding the Port : '+str(port))

		s.bind((host,port))
		s.listen(5)

	except socket.error as msg:
		print('Error in binding socket '+str(msg) +'\n' + 'Retrying ...\n')
		bind_socket()


def send_command(conn):
	
	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd)) > 0 :
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024),'utf-8')
			print(client_response + '\n',end = "")




# Establish the connection with the client 
def accept_conn():
	

	conn,addr = s.accept()
	print('Connection has been established with IP Address : '+str(addr[0] + " with Port Number : "+str(addr[1])))
	send_command(conn)


	conn.close()


def main():
	create_socket()
	bind_socket()
	accept_conn()

main()