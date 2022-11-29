#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            letter = chr(ord(str[i]) - 32)
        else:
            letter = str[i]
        print("{:s}".format(letter), end="")
    print()
