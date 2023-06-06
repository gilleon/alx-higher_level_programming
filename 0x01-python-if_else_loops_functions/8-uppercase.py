#!/usr/bin/python3
def uppercase(str):
    for num in range(0, len(str)):
        if (ord(str[num]) >= 97) and (ord(str[num]) <= 122):
            lower = True
        else:
            lower = False
        print("{}".format((chr(ord(str[num]) - 32)) if lower else
              str[num]), end="")
    print("")
