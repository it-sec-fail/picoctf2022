#!/bin/bash

echo "batteryhorse" | python3 unpackme.flag.py | grep -o "picoCTF{.*}"
