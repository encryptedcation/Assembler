from matplotlib import pyplot as plt
import sys

PC = 0
Cycle = 0
Cycle = -1
x_coord = []
y_coord = []
temp = []

from motherConvertor import binaryToInteger, integerToBinary
from regs import R, opc
from mem import memHandler

# overflowFlag = 0

# R is a dictionary which stores the current value in the register as key and register code as value

# assuming all R have decimal values stored in them

hltFlag = 0

memFile = memHandler()
memFile.load(sys.stdin)


def floatToDec(binNum: str):
    exp = binNum[:3]
    mantissa = binNum[3:]
    exp = bin(binaryToInteger(exp))[2:]
    mantissa = "1" + "".join(mantissa)
    dec = binaryToInteger(mantissa[: -(len(exp))])
    exp = list(exp)
    exp = [int(i) for i in exp]
    res = 0
    idx = 1
    for i in exp:
        res += (i * 2) ** (-idx)
        idx += 1
    return dec + res


def resetFlag():
    R["111"] = 0


def findOpcodeType(op_bin):  # takes the opcode in binary
    return opc[op_bin]


def movImm(reg1, imm):  # assuming immediate is already a decimal here
    R[reg1] = imm
    resetFlag()
    dump()


def movReg(reg1, reg2):
    R[reg2] = R[reg1]
    resetFlag()
    dump()


def add(reg1, reg2, reg3):
    R[reg1] = R[reg2] + R[reg3]
    if R[reg1] > 65535:
        R[reg1] = R[reg1] % 65535  # make all bits 1 in reg1
        R["111"] = 8  # setting overflow flag
        dump()
    else:
        resetFlag()
        dump()


def sub(reg1, reg2, reg3):
    R[reg1] = R[reg2] - R[reg3]
    if R[reg1] < 0:
        R[reg1] = 0  # case of underflow
        R["111"] = 8  # setting overflow flag
        dump()
    else:
        resetFlag()
        dump()


def OR(reg1, reg2, reg3):
    R[reg1] = R[reg2] | R[reg3]
    resetFlag()
    dump()


def mul(r1, r2, r3):
    R[r1] = R[r2] * R[r3]
    if R[r1] > 65535:
        R[r1] = R[r1] % 65535
        R["111"] = 8  # Raise OVERFLOW flag
        dump()
    else:
        resetFlag()
        dump()


def divide(r1, r2):
    R["000"] = int(R[r1] / R[r2])
    R["001"] = int(R[r1] % R[r2])
    if R[r1] < 0:
        R["000"] = 0  # case of underflow
        R["111"] = 8  # Raise OVERFLOW flag
        dump()
    else:
        resetFlag()
        dump()


def rShift(r1, imm):
    R[r1] = R[r1] >> imm
    if R[r1] < 0:
        R[r1] = 0  # case of underflow
        R["111"] = 8  # Raise OVERFLOW flag
        dump()
    else:
        resetFlag()
        dump()


def lShift(r1, imm):
    R[r1] = R[r1] << imm
    if R[r1] > 65535:
        R[r1] = R[r1] % 65535
        R["111"] = 8
        dump()
    else:
        resetFlag()
        dump()


def xor(r1, r2, r3):
    R[r1] = R[r2] ^ R[r3]
    if R[r1] > 65535:
        R[r1] = R[r1] % 65535
        R["111"] = 8  # Raise OVERFLOW flag
        dump()
    else:
        resetFlag()
        dump()


def AND(r1, r2, r3):
    R[r1] = R[r2] & R[r3]
    if R[r1] > 65535:
        R[r1] = R[r1] % 65535
        R["111"] = 8  # Raise OVERFLOW flag
        dump()
    else:
        resetFlag()
        dump()


def invert(reg1, reg2):
    R[reg1] = 65535 ^ R[reg2]
    resetFlag()
    dump()


def compare(r1, r2):
    resetFlag()
    if R[r1] == R[r2]:
        R["111"] = 1
    elif R[r1] > R[r2]:
        R["111"] = 2
    else:
        R["111"] = 4
    dump()


def load(r1, mem):
    R[r1] = binaryToInteger(memFile.mem[binaryToInteger(mem)])
    resetFlag()
    dump()


def store(r1, mem):
    memFile.mem[binaryToInteger(mem)] = integerToBinary(R[r1], 16)
    resetFlag()
    dump()


