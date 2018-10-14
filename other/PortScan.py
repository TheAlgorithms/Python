#!/usr/bin/env python3

''' PortScan v3
    -----------
    This application scans for open ports on the designated system. It uses
    multiprocessing to speed up this process.
'''

import socket
import subprocess
import sys
from datetime import datetime
from multiprocessing import Pool

def scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print("Port {}:\tOpen".format(port))
        sock.close()
    except socket.gaierror:
        print('Hostname could not be resolved.')
        sys.exit(0)
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit(0)
    except:
        return

if __name__ == '__main__':
    ports = list(range(1,4096))
    target = ''
    try:
        target = sys.argv[1]
    except:
        print("\nUsage:\t{} [target]\n\n\tScan for open ports on target machine.\n".format(sys.argv[0]))
        sys.exit(0)
    
    # Clear the screen
    subprocess.call('clear', shell=True)
    
    target_ip  = socket.gethostbyname(target)
    
    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", target_ip)
    print("-" * 60)
    
    # Check what time the scan started
    t1 = datetime.now()
    
    with Pool(processes = 8) as p:
        p.map(scan, ports)
    
    # Checking the time again
    t2 = datetime.now()
    
    # Calculates the difference of time, to see how long it took to run the script
    total =  t2 - t1
    
    # Printing the information to screen
    print('Scanning Completed in: ', total)
