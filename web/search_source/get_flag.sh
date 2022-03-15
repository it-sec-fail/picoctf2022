#!/bin/bash

echo "Downloading website..."
wget --recursive http://saturn.picoctf.net:56849/ > /dev/null 2>&1
echo "Changing DIR Name..."
mv saturn.picoctf.net:56849 website
echo "Looking for flag..."
grep -rho "picoCTF{.*}" website

