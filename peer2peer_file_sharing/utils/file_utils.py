import os
import hashlib
import ipaddress

CHUNK_SIZE = 64 * 1024


def sha256_digest_stream(path: str) -> str:
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(CHUNK_SIZE), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def ensure_dir(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)


def is_valid_ip(ip_str):
    try:
        if ip_str.strip().lower() == "localhost":
            return True
        ipaddress.ip_address(ip_str)
        return True

    except ValueError:
        return False


def is_valid_port(port_str):
    try:
        port = int(port_str)
        return 1 <= port <= 65535

    except ValueError:
        return False
