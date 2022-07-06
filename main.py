from errors import *
from params import *
from print_statements import *

lineCount = 0  # Counting number of lines entered till now
lines = []
variables = []
labels = {}


def isValidCmd(line: str):
    cmd = line.split()[0]
    if cmd in opcode.keys():
        return True
    if cmd == "var":
        return True
    return False


def duplicateVar(varName: str):
    if varName in variables:
        return True
    else:
        return False


def duplicateLabel(labelName: str):
    if labelName in labels:
        return True
    return False


def labelValidity(labelName: str):
    if duplicateLabel(labelName):
        return False
    if duplicateVar(labelName):
        print("Misuse: Label name is same as variable name: " + labelName)
        return False


def varNameValidity(varName: str):
    if duplicateVar(varName):
        return False
    if duplicateLabel(varName):
        print("Misuse: Variable name is same as label name: " + varName)
        return False
    if varName.isalnum():
        if varName.isdigit():
            print("Variable name can't be all digits")
            return False
        return True
    print("Variable name should be aplhanumeric")
    return False


def regValidity(reg: str):
    if reg in registers.keys():
        return True
    return False


def immediateValidity(imm: str):
    imm = list(imm)
    if imm[0] == "$":
        imm = "".join(imm[1:])
        if imm.isdigit() and (int(imm) in range(0, 256)):
            return True
        else:
            print("Imm more than 8 bits: " + imm)
            return False
    return False


def lenChecker(line: str):
    if isValidCmd(line) or line[-1] == ":":
        line = line.split()
        cmd = line[0]
        if cmd == "mov" and immediateValidity(line[2]):
            return True
        elif cmd == "mov" and regValidity(line[2]):
            return True
        elif opcode[cmd][1] == "A" and len(line) == 4:
            return True
        elif opcode[cmd][1] == "B" and len(line) == 3:
            return True
        elif opcode[cmd][1] == "C" and len(line) == 3:
            return True
        elif opcode[cmd][1] == "D" and len(line) == 3:
            return True
        elif opcode[cmd][1] == "E" and len(line) == 2:
            return True
        elif opcode[cmd][1] == "F" and len(line) == 1:
            return True
        elif line[-1] == ":":
            if line[:-1].isalnum():
                return True
            else:
                print("Label isn't alphanumeric")
    return False


def isValidMemAddr(line: str):
    cmd = line.split()[0]
    jumpCommands = ["jmp", "jlt", "jgt", "je"]
    loadStore = ["ld", "st"]
    if cmd in jumpCommands:
        if labelValidity(line[2]):
            return True
    if cmd in loadStore:
        if line[2] in variables:
            return True
    return False


def isLineValid(line: str):
    if lenChecker(line):
        line = line.split()
        cmd = line[0]
        if cmd == "mov":
            if regValidity(line[1]):
                if immediateValidity(line[2]):
                    return True
                elif regValidity(line[2]):
                    return True
                elif line[2] == "FLAGS":
                    return True
                else:
                    return False
            else:
                return False
        if "FLAGS" in line:
            print("Illegal use of FLAGS register. Command: " + line.join())
            return False
        if opcode[cmd][1] == "A":
            if regValidity(line[1]) and regValidity(line[2]) and regValidity(line[3]):
                return True
        elif opcode[cmd][1] == "B":
            if regValidity(line[1]) and immediateValidity(line[2]):
                return True
        elif opcode[cmd][1] == "C":
            if regValidity(line[1]) and regValidity(line[2]):
                return True
        elif opcode[cmd][1] == "D" or opcode[cmd][1] == "E":
            if regValidity(line[1]) and isValidMemAddr(line[2]):
                return True
        elif opcode[cmd][1] == "F":
            if len(line) == 1:
                return True
        elif line[-1] == ":":
            return True
        else:
            return False


# List of functions in print_statements.py

"""
1. make_8_bit(num)
2. printbin(lst)
"""

# mehul writing here

"""Checks for list of lines:
a. Typos in instruction name or register name DONE
b. Use of undefined variables DONE
c. Use of undefined labels DONE
d. Illegal use of FLAGS register DONE
e. Illegal Immediate values (more than 8 bits) DONE
f. Misuse of labels as variables or vice-versa
g. Variables not declared at the beginning DONE
h. Missing hlt instruction DONE
i. hlt not being used as the last instruction DONE
"""


while True:
    try:
        if lineCount < 256:
            cmd = input()
            if isValidCmd(cmd) or cmd[-1] == ":" or cmd[-1] == " ":
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
    if ":" in line:
        label = line.split(":")[0]
        if label in labels.keys():
            print(f"Error: Label {label} is already declared")
            exit()
        else:
            labels[label] = lineCount
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
            if duplicateVar(var, variables):
                print(f"Error: Duplicate variable on line {lineCount}: {line}")
                exit()
            else:
                variables.append(var)
    else:
        flagVarOver = 1
        continue
# --------
