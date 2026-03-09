#!/usr/bin/python3
# 2-args.py

if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(argc))
        for i in range(1, argc + 1
            print("{:d}: {}".format(i, sys.argv[i]))
