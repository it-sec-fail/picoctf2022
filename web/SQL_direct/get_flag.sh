#!/bin/bash

echo "Let me get the flag for you, just tell me the port:"
read -p "Port:" port
echo "select * from \"flags\";" | psql -h saturn.picoctf.net -p ${port} -U postgres pico
