"""
	File transfer protocol used to send and receive files using FTP server.
	Use credentials to provide access to the FTP client

	Note: Do not use root username & password for security reasons
	  Create a seperate user and provide access to a home directory of the user
	  Use login id and password of the user created 
	  cwd here stands for current working directory
"""

from ftplib import FTP
ftp = FTP('xxx.xxx.x.x')  # Enter the ip address or the domain name here
ftp.login(user='username', passwd='password')
ftp.cwd('/Enter the directory here/')

"""
	The file which will be received via the FTP server
	Enter the location of the file where the file is received
"""

def ReceiveFile():
	FileName = 'example.txt'   """ Enter the location of the file """
	with open(FileName, 'wb') as LocalFile:
		ftp.retrbinary('RETR ' + FileName, LocalFile.write, 1024)
	ftp.quit()

"""
	The file which will be sent via the FTP server
	The file send will be send to the current working directory
"""

def SendFile():
	FileName = 'example.txt'   """ Enter the name of the file """
	with open(FileName, 'rb') as LocalFile:
		ftp.storbinary('STOR ' + FileName, LocalFile)
	ftp.quit()
