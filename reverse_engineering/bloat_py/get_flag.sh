#!/bin/bash

echo "happychance" | python3 bloat.flag.py | grep -o "picoCTF{.*}"
