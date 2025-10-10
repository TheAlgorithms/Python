"""
P2P File Sharing Implementation
Author: Nikhil Karoriya
Description: This module implements a secure peer-to-peer file sharing algorithm
using socket programming, AES for data encryption, RSA for key exchange and Zlib for data compression

Usage:
    python peer.py --listen-port 5001

You will be prompted for:

    Send file (y/n)? y
    Enter file path to send: sample.txt
    Enter receiver's IP address: localhost (or receiver's IP address)
    Enter receiver's port: 6001
"""

import os
import socket
import threading
import traceback
from tqdm import tqdm
import argparse
from time import sleep
from crypto.rsa_crypto import (
    decrypt_with_rsa_private_key,
    encrypt_with_rsa_public_key,
    generate_rsa_key_pair,
    is_valid_pem_key,
)
from crypto.aes_crypto import (
    generate_aes_key,
    encrypt_chunk_with_aes,
    decrypt_chunk_with_aes,
)
from utils.file_utils import (
    ensure_dir,
    sha256_digest_stream,
    is_valid_ip,
    is_valid_port,
)
from utils.file_utils import CHUNK_SIZE

PRIVATE_KEY_PATH = "keys/private_key.pem"
PUBLIC_KEY_PATH = "keys/public_keys.pem"
RECEIVE_DIR = "received_files"

ensure_dir(RECEIVE_DIR)
ensure_dir("keys")

if not is_valid_pem_key(PRIVATE_KEY_PATH, is_private=True) or not is_valid_pem_key(
    PUBLIC_KEY_PATH, is_private=False
):
    print("\n[!] RSA key missing or invalid. Regenerating...")
    generate_rsa_key_pair(PRIVATE_KEY_PATH, PUBLIC_KEY_PATH)
    print("\n[+] RSA key pair regenerated.")

parser = argparse.ArgumentParser()
parser.add_argument("--listen-port", type=int, required=True)
args = parser.parse_args()

LISTEN_PORT = args.listen_port


def peer_listener():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", LISTEN_PORT))
        server_socket.listen(1)
        print(f"\n[+] Listening on port {LISTEN_PORT}...")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"\n\n[+] Incoming connection from {addr}\n")

            try:
                key_size = int.from_bytes(client_socket.recv(4), "big")
                encrypted_key = client_socket.recv(key_size)

                name_len = int.from_bytes(client_socket.recv(4), "big")
                file_name = client_socket.recv(name_len).decode()

                extension = int.from_bytes(client_socket.recv(4), "big")
                file_extension = client_socket.recv(extension).decode()

                total_size = int.from_bytes(client_socket.recv(8), "big")

                aes_key = decrypt_with_rsa_private_key(encrypted_key, PRIVATE_KEY_PATH)

                file_path = os.path.join(RECEIVE_DIR, file_name)

                with (
                    open(file_path, "wb") as f_out,
                    tqdm(
                        total=total_size,
                        desc=f"[+] Receiving {file_name}",
                        unit="B",
                        unit_scale=True,
                    ) as pbar,
                ):
                    received_bytes = 0
                    while received_bytes < total_size:
                        rcv_chunk_size = int.from_bytes(client_socket.recv(4), "big")
                        encrypted_chunk = b""

                        while len(encrypted_chunk) < rcv_chunk_size:
                            part = client_socket.recv(
                                rcv_chunk_size - len(encrypted_chunk)
                            )
                            if not part:
                                raise Exception(
                                    "\n[!] Connection lost during transfer."
                                )
                            encrypted_chunk += part

                        decrypted_chunk = decrypt_chunk_with_aes(
                            encrypted_chunk, aes_key, file_extension
                        )
                        f_out.write(decrypted_chunk)
                        received_bytes += len(decrypted_chunk)
                        pbar.update(len(decrypted_chunk))

                print(f"\n[+] File saved to {file_path}")
                file_hash = sha256_digest_stream(file_path)
                print(f"\n[+] SHA256 Hash: {file_hash}")

            except Exception as e:
                print(f"\n[!] ERROR receiving file: {str(e)}\n{traceback.format_exc()}")
            finally:
                client_socket.close()

    except Exception as e:
        print(f"\n[!] Server failed: {str(e)}\n{traceback.format_exc()}")


def send_file(file_path, peer_ip, peer_port):
    try:
        file_name = os.path.basename(file_path)
        file_extension = os.path.splitext(file_name)[1].lower()

        aes_key = generate_aes_key()
        encrypted_key = encrypt_with_rsa_public_key(aes_key, PUBLIC_KEY_PATH)
        file_size = os.path.getsize(file_path)

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((peer_ip, peer_port))

        client_socket.sendall(len(encrypted_key).to_bytes(4, "big"))
        client_socket.sendall(encrypted_key)

        client_socket.sendall(len(file_name.encode()).to_bytes(4, "big"))
        client_socket.sendall(file_name.encode())

        client_socket.sendall(len(file_extension.encode()).to_bytes(4, "big"))
        client_socket.sendall(file_extension.encode())

        client_socket.sendall(file_size.to_bytes(8, "big"))

        print()

        with (
            open(file_path, "rb") as f,
            tqdm(
                total=file_size,
                desc=f"[+] Sending {file_name}",
                unit="B",
                unit_scale=True,
            ) as pbar,
        ):
            for chunk in iter(lambda: f.read(CHUNK_SIZE), b""):
                encrypted_chunk = encrypt_chunk_with_aes(chunk, aes_key, file_extension)
                client_socket.sendall(len(encrypted_chunk).to_bytes(4, "big"))
                client_socket.sendall(encrypted_chunk)
                pbar.update(len(chunk))

        print(f"\n[+] File '{file_name}' sent successfully to {peer_ip}:{peer_port}.")
        client_socket.close()

    except Exception as e:
        print(f"\n[!] Failed to send file: {str(e)}\n{traceback.format_exc()}")


if __name__ == "__main__":
    try:
        threading.Thread(target=peer_listener, daemon=True).start()
        sleep(0.5)

        while True:
            user_input = (
                input("\nSend file [y], wait [w], or exit [e]? ").strip().lower()
            )

            if user_input == "e":
                print("\n[INFO] Exiting...")
                break

            elif user_input == "y":
                file_path = input("\nEnter file path to send: ").strip()
                peer_ip = input("\nEnter receiver's IP address: ").strip()
                peer_port_input = input("\nEnter receiver's port: ").strip()

                if not is_valid_port(peer_port_input) or not is_valid_ip(peer_ip):
                    print("\n[!] Receiver IP or port not correct/specified.")
                    continue

                if not os.path.isfile(file_path):
                    print("\n[!] File does not exist.")
                    continue

                peer_port = int(peer_port_input)
                send_file(file_path, peer_ip, peer_port)

            elif user_input == "w":
                print("\n[INFO] Waiting for incoming transfers...")

            else:
                print("\n[!] Invalid input. Use 'y', 'w', or 'e'.")

    except KeyboardInterrupt:
        print("\n[INFO] Exiting by keyboard interrupt.")

    except Exception as e:
        print(f"\n[!] An error occurred: {str(e)}\n{traceback.format_exc()}")
