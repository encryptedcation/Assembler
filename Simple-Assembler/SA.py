opcode = {
    "add": ("10000", "A"),
    "sub": ("10001", "A"),
    "mov": [("10010", "B"), ("10011", "C")],
    "ld": ("10100", "D"),
    "st": ("10101", "D"),
    "mul": ("10110", "A"),
    "div": ("10111", "C"),
    "rs": ("11000", "B"),
    "ls": ("11001", "B"),
    "xor": ("11010", "A"),
    "or": ("11011", "A"),
    "and": ("11100", "A"),
    "not": ("11101", "C"),
    "cmp": ("11110", "C"),
    "jmp": ("11111", "E"),
    "jlt": ("01100", "E"),
    "jgt": ("01101", "E"),
    "je": ("01111", "E"),
    "hlt": ("01010", "F"),
}

registers = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
}

registersF = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111",
}


lineCount = 0  # Counting number of lines entered till now
lines = []
variables = []
labels = {}
instrn_count = 0


def make_8_bit(num):
    con_num = []
    while num >= 1:
        rem = num % 2
        con_num.append(str(int(rem)))
        num = num // 2
    con_num = con_num[::-1]
    bin = "".join(con_num)
    if len(bin) < 8:
        bin = "0" * (8 - len(bin)) + bin
    return bin


def printbin(lst):
    code = lst[0]
    val = ""
    # A
    if code == "add":
        val = (
            opcode[code][0]
            + "00"
            + registersF[lst[1]]
            + registersF[lst[2]]
            + registersF[lst[3]]
        )

    elif code == "sub":
        val = (
            opcode[code][0]
            + "00"
            + registersF[lst[1]]
            + registersF[lst[2]]
            + registersF[lst[3]]
        )

    elif code == "mul":
        val = (
            opcode[code][0]
            + "00"
            + registersF[lst[1]]
            + registersF[lst[2]]
            + registersF[lst[3]]
        )

    elif code == "xor":
        val = (
            opcode[code][0]
            + "00"
            + registersF[lst[1]]
            + registersF[lst[2]]
            + registersF[lst[3]]
        )

    elif code == "or":
        val = (
            opcode[code][0]
            + "00"
            + registersF[lst[1]]
            + registersF[lst[2]]
            + registersF[lst[3]]
        )

    elif code == "and":
        val = (
            opcode[code][0]
            + "00"
            + registersF[lst[1]]
            + registersF[lst[2]]
            + registersF[lst[3]]
        )

    # B,C

    elif code == "mov":
        if lst[-1][0] == "$":
            needed_num = int(lst[-1][1:])
            final_bin = make_8_bit(needed_num)
            val = opcode[code][0][0] + registersF[lst[1]] + final_bin

        else:
            val = opcode[code][1][0] + "00000" + registersF[lst[1]] + registersF[lst[2]]

    elif code == "div":
        val = opcode[code][0] + "00000" + registersF[lst[1]] + registersF[lst[2]]

    elif code == "not":
        val = opcode[code][0] + "00000" + registersF[lst[1]] + registersF[lst[2]]

    elif code == "cmp":
        val = opcode[code][0] + "00000" + registersF[lst[1]] + registersF[lst[2]]

    elif code == "ls":
        needed_num = int(lst[-1][1:])
        final_bin = make_8_bit(needed_num)
        val = opcode[code][0][0] + registersF[lst[1]] + final_bin

    elif code == "rs":
        needed_num = int(lst[-1][1:])
        final_bin = make_8_bit(needed_num)
        val = opcode[code][0][0] + registersF[lst[1]] + final_bin

    # F
    elif code == "hlt":
        val = opcode[code][0] + "00000000000"

    # D
    elif code == "ld":
        if lst[-1] in variables:
            for i in range(len(variables)):
                if variables[i] == lst[-1]:
                    ind = i
                    break
            mem_addr = instrn_count + (ind + 1)
            bin_mem_addr = make_8_bit(mem_addr)
            val = opcode[code][0] + registersF[lst[1]] + bin_mem_addr
        else:
            pass  # handle no variable declared error here?

    elif code == "st":
        if lst[-1] in variables:
            for i in range(len(variables)):
                if variables[i] == lst[-1]:
                    ind = i
                    break
            mem_addr = instrn_count + (ind + 1)
            bin_mem_addr = make_8_bit(mem_addr)
            val = opcode[code][0] + registersF[lst[1]] + bin_mem_addr
        else:
            pass  # handle no variable declared error here?

    # E
    elif code == "jmp":
        bin_mem_addr = labels[lst[1]]

        val = opcode[code][0] + "000" + bin_mem_addr

    elif code == "jlt":
        bin_mem_addr = labels[lst[1]]

        val = opcode[code][0] + "000" + bin_mem_addr

    elif code == "jgt":
        bin_mem_addr = labels[lst[1]]

        val = opcode[code][0] + "000" + bin_mem_addr

    elif code == "je":
        bin_mem_addr = labels[lst[1]]

        val = opcode[code][0] + "000" + bin_mem_addr

    print(val)


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
        print("Reused label name: " + labelName)
        return False
    elif duplicateVar(labelName):
        print("Misuse: Label name is same as variable name: " + labelName)
        return False
    else:
        return True


