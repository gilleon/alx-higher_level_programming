#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv) - 1
    sumval = 0
    for x in range(len):
        sumval += int(sys.argv[x + 1])
    print(sumval)
