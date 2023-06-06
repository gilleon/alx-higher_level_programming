#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
last_digit = abs(num) % 10
if num < 0:
    last_digit = -last_digit
print("Last last_digit of {} is {} and is ".format(num, last_digit), end="")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 not 0")
