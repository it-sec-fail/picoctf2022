#!/usr/bin/env python

import re

flag = ""

print("Let me extract the flag from the svg file...")

with open("drawing.flag.svg","r") as file:
    lookfor = re.compile('^.*tspan.*">(.*)</tspan.*', re.IGNORECASE)
    for line in file:
        _ = lookfor.match(line)
        if _:
            flag = flag + _.group(1)
    
    print("And here it is: ")
    print(flag.replace(" ",""))
