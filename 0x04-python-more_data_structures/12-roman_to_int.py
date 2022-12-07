#!/usr/bin/python3

# define the values of the roman numerals.
def value(v):
    if v == 'I':
        return 1
    if v == 'V':
        return 5
    if v == 'X':
        return 10
    if v == 'L':
        return 50
    if v == 'C':
        return 100
    if v == 'D':
        return 500
    if v == 'M':
        return 1000
    return -1


# function to convert to integer
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    else:
        res = 0
        i = 0

        while (i < len(roman_string)):
            # getting value of symbol
            sa = value(roman_string[i])

            if (i + 1 < len(roman_string)):
                # getting value of symbol
                sb = value(roman_string[i + 1])

                # comparing both values
                if (sa >= sb):
                    res = res + sa
                    i = i + 1
                else:
                    res = res + sb - sa
                    i = i + 2
            else:
                res = res + sa
                i = i + 1
        return res
