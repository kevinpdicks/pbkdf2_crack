#!/usr/bin/env python3

import hashlib
from multiprocessing import Pool, cpu_count
import sys

def check_password(args):
    password_bytes, salt, iterations, target_hash = args
    try:
        computed = hashlib.pbkdf2_hmac('sha256', password_bytes, salt.encode('utf-8'), iterations)
        if computed.hex() == target_hash:
            return password_bytes.decode('utf-8', errors='ignore').strip()
    except Exception:
        pass
    return None

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python3 crack_pbkdf2.py <salt> <target_hash_hex> <wordlist_path> <iterations=600000>")
        print("Example: python3 crack_pbkdf2.py mysalt 1a2b3c... /path/to/rockyou.txt 600000")
        sys.exit(1)

    salt = sys.argv[1]
    target_hash = sys.argv[2]
    wordlist_path = sys.argv[3]
    iterations = int(sys.argv[4]) if len(sys.argv) > 4 else 600000

    print(f"[*] Targeting PBKDF2-SHA256 with salt: {salt}")
    print(f"[*] Target hash: {target_hash}")
    print(f"[*] Iterations: {iterations}")
    print(f"[*] Wordlist: {wordlist_path}")
    print(f"[*] Using {cpu_count()} processes")

    # Prepare arguments for each password candidate
    candidates = []
    with open(wordlist_path, 'rb') as f:
        for line in f:
            password_bytes = line.strip()
            if password_bytes:  # Skip empty lines
                candidates.append((password_bytes, salt, iterations, target_hash))

    # Process in parallel
    with Pool(cpu_count()) as pool:
        for result in pool.imap_unordered(check_password, candidates, chunksize=1000):
            if result:
                print(f"\n[+] Password found: {result}")
                sys.exit(0)

    print("\n[-] Password not found in wordlist.")