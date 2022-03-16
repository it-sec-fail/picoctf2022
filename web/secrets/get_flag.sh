#!/bin/bash
curl http://saturn.picoctf.net:49810/secret/hidden/superhidden/ > /dev/null 2>&1| grep -o "picoCTF{.*}"
