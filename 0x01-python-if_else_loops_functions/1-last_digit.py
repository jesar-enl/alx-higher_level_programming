#!/usr/bin/python3

# Print a random signed number
'''
use it to check if last digit is;
1. greater than 5: print("...and is greater than 5")
2. 0: print("...is 0")
3. less than 6 and not 0: print("...and is less than 6 and not 0")
'''
import random
number = random.randint(-10000, 10000)

# use the string representation function to get the
# last character of the string
# convert the last character into an integer
value = abs(number)

if number < 0:
    last_digit = -1 * (value % 10)
else:
    last_digit = (value % 10)

if last_digit > 5:
    message = "is greater than 5"
elif last_digit == 0:
    message = "is 0"
elif last_digit < 6 and last_digit != 0:
    message = "is less than 6 and not 0"
print(f"Last digit of {number:d} is {last_digit:d} and {message}")
