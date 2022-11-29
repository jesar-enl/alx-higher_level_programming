#!/usr/bin/python3
# Print the alphabet in lowercase, not followed by a newline
for alpha in range(ord('a'), ord('z') + 1):
    print("{:s}".format(chr(alpha)), end="")
