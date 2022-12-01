#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

# get the number of elements of argv
nargs = len(argv)

# print the number of elements/ arguments
if nargs == 1:
    # when no arguments are provided while executing
    print("{:d} arguments.".format(nargs - 1))
elif nargs > 1:
    # if arguments are provided.
    msg = "argument" if (nargs == 2) else "argments"
    print("{:d} {:s}:".format(nargs - 1, msg))
    # also print the arguments thatare given starting from index[1]
    for a in range(1, nargs):
        print("{:d}: {:s}".format(a, argv[a]))
