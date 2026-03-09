#!/usr/bin/python3
# 3-infinite_add.py

if __name__ == "__main__":
    import sys
# Initialize result to 0
    result = 0

# Add all arguments (starting from index 1 to skip script name)
    for i in range(1, len(sys.argv)):
        result += int(sys.argv[i])

# Print the result
    print(result)
