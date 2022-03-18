#!/bin/bash
echo "Getting flag for you..."
echo "Using password ak98-=90adfjhgj321sleuth9000"
echo "ak98-=90adfjhgj321sleuth9000" | python patchme.flag.py | grep -o "picoCTF{.*}"
