R = {
    "000" : 3,
    "001" : 5,
    "010" : 6,
    "011" : 0,
    "100" : 0,
    "101" : 0,
    "110" : 0,
    "111" : 0,
}

# overflowFlag = 0

#R is a dictionary which stores the current value in the register as key and register code as value

#assuming all R have decimal values stored in them

hltFlag = 0

PC = 0

def initializeMem():
    pass

def resetFlag():
    pass

def memDump():
    pass


def movImm(reg1,imm): # assuming immediate is already a decimal here
    R[reg1] = imm
    resetFlag()
    memDump()

def movReg(reg1,reg2):
    R[reg1] = R[reg2]
    resetFlag()
    memDump()

def add(reg1,reg2,reg3):
    R[reg1] = R[reg2] + R[reg3]
    if R[reg1] > 65535:
        R[reg1] = 65535 # make all bits 1 in reg1
        R['111'] = 8  # setting overflow flag
    else:
        resetFlag()
    memDump()

def sub(reg1,reg2,reg3):
    R[reg1] = R[reg2] - R[reg3]
    if R[reg1] < 0:
        R[reg1] = 0 # case of underflow
        R['111'] = 8  # setting overflow flag
    else:
        resetFlag()
    memDump()

def OR(reg1,reg2,reg3):
    R[reg1] = R[reg2] | R[reg3]
    resetFlag()
    memDump()

def mul(line):
    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:16]
    R[r1] = R[r2]*R[r3]
    return R[r1]

def divide(line):
    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:16]
    R[r1] = R[r2]/R[r3]
    return R[r1]

def rShift(line):
    r1 = line[7:10]
    r2 = line[10:18]
    R[r1] = R[r2]/R[r3]
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

def invert():
    pass

def compare():
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

def load():
    pass

def store():
    pass

def jmp():
    pass

def jgt():
    pass

def je():
    pass

def jlt():
    pass

r = input() # enter input file name

with open(r , "r") as file:
    lines = file.readlines()

    while (hltFlag != 1):
        line = lines[PC]
        opcode = line[0:5]
        opcodeType = findOpcodeType(opcode)

        if (opcodeType == "A"):
            reg1 = line[7:10]
            reg2 = line[10:13]
            reg3 = line[13:]

            if (opcode == "10000"):
                PC += 1
                res = add(reg1, reg2, reg3)
            
            elif (opcode == "10001"):
                PC += 1
                res = sub(reg1, reg2, reg3)
            
            elif (opcode == "10110"):
                PC += 1
                res = mul(reg1, reg2, reg3)

            elif (opcode == "11010"):
                PC += 1
                res = xor(reg1, reg2, reg3)

            elif (opcode == "11011"):
                PC += 1
                res = OR(reg1, reg2, reg3)
            
            elif (opcode == "11100"):
                PC += 1
                res = AND(reg1, reg2, reg3)

            elif (opcode == "10001"):
                PC += 1
                res = sub(reg1, reg2, reg3)

        
        elif (opcodeType == "B"):
            reg1 = line[5:8]
            imm = line[8:]

            if (opcode == "10010"):
                PC += 1
                res = movImm(reg1, imm)
            
            elif (opcode == "11001"):
                PC += 1
                res = lShift(reg1, imm)
            
            elif (opcode == "11000"):
                PC += 1
                res = rShift(reg1, imm)
        
        elif (opcodeType == "C"):
            reg1 = line[10:13]
            reg2 = line[13:]

            if (opcode == "10011"):
                PC += 1
                res = movReg(reg1, reg2)
            
            elif (opcode == "10111"):
                PC += 1
                res = divide(reg1, reg2)
            
            elif (opcode == "11101"):
                PC += 1
                res = invert(reg1, reg2)
            
            elif (opcode == "11110"):
                PC += 1
                res = compare(reg1, reg2)
        
        elif (opcodeType == "D"):
            reg1 = line[5:8]
            memAddr = line[8:]

            if (opcode == "10100"):
                PC += 1
                res = load(reg1, memAddr)
            
            elif (opcode == "10101"):
                PC += 1
                res = store(reg1, memAddr)
        
        elif (opcodeType == "E"):
            memAddr = line[8:]

            if (opcode == "11111"):
                PC = 'idk'
                res = jmp(memAddr)
            
            elif (opcode == "01100"):
                PC = 'idk'
                res = jlt(memAddr)
            
            elif (opcode == "01101"):
                PC = 'idk'
                res = jgt(memAddr)
            
            elif (opcode == "01111"):
                PC = 'idk'
                res = je(memAddr)
        
        elif (opcodeType == "F"):
            hltFlag = 1
            break
        

        
        
