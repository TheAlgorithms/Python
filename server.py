# all imports - including #s
import socket
#import os
#import sys
#import subprocess
# end of imports
# the below classes will clarify what information is for the attacker and client
class Termrequire:
    host = socket.gethostname()
    port = 3333 # fake numeral for the moment
class Clientrequire:
    host = socket.gethostname()
    port = 2222 # fake numeral for the moment
#CORE REQUIREMENTS OF PROGRAM:
### host ip = server ip
### potential connection hosts info (host, port)
### user.config
### user.config
# using SERVER for connections and linux meterpreter sessions
# SERVER DETAILS:
    #5 client availability for pivoting #although that is not yet available in a regular form of
    #exploitation  - we have to go with what we have.

# #learnmore - USER_CONFIG
# server ip will be displayed every connection at version 2.0
# terminal attacker socket object creation
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# terminal attacker socket binding
t.bind()
# terminal attacker socket listen
t.listen()
#  client socket object creation
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binding information with s.bind method
s.bind()
#listening for connections with s.listen method
s.listen(1)
# server_functionality waits for terminal shell and then gets client information connectivity
def func4client():
    s.accept()
# terminal functionality for attacker - I will definitely customize it soon. Maybe tkinter?
def func4term():
    t.accept()