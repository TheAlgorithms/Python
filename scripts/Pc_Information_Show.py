import argparse
import sys
import socket
import psutil #pip install psutil

def python_version():
    return sys.version_info

def ip_addresses():
    hostname = socket.gethostname()
    addresses = socket.getaddrinfo(hostname, None)

    address_info = []
    for address in addresses:
        address_info.append((address[0].name, address[4][0]))
    return address_info

def cpu_load():
    return psutil.cpu_percent(interval=0.1)

def ram_available():
    return psutil.virtual_memory().available

def ac_connected():
    return psutil.sensors_battery().power_plugged

def show_sensors():
    print("Python Version:{0.major}.{0.minor}".format(python_version()))
    for address in ip_addresses():
        print("IP Addresses: {0[1]} ({0[0]})".format(address))
    print("CPU Load: {:.1f}".format(cpu_load()))
    print("RAM Available: {} MiB".format(ram_available() / 1024**2))
    print("AC Connected: {}".format(ac_connected()))

def command_line(argv):
    parser = argparse.ArgumentParser(
        description='Display the values of the sensors',add_help=True,)
    arguments = parser.parse_args()
    show_sensors()

if __name__ == '__main__':
    command_line(sys.argv)
