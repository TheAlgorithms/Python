import os
import platform

def ping(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    return os.system(' '.join(command)) == 0

def main():
    print("=== Simple Network Ping Sweep ===")
    subnet = input("Enter subnet (example: 192.168.1.): ")

    print("\nScanning...\n")
    alive = []

    for i in range(1, 255):
        ip = subnet + str(i)
        if ping(ip):
            print(f"[+] Reachable: {ip}")
            alive.append(ip)

    print("\n=== Scan Complete ===")
    if alive:
        print("Active Hosts:")
        for host in alive:
            print(host)
    else:
        print("No active hosts found.")

if __name__ == "__main__":
    main()


    