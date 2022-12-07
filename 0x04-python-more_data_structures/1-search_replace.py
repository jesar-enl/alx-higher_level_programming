#!/usr/bin/pyhton3

def search_replace(my_list, search, replace):
    newl = []
    newl = list(map(lambda n: n if (n is not search) else replace, my_list))
    return newl
