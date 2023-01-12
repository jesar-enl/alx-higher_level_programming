#!/usr/bin/python3
"""Module to contain the user input"""


from name_function import get_formatted_name

print("Enter 'q' to quit.")
while True:
    first = input("\nWhat is your first name: ")
    if first == 'q':
        break
    last = input("Please enter the second name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nYour neatly formatted name: {formatted_name}.")
