import crypt
from itertools import product
from sys import argv

if len(argv) != 2:
    print('Usage: python crack.py hash')
    quit()

char_list = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

pw_hash = argv[1]
passed_salt = pw_hash[0:2]

for i in range(1, 6):
    for pw in product(char_list, repeat=i):
        pw = ''.join(pw).strip()
        if crypt.crypt(pw, passed_salt) == pw_hash:
            print(pw)
            quit()

print("Password not found")
