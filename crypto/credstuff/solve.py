#!/usr/bin/env python

import codecs

user="cultiris"
counter=1

with open("leak/usernames.txt","r") as userfile:
    for line in userfile:
#        print(line.strip())
        if line.strip() == user:
            print("Found user " + user + " at line " + str(counter) + ".")
            break
        counter+=1

with open("leak/passwords.txt","r") as passwdfile:
    all_lines = passwdfile.readlines()
    index = counter - 1
    
    print("Getting corresponding line with password")
    
    flag_enc = all_lines[index]

    print("Password looks encoded (rot13)... " + flag_enc)
    print("decoding...")

    flag = codecs.decode(flag_enc, 'rot_13')

    print("Got it!")
    print(">>   " + flag)
