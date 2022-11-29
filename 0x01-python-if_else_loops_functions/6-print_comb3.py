#!/usr/bin/python3

for i in range(9):
    j = i + 1
    for j in range(j, 10):
        print(f"{i}", end="")
        if i == 8 and j == 9:
            print(f"{j}", end="")
        else:
            print(f"{j}", end=", ")
