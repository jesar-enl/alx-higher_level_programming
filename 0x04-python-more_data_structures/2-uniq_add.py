#!/usr/bin/python3

def uniq_add(my_list=[]):
    num = set(my_list)
    res = 0
    for i in num:
        res = res + i
    return res
