# Cyber Security Utilities

Small, self-contained scripts for practical security tasks. Each script can be
run as a module or imported.

## Modules

- password_strength_checker: Estimate password strength (entropy) and provide feedback.
- hash_cracker: Hash cracker using a wordlist, supports md5/sha1/sha256.
- port_scanner: Multithreaded TCP port scanner with banner grabbing.
- file_integrity_monitor: Initialize and verify file integrity baselines.
- url_analyzer: Heuristic URL analyzer for phishing and IDN homograph risks.

## Usage

Run any script as a module:

```bash
python -m cyber_security.password_strength_checker --help
python -m cyber_security.hash_cracker --help
python -m cyber_security.port_scanner --help
python -m cyber_security.file_integrity_monitor --help
python -m cyber_security.url_analyzer --help
```

These are educational utilities and should be used responsibly and legally.
