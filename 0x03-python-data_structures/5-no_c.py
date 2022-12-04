#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        my_list = list(my_string)
        new_list = []
        for l in my_list:
            if l != 'c' and l != 'C':
                new_list.append(l)
        new_string = ''.join(new_list)
        return new_string
    else:
        return None
