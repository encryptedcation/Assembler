from matplotlib import pyplot as plt

PC = 0
Cycle = -1
x_coord = []
y_coord = []
commandList = []
temp = []

R = {
    "000": 0,
    "001": 0,
    "010": 0,
    "011": 0,
    "100": 0,
    "101": 0,
    "110": 0,
    "111": 0,
}

# overflowFlag = 0

# R is a dictionary which stores the current value in the register as key and register code as value

# assuming all R have decimal values stored in them

hltFlag = 0

PC = 0


def initializeMem():
    pass


def resetFlag():
    pass


def memDump():
    pass


def movImm(reg1, imm):  # assuming immediate is already a decimal here
    R[reg1] = imm
    resetFlag()
    memDump()


def movReg(reg1, reg2):
    R[reg1] = R[reg2]
    resetFlag()
    memDump()


def add(reg1, reg2, reg3):
    R[reg1] = R[reg2] + R[reg3]
    if R[reg1] > 65535:
        R[reg1] = 65535  # make all bits 1 in reg1
        R["111"] = 8  # setting overflow flag
    else:
        resetFlag()
    memDump()


def sub(reg1, reg2, reg3):
    R[reg1] = R[reg2] - R[reg3]
    if R[reg1] < 0:
        R[reg1] = 0  # case of underflow
        R["111"] = 8  # setting overflow flag
    else:
        resetFlag()
    memDump()


def OR(reg1, reg2, reg3):
    R[reg1] = R[reg2] | R[reg3]
    resetFlag()
    memDump()


def mul(line):
    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:16]
    R[r1] = R[r2] * R[r3]
    if R[r1] > 65535:
    R[reg1] = 65535  # make all bits 1 in reg1
    R["111"] = 8  # setting overflow flag
    return R[r1]


def divide(line):
    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:16]
    R[r1] = R[r2] / R[r3]
    return R[r1]


def rShift(line):
    r1 = line[7:10]
    r2 = line[10:18]
    R[r1] = R[r2] / R[r3]
    return R[r1]


def lShift(line):
    r1 = line[7:10]
    r2 = line[10:18]


def xor(line):
    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:16]


def AND(line):
    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:16]


def invert(line):
    pass


def compare(line):
    pass


def mem(writeAddr):
    pass


def findOpcodeType(opcode):
    pass


def isValidReg(regs):
    pass


def isValidMemAddr(memAddr):
    pass


def isValidImm(imm):
    pass


def load(line):
    pass


def store(line):
    pass


def jmp(line):
    pass


def jgt(line):
    pass


def je(line):
    pass


def jlt(line):
    pass


lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

while hltFlag != 1:
    line = lines[PC]
    opcode = line[0:5]
    opcodeType = findOpcodeType(opcode) #yet to be programmed
    if opcodeType == "A":
        reg1 = line[7:10]
        reg2 = line[10:13]
        reg3 = line[13:]

        if opcode == "10000":
            PC += 1
            add(reg1, reg2, reg3)

        elif opcode == "10001":
            PC += 1
            sub(reg1, reg2, reg3)

        elif opcode == "10110":
            PC += 1
            mul(reg1, reg2, reg3)

        elif opcode == "11010":
            PC += 1
            xor(reg1, reg2, reg3)

        elif opcode == "11011":
            PC += 1
            OR(reg1, reg2, reg3)

        elif opcode == "11100":
            PC += 1
            AND(reg1, reg2, reg3)

        elif opcode == "10001":
            PC += 1
            sub(reg1, reg2, reg3)

    elif opcodeType == "B":
        reg1 = line[5:8]
        imm = line[8:]

        if opcode == "10010":
            PC += 1
            movImm(reg1, imm)

        elif opcode == "11001":
            PC += 1
            lShift(reg1, imm)

        elif opcode == "11000":
            PC += 1
            rShift(reg1, imm)

    elif opcodeType == "C":
        reg1 = line[10:13]
        reg2 = line[13:]

        if opcode == "10011":
            PC += 1
            movReg(reg1, reg2)

        elif opcode == "10111":
            PC += 1
            divide(reg1, reg2)

        elif opcode == "11101":
            PC += 1
            invert(reg1, reg2)

        elif opcode == "11110":
            PC += 1
            compare(reg1, reg2)

    elif opcodeType == "D":
        reg1 = line[5:8]
        memAddr = line[8:]

        if opcode == "10100":
            PC += 1
            load(reg1, memAddr)

        elif opcode == "10101":
            PC += 1
            store(reg1, memAddr)

    elif opcodeType == "E":
        memAddr = line[8:]

        if opcode == "11111":
            PC = "idk"
            jmp(memAddr)

        elif opcode == "01100":
            PC = "idk"
            jlt(memAddr)

        elif opcode == "01101":
            PC = "idk"
            jgt(memAddr)

        elif opcode == "01111":
            PC = "idk"
            je(memAddr)

    elif opcodeType == "F":
        hltFlag = 1
        break


while True:
    try:
        s = input()
        commandList.append(s)

    except EOFError:
        break


def plot():
    plt.style.use("seaborn")
    plt.scatter(
        x_coord, y_coord, cmap="summer", edgecolor="black", linewidth=1, alpha=0.75
    )
    plt.title("Memory accessed Vs Cycles")
    plt.xlabel("Cycle number")
    plt.ylabel("Memory address")
    plt.tight_layout()
    plt.show()


plot()
