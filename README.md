# pbkdf2_crack
PBKDF2 hash cracker in Python3

#### Usage
python3 crack_pbkdf2.py <salt> <target_hash_hex> <wordlist_path> <iterations=600000>

Example:
```
python3 pbkdf2_crack.py 'AMtzteQIG7yAbZIa' '0673ad90a0b4afb19d662336f0fce3a9edd0b7b19193717be28ce4d66c887133' /usr/share/wordlists/rockyou.txt 600000
[*] Targeting PBKDF2-SHA256 with salt: AMtzteQIG7yAbZIa
[*] Target hash: 0673ad90a0b4afb19d662336f0fce3a9edd0b7b19193717be28ce4d66c887133
[*] Iterations: 600000
[*] Wordlist: /usr/share/wordlists/rockyou.txt
[*] Using 2 processes

[+] Password found: iloveyou1
```