def jmp(mem):
    resetFlag()
    dump()
    global PC
    PC = binaryToInteger(mem)


def jgt(line):
    global PC
    if R["111"] == 2:
        resetFlag()
        dump()
        PC = binaryToInteger(line)
    else:
        resetFlag()
        dump()
        PC += 1


def addf(r1, r2, r3):
    # add floating point r2 and r3 and store in r1
    R[r1] = floatToDec(R[r2]) + floatToDec(R[r3])
    if R[r1] > 252.0:
        R[r1] = 252.0
        R["111"] = 8
        dump()
    else:
        resetFlag()
        dump()


def subf(r1, r2, r3):
    # subtract floating point r2 and r3 and store in r1
    R[r1] = floatToDec(R[r2]) - floatToDec(R[r3])
    if R[r1] < 0:
        R[r1] = 0
        R["111"] = 8
        dump()
    else:
        resetFlag()
        dump()


def movf(r1, imm):
    R[r1] = floatToDec(imm)
    resetFlag()
    dump()


def je(line):
    global PC
    if R["111"] == 1:
        resetFlag()
        dump()
        PC = binaryToInteger(line)
    else:
        resetFlag()
        dump()
        PC += 1


def jlt(line):
    global PC
    if R["111"] == 4:
        resetFlag()
        dump()
        PC = binaryToInteger(line)
    else:
        resetFlag()
        dump()
        PC += 1


def dump():
    print(integerToBinary(int(PC), 8), end=" ")
    for reg in R:
        print(integerToBinary(int(R[reg]), 16), end=" ")
    print()


lines = []

count = 0
while hltFlag != 1:
    count += 1
    if count > 100000:
        break
    Cycle += 1
    line = memFile.getInst(PC)
    x_coord.append(Cycle)
    y_coord.append(PC)
    opcode = line[0:5]
    opcodeType = findOpcodeType(opcode)

    if opcodeType == "A":
        reg1 = line[7:10].strip()
        reg2 = line[10:13].strip()
        reg3 = line[13:].strip()

        if opcode == "10000":
            add(reg1, reg2, reg3)
            PC += 1

        elif opcode == "10001":
            sub(reg1, reg2, reg3)
            PC += 1

        elif opcode == "10110":
            mul(reg1, reg2, reg3)
            PC += 1

        elif opcode == "11010":
            xor(reg1, reg2, reg3)
            PC += 1

        elif opcode == "11011":
            OR(reg1, reg2, reg3)
            PC += 1

        elif opcode == "11100":
            AND(reg1, reg2, reg3)
            PC += 1

        elif opcode == "10001":
            sub(reg1, reg2, reg3)
            PC += 1

        elif opcode == "00000":
            addf(reg1, reg2, reg3)

        elif opcode == "00001":
            subf(reg1, reg2, reg3)

    elif opcodeType == "B":
        reg1 = line[5:8].strip()
        imm1 = line[8:].strip()
        imm = binaryToInteger(line[8:].strip())

        if opcode == "10010":
            movImm(reg1, imm)
            PC += 1

        elif opcode == "11001":
            lShift(reg1, imm)
            PC += 1

        elif opcode == "11000":
            rShift(reg1, imm)
            PC += 1

        elif opcode == "10111":
            movf(reg1, imm1)

    elif opcodeType == "C":
        reg1 = line[10:13].strip()
        reg2 = line[13:].strip()

        if opcode == "10011":
            movReg(reg1, reg2)
            PC += 1

        elif opcode == "10111":
            divide(reg1, reg2)
            PC += 1

        elif opcode == "11101":
            invert(reg1, reg2)
            PC += 1

        elif opcode == "11110":
            compare(reg1, reg2)
            PC += 1

    elif opcodeType == "D":
        reg1 = line[5:8].strip()
        memAddr = line[8:].strip()

        if opcode == "10100":
            load(reg1, memAddr)
            PC += 1

        elif opcode == "10101":
            store(reg1, memAddr)
            PC += 1

    elif opcodeType == "E":
        memAddr = line[8:].strip()

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
        dump()
        break


memFile.dump()


"""def plot():
   plt.style.use("seaborn")
    plt.scatter(
        x_coord, y_coord, cmap="summer", edgecolor="black", linewidth=1, alpha=0.75
    )
    plt.title("Memory accessed Vs Cycles")
    plt.xlabel("Cycle number")
    plt.ylabel("Memory address")
    plt.tight_layout()
    plt.show()


plot()"""
