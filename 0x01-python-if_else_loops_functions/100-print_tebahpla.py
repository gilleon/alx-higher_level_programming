#!/usr/bin/python3
for x in range(122, 96, -1):
    c = True
    if x % 2 != 0:
        c = False
    print("{}".format(chr(x) if c else chr(x - 32)), end='')
