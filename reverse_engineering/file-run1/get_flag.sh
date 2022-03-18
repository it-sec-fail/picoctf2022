#!/bin/bash

chmod u+x run
echo "$(./run)" | grep -o "picoCTF{.*}"
chmod u-x run

