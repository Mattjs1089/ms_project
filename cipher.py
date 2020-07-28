#Creates a subsitution cipher with user's entry, then gives the option to decrypt the message

import time
import datetime
import getpass
#Initialize variables
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
space = []
key = 1
cipher = ''
print("WELCOME:::ENCRYPTION/DECRYPTION SOFTWARE:::")
print("-------------------------------------------")
time.sleep(1)
#hides user entry
plaintext = getpass.getpass(prompt='Enter Transmission: ', stream=None)
#Begin iteration of entryu, changing each letter according to key
for c in plaintext or c in space: 
    if c in alphabet:
        cipher += alphabet[(alphabet.index(c) + key) % (len(alphabet))]

print('Your encrypted message is: ' + cipher)
time.sleep(1)
menuselect = input("What would you like to do?")
print("--------------------------")
print("1. Decrypt Message \n2. Exit")
print("--------------------------")
#gives option to decrypt message
if menuselect == '1':
    print("Decrypted Message:")
    print("------------------")
    print(plaintext)
elif menuselect == '2':
    print("Logging Out...")
    time.sleep(1)
    date_time = datetime.datetime.now()
    print("Logged off at: ")
    print(date_time.strftime("%Y-%m-%d %H:%M:%S"))

