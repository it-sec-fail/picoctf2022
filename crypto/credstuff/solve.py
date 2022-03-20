#!/usr/bin/env python

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
