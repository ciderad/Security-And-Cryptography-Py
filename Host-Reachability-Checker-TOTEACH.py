#!/usr/bin/env python3
"""
Lightweight security placeholder script:
- Pings a target to check reachability
- Verifies integrity of a local file using SHA-256
"""

import hashlib #hashing algorithm library
import subprocess

def ping_host(target: str) -> bool:
    result = subprocess.run(
        ["ping", "-c", "1", target],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def file_hash(path: str) -> str:
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        sha.update(f.read())
    return sha.hexdigest()

if __name__ == "__main__":
    host = "8.8.8.8"
    test_file = "file.txt"
    
    #TEST CASE 1 USING EXAMPLE.TXT
    print(f"[+] Host reachable: {ping_host(host)}")
    print(f"[+] {test_file} SHA-256: {file_hash(test_file)}")