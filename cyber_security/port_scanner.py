#!/usr/bin/env python3
"""Multithreaded TCP port scanner with optional banner grabbing.

Usage:
  python -m cyber_security.port_scanner 192.168.1.10 --ports 1-1024 --threads 200 --timeout 0.5 --banner
"""

from __future__ import annotations

import argparse
import concurrent.futures
import socket
import sys
from dataclasses import dataclass
from typing import Iterable, Tuple


DEFAULT_TIMEOUT = 0.7
DEFAULT_THREADS = 200


@dataclass
class ScanResult:
    host: str
    port: int
    is_open: bool
    banner: str | None


def parse_ports(spec: str) -> Iterable[int]:
    parts = (p.strip() for p in spec.split(","))
    for part in parts:
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start = int(start_s)
            end = int(end_s)
            for p in range(max(1, start), min(65535, end) + 1):
                yield p
        else:
            yield int(part)


def try_connect(host: str, port: int, timeout: float, banner: bool) -> ScanResult:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((host, port))
        if result != 0:
            return ScanResult(host, port, False, None)
        recv_banner: str | None = None
        if banner:
            try:
                sock.sendall(b"\r\n")
                data = sock.recv(1024)
                if data:
                    recv_banner = data.decode("utf-8", errors="replace").strip()
            except Exception:
                recv_banner = None
        return ScanResult(host, port, True, recv_banner)
    except Exception:
        return ScanResult(host, port, False, None)
    finally:
        try:
            sock.close()
        except Exception:
            pass


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="TCP port scanner with multi-threading and banner grab."
    )
    parser.add_argument("host", help="Target IPv4/hostname")
    parser.add_argument(
        "--ports", default="1-1024", help="Port spec, e.g., 1-1024,22,80,443"
    )
    parser.add_argument(
        "--threads", type=int, default=DEFAULT_THREADS, help="Max worker threads"
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT,
        help="Socket timeout in seconds",
    )
    parser.add_argument(
        "--banner", action="store_true", help="Attempt to grab service banner"
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)

    # Resolve host once
    try:
        host = socket.gethostbyname(args.host)
    except socket.gaierror:
        print(f"Unable to resolve host: {args.host}", file=sys.stderr)
        return 2

    ports = list(parse_ports(args.ports))
    if not ports:
        print("No ports to scan.", file=sys.stderr)
        return 2

    tasks: list[Tuple[str, int]] = [(host, p) for p in ports]

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=max(1, args.threads)
    ) as executor:
        future_to_port = {
            executor.submit(try_connect, host, port, args.timeout, args.banner): port
            for _, port in tasks
        }
        for future in concurrent.futures.as_completed(future_to_port):
            res = future.result()
            if res.is_open:
                line = f"{res.host}:{res.port} open"
                if args.banner and res.banner:
                    line += f" | {res.banner}"
                print(line)

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
