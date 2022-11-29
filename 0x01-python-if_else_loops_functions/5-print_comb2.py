#!/usr/bin/python3
'''
Program to print numbers from 00 t0 99
'''
for i in range(0,100):
    if i == 99:
        print("{:02d},".format(i), end=" ")
    else:
        print("{:02d},".format(i), end=" ")

