#!/bin/bash

chmod u+x run
echo "$(./run Hello!)" | grep -o "picoCTF{.*}"
chmod u-x run

