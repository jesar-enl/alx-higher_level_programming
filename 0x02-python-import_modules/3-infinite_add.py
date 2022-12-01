#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
# get the length of the arguments
n = len(argv)
# get the sum of the arguments passed
sum = 0
for i  in range(1, n):
    sum += int(argv[i])
# print the result
print("{:d}".format(sum))
