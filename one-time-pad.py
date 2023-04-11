# One-Time Pad Encryption/Decryption Script
# Copyright (C) 2023 by cs-mt (https://github.com/cs-mt)

import random

def encrypt(plaintext, key):
    ciphertext = ""

    for x in range(len(plaintext)):
      char1 = plaintext[x]
      char2 = key[x]

      num1 = alphabet.index(char1)
      num2 = alphabet.index(char2)

      ciphernum = (num1+num2) % len(alphabet)
      ciphertext += alphabet[ciphernum]

    return ciphertext

def decrypt(ciphertext, key):
    decrypted = ""

    for x in range(len(ciphertext)):
      cipherletter = ciphertext[x]
      ciphernum = alphabet.index(cipherletter)

      keyletter = key[x]
      keynum = alphabet.index(keyletter)

      plainnum = (ciphernum-keynum) % len(alphabet)
      plainletter = alphabet[plainnum]

      decrypted += plainletter

    return decrypted

def generateKey(length):
    key = ""
    for x in range(length):
        key += random.choice(alphabet)

    return key

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "

action = input("(1) Encrypt (2) Decrypt : ")

if action == "1":
    plaintext = input("Plaintext (Alphanumeric English): ").upper()
    key = input("Key (-1 for random): ")

    if key == "-1":
      key = generateKey(len(plaintext))

    ciphertext = encrypt(plaintext, key)

    print("Key: {}".format(key))
    print("Ciphertext: {}".format(ciphertext))
elif action == "2":
    ciphertext = input("Ciphertext: ").upper()
    key = input("Key: ").upper()

    plaintext = decrypt(ciphertext, key)
    print("Decrypted: {}".format(plaintext))
