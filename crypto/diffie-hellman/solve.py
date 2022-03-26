#!/usr/bin/env python

from time import sleep

## Given by task description
p = 13
g = 5
alice = 7
bob = 3

## For the caeser cipher
charset="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Calculating keys with given values for decrypting...")
sleep(2)
## Calculating keys
Asecret = g**alice % p
Bsecret = g**bob % p
print("Oh boy - still calculating...")
sleep(2)
keya = Bsecret**alice % p
keyb = Asecret**bob % p
print("done...")

if keya == keyb:
    print("Keys are equal! Alice's key: " + str(keya) + " and Bobs key: " + str(keyb))
else: 
    print("Keys are different. Alice's key: " + str(keya) + " and Bobs key: " + str(keyb))

print("Let's decipher the caeser encrypted message with the keys.")

sleep(2)

with open("message.txt","r") as encfile:
    message = encfile.readline()

print("\n\nHere is the encrypted message:\n" + message)
print("Now I'll will decipher it... please wait while I process the message!\n\n")
print("Calculating forwards and backwards")
sleep(2)
print("Quite difficult...")
sleep(2)
print("Swirl letters...")
sleep(2)
print("Cuddle with bees! So sweet! They produce bee vomit!")
sleep(1)
print("Sorry - got distracted.")


def decrypt(key, message,forward):
    message = message.upper()
    result = "picoCTF{"

    for letter in message:
        if forward == True:
            if letter in charset:
                letter_index = (charset.find(letter) - key) % len(charset)
                result = result + charset[letter_index]
            else:
                result = result + letter
        else:
            if letter in charset:
                letter_index = (charset.find(letter) + key) %len(charset)
                result = result + charset[letter_index]
            else:
                result = result + letter
    result = result + "}"
    return result

sleep(1)
print("First one decrypted...\n")
print("Decoded message (forward):\n\t" + decrypt(keya,message,True))
sleep(2)
print("And backwards!!!\n")
print("Decoded message (backward):\n\t" + decrypt(keya,message,False))

print("\nYou need to decide which one the flag is... Don't ask me... I know it, but I won't tell!\nYou are welcome! Thank you for traveling with deutsche Bahn!")
