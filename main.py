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
a. Typos in instruction name or register name DONE
b. Use of undefined variables
c. Use of undefined labels
d. Illegal use of FLAGS register
e. Illegal Immediate values (more than 8 bits)
f. Misuse of labels as variables or vice-versa
g. Variables not declared at the beginning DONE
h. Missing hlt instruction DONE
i. hlt not being used as the last instruction DONE
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

# hlt checks --------
if "hlt" in lines:
    if lines[-1] != "hlt":
        print("Error: hlt not being used as the last instruction")
        exit()
else:
    print("Error: Missing hlt instruction")
    exit()
# --------

# var checks --------
for lineCount in range(len(lines)):
    line = lines[lineCount]
    if "var" in line:
        if flagVarOver:
            print(
                "Error: Variables found after the beginning at line "
                + str(lineCount)
                + ": "
                + line
            )
            exit()
        else:
            var = line.split()[1]
            if var in variables:
                print(f"Error: Duplicate variable on line {lineCount}: {line}")
                exit()
            variables.append(var)
    else:
        flagVarOver = 1
        continue
# --------
