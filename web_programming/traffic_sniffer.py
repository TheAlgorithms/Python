import pyshark
import argparse
from datetime import datetime


def sniff(interface, n_packet, filename):
    capture = pyshark.LiveCapture(interface=interface)
    capture.sniff(packet_count=n_packet)

    with open(filename + '.txt', 'a+') as file:
        for n, pkt in enumerate(capture):
            file.write("Packet #" + str(n + 1) + ':\n')
            file.write(str(pkt) + '\n')
    capture.close()


if __name__ == "__main__":
    programDescription = '''
        Command Line Tool: python sniffer using pyshark; Need to run with `sudo`
    '''

    parser = argparse.ArgumentParser(description=programDescription)
    parser.add_argument("--interface", "-i", help="interface")
    parser.add_argument("--number", "-n", help="number of packets")
    parser.add_argument("--filename", "-f", help="filename to save")
    args = parser.parse_args()

    interface = args.interface if args.interface else 'en0'
    number = abs(int(args.number)) if args.number else 50
    filename = args.filename if args.filename else "result"
    
    sniff(interface, number, filename)

    print('Sniffing is completed at %s' % datetime.now())
