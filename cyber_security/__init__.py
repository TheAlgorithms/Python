"""Cyber security utilities.

This package includes small, self-contained scripts useful for learning or
performing basic security-related tasks, such as:

- Password strength estimation
- Hash cracking
- TCP port scanning with banner grabbing
- File integrity monitoring (hash baseline and verification)
- URL analysis with phishing heuristics

Each module is runnable as a script (python -m cyber_security.<module>) and
also importable for use in other code.
"""

__all__ = [
    "password_strength_checker",
    "hash_cracker",
    "port_scanner",
    "file_integrity_monitor",
    "url_analyzer",
]


