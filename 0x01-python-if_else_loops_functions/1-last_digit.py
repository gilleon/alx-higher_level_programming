import random
num = random.randint(-10000, 10000)
last_num = num % 10 if num > 0 else int(repr(num)[-1]) * -1
if (last_num > 5):
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(num, last_num))
elif (last_num == 0):
    print("Last digit of {:d} is {:d} and is 0"
          .format(num, last_num))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(num, last_num))
