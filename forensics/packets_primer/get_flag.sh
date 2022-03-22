#!/bin/bash

echo "Getting flag from pcap file..."

strings network-dump.flag.pcap | grep "p i c o"| tr -d ' '
