#!/usr/bin/env python

from sympy import mod_inverse

charset = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","_"]

flag = "picoCTF{"

encfile = "message.txt"

print("Try to decrypt file " + encfile)

with open(encfile, 'r', encoding='utf-8') as file:
    for line in file:
        numbers = line.split()
        for number in numbers:
            flag = flag + (charset[(mod_inverse(int(number),41))-1])

print("If anything worked... this should be the flag...")
print(flag + "}")

