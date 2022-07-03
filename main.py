from errors import *
from params import *
from print_statements import *

# List of functions in errors.py

# isLineValid uses most of the functions declared in errors.py
# use isLineValid to check the validity of the line. You don't have to manually use all the functions.

"""
1. isValidCmd(line: str)
2. duplicateVar(varName: str)
3. duplicateLabel(labelName: str)
4. labelValidity(labelName: str)
5. varNameValidity(varName: str)
6. regValidity(reg: str)
7. immediateValidity(imm: str)
8. lenChecker(line: str)lst
9. isValidMemAddr(line: str)
10. isLineValid(line: str)
"""

# List of functions in print_statements.py

"""
1. make_8_bit(num)
2. printbin(lst)
"""

# mehul writing here

"""Checks for list of lines:
1. Variables declared at the very starting
2. Redeclaration of variables not allowed
No use of undefined variables
No use of undefined labels
No illegal use of FLAGS register

Only one hlt at end
No lines after hlt

"""

lineCount = 0  # Counting number of lines entered till now
lines = []
variables = []
labels = {}

while True:
    try:
        if lineCount < 256:
            cmd = input()
            if isValidCmd(cmd):
                if isLineValid(cmd):
                    lines.append(cmd)
                    lineCount += 1
                else:
                    print(f"General Syntax Error on line {lineCount}: {cmd}")
                    exit()
            else:
                print("Error: Invalid Command on line " + str(lineCount) + ": " + cmd)
                exit()
        else:
            print("Error: Too many lines")
            exit()
    except EOFError:
        break
