import serial
import argparse

"""
Tested with GSM modem
Windows and Linux
"""

parser = argparse.ArgumentParser()
parser.add_argument('--port', default="/dev/ttyUSB0", help="Command Control Port. Windows: COM | Linux: /dev/ttyUSB0")
parser.add_argument('--baudrate', default=115200, type=int, help="Baudrate")
parser.add_argument('--to', type=str, default="08221278121", help="Recipient Number")
parser.add_argument('--message', type=str, default="test", help="message content")

args, unknown = parser.parse_known_args()

def send_sms(port, baudrate, recipient, message):
    phone = serial.Serial(port,  baudrate, timeout=0)
    try:
        phone.write(b'AT\r\n')
        phone.write(b'AT+CMGF=1\r\n')
        phone.write(b'AT+CSCS="GSM"\r\n')
        phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r\n')
        phone.write(message.encode() + b'\r\n')
        time.sleep(0.5)
        phone.write(bytes([26]))
        time.sleep(0.5)
        print("Message Sent")
    except:
        print("Failed sending message")
    finally:
        phone.close()

send_sms(args.port, args.baudrate, args.to, args.message)
