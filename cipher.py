#Creates a subsitution cipher with user's entry, then gives the option to decrypt the message

import time
from datetime import date
import getpass

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
space = []
key = 1
cipher = ''
print("CIA LEVEL 1A ACCESS: UNAUTHORIZED ACCESS PUNISHABLE BY LAW")
time.sleep(1)
plaintext = getpass.getpass(prompt='Enter Transmission: ', stream=None)

for c in plaintext or c in space: 
    if c in alphabet:
        cipher += alphabet[(alphabet.index(c) + key) % (len(alphabet))]

print('Your encrypted message is: ' + cipher)
time.sleep(1)
menuselect = input("What would you like to do?")
print("--------------------------")
print("1. Decrypt Message \n2. Exit")
print("--------------------------")

if menuselect == '1':
    print("Decrypted Message:")
    print("------------------")
    print(plaintext)
elif menuselect == '2':
    print("Logging Out...")
    time.sleep(1)
    date = date.today
    print("Logged off at:" + str(date))

