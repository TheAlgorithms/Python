import socket
import concurrent.futures
import subprocess

# ANSI escape codes for colors
YELLOW = "\033[38;2;255;241;0m"
GREEN = "\033[38;2;0;255;0m"
RESET = "\033[0m"

print(f"{YELLOW}   _____ ____   _____ _____           _    _____")
print(f" / ____|  _ \ / ____|  __ \         | |  / ____|")
print(f"| (___ | |_) | (___ | |__) |__  _ __| |_| (___   ___ __ _ _ __  _ __   ___ _ __")
print(f" \___ \|  _ < \___ \|  ___/ _ \| '__| __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|")
print(f" ____) | |_) |____) | |  | (_) | |  | |_ ____) | (_| (_| | | | | | | |  __/ |")
print(f"|_____/|____/|_____/|_|   \___/|_|   \__|_____/ \___\__,_|_| |_|_| |_|\___|_|")
print("-By ShortBus Security")
print(RESET)

ip = input("Enter IP/Hostname to target: ")
open_ports = []

def scan(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
        scanner.settimeout(0.5)
        result = scanner.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
            print(f"{GREEN}{port}...open{RESET}")

with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
    executor.map(scan, range(1, 65536))

print(f"{YELLOW}Your Bus Is Nearing Your Stop!{RESET}")
if open_ports:
    ports_str = ','.join(map(str, open_ports))
    nmap_cmd = f"nmap -sC -sV {ip} -p {ports_str}"
    subprocess.call(nmap_cmd, shell=True)
print(f"{YELLOW}___________________")
print(f"|,-----.,-----.,---.\\")
print(f"||     ||     ||    \\")
print(f"|`-----'|-----||-----\`----.")
print(f"[       |    -||-   _|    (|")
print(f"[  ,--. |_____||___/.--.   |")
print(f"=-(( `))-----------(( `))-==")
print(f"   `--'             `--'")
print(f"{YELLOW}Your Bus Has Arrived! Beep Beep!{RESET}")
print(RESET)
