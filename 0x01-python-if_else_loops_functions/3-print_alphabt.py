#!/usr/bin/python3
# Print the alphabet in lowercase, not followed by a newline

for alpha in range(ord('a'), ord('z') + 1):
    # exclude letters 'e' and 'q' in the list
    if alpha == ord('e') or alpha == ord('q'):
        continue
    else:
        print("{:s}".format(chr(aplha)), end="")