def varNameValidity(varName: str):
    if duplicateVar(varName):
        print("Reused variable name: " + varName)
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
            exit()
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
        if line.split()[1] in labels.keys():
            return True
        else:
            print("Label not found: " + line.split()[1])
            exit()
    elif cmd in loadStore:
        if line.split()[2] in variables:
            return True
        else:
            print("Variable not found: " + line.split()[2])
            exit()

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
                else:
                    return False
            elif line[1] == "FLAGS":
                if regValidity(line[2]):
                    return True
                else:
                    return True
            elif line[2] == "FLAGS":
                print("Illegal use of FLAGS register. Command: " + " ".join(line))
                exit()
            else:
                return False
        if "FLAGS" in line:
            print("Illegal use of FLAGS register. Command: " + " ".join(line))
            exit()
        if opcode[cmd][1] == "A":
            if regValidity(line[1]) and regValidity(line[2]) and regValidity(line[3]):
                return True
        elif opcode[cmd][1] == "B":
            if regValidity(line[1]) and immediateValidity(line[2]):
                return True
        elif opcode[cmd][1] == "C":
            if regValidity(line[1]) and regValidity(line[2]):
                return True
        elif opcode[cmd][1] == "D":
            if regValidity(line[1]) and isValidMemAddr(" ".join(line)):
                return True
        elif opcode[cmd][1] == "E":
            if isValidMemAddr(" ".join(line)):
                return True
        elif opcode[cmd][1] == "F":
            if len(line) == 1:
                return True
        elif line[-1] == ":":
            return True
        else:
            return False
    else:
        return False


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

flagVarOver = 0
while True:
    try:
        if lineCount <= 256:
            cmd = input()
            if cmd.split()[0] == "var":
                if len(cmd.split()) == 2:
                    if flagVarOver:
                        print(
                            "Error: Variables found after the beginning at line "
                            + str(lineCount + 1)
                            + ": "
                            + cmd
                        )
                        exit()
                    else:
                        var = cmd.split()[1]
                        if duplicateVar(var):
                            print(
                                f"Error: Duplicate variable on line {lineCount+1}: {cmd}"
                            )
                            exit()
                        else:
                            if varNameValidity(var):
                                variables.append(var)
                                lineCount += 1
                                continue
                            else:
                                exit()
                else:
                    print(
                        "General Syntax Error on line "
                        + str(lineCount + 1)
                        + ": "
                        + cmd
                    )
                    exit()
            else:
                flagVarOver = 1
            if ":" in cmd:
                cmd1 = cmd.split(":")[1].strip()
                if labelValidity(cmd.split(":")[0]):
                    if isValidCmd(cmd1):
                        if isLineValid(cmd1):
                            labels[cmd.split(":")[0]] = lineCount - len(variables)
                            lines.append(cmd1)
                            lineCount += 1
                        else:
                            print(f"General Syntax Error on line {lineCount+1}: {cmd}")
                            exit()
                    else:
                        print(f"General Syntax Error on line {lineCount+1}: {cmd}")
                        exit()
                else:
                    print("Invalid label on line:", lineCount, cmd.split(":")[0])
                    exit()
            elif isValidCmd(cmd):
                if isLineValid(cmd):
                    lines.append(cmd)
                    lineCount += 1
                else:
                    print(f"General Syntax Error on line {lineCount+1}: {cmd}")
                    exit()
            else:
                print(
                    "Error: Invalid Command on line " + str(lineCount + 1) + ": " + cmd
                )
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

for key in labels.keys():
    labels[key] = make_8_bit(labels[key] - len(variables))

for line in lines:
    printbin(line.split())
