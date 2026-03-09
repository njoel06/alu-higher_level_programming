#!/usr/bin/python3
# 2-args.py

if __name__ == "__main__":
    import sys

    # Get all arguments (excluding script name)
    args = sys.argv[1:]
    # Print based on number of arguments
    if len(args) == 0:
        print("0 arguments.")
    elif len(args) == 1:
        print("1 argument:")
        print("1: {}".format(args[0]))
    else:
        print("{} arguments:".format(len(args)))                                                                    
        for i, arg in enumerate(args, 1):  
            print("{}: {}".format(i, arg))
