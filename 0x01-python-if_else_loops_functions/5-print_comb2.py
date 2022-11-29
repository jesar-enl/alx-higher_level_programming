#!/usr/bin/python3
'''
Program to print numbers from 00 t0 99
'''
for i in range(0,100):
    if i < 10:
        print(f"0{i},", end=" ")
    elif i == 99:
        print(i)
    else:
        print(f"{i},", end=" ")

