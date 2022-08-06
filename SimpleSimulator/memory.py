from matplotlib import pyplot as plt

PC = 0
Cycle = -1
x_coord = []
y_coord = []
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


def movReg(reg1, reg2):
    R[reg1] = R[reg2]
    resetFlag()


def add(reg1, reg2, reg3):
    R[reg1] = R[reg2] + R[reg3]
    if R[reg1] > 65535:
        R[reg1] = 65535  # make all bits 1 in reg1
        R["111"] = 8  # setting overflow flag
    else:
        resetFlag()


def sub(reg1, reg2, reg3):
    R[reg1] = R[reg2] - R[reg3]
    if R[reg1] < 0:
        R[reg1] = 0  # case of underflow
        R["111"] = 8  # setting overflow flag
    else:
        resetFlag()


def OR(reg1, reg2, reg3):
    R[reg1] = R[reg2] | R[reg3]
    resetFlag()


def mul(r1, r2, r3):
    R[r1] = R[r2] * R[r3]
    if R[r1] > 65535:
        R[r1] = 65535
        R["111"] = 8  # Raise OVERFLOW flag
    else:
        resetFlag()


def divide(r1, r2, r3):
    R[r1] = int(R[r2] / R[r3])
    if R[r1] < 0:
        R[r1] = 0  # case of underflow
        R["111"] = 8  # Raise OVERFLOW flag
    else:
        resetFlag()


def rShift(r1, imm):
    R[r1] = R[r1] >> imm
    if R[r1] < 0:
        R[r1] = 0  # case of underflow
        R["111"] = 8  # Raise OVERFLOW flag
    else:
        resetFlag()


def lShift(r1, imm):
    R[r1] = R[r1] << imm
    if R[r1] > 65535:
        R[r1] = 65535
        R["111"] = 8
    else:
        resetFlag()


def xor(r1, r2, r3):
    R[r1] = R[r2] ^ R[r3]
    if R[r1] > 65535:
        R[r1] = 65535
        R["111"] = 8  # Raise OVERFLOW flag
    else:
        resetFlag()


def AND(r1, r2, r3):
    R[r1] = R[r2] & R[r3]
    if R[r1] > 65535:
        R[r1] = 65535
        R["111"] = 8  # Raise OVERFLOW flag
    else:
        resetFlag()


def invert(reg1, reg2):
    R[reg1] = 65535 ^ R[reg2]
    resetFlag()


def compare(r1, r2):
    resetFlag()
    if R[r1] == R[r2]:
        R["111"] = 1
    elif R[r1] > R[r2]:
        R["111"] = 2
    else:
        R["111"] = 4


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


def load(r1, mem):
    if mem not in memAddr.keys():
        memAddr[mem] = 0
    R[r1] = memAddr[mem]
    resetFlag()


def store(r1, mem):
    memAddr[mem] = R[r1]
    resetFlag()


def jmp(mem):
    PC = mem


def jgt(line):
    if R["111"] == 2:
        PC = line
    else:
        PC += 1


def je(line):
    if R["111"] == 1:
        PC = line
    else:
        PC += 1


def jlt(line):
    if R["111"] == 4:
        PC = line
    else:
        PC += 1


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
    opcodeType = findOpcodeType(opcode)

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
            jmp(memAddr)

        elif opcode == "01100":
            jlt(memAddr)

        elif opcode == "01101":
            jgt(memAddr)

        elif opcode == "01111":
            je(memAddr)

    elif opcodeType == "F":
        hltFlag = 1
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
