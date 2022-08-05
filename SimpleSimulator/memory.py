
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

def takeAnd(line):
    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:16]

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
        
        elif (opcodeType == "B"):
            reg1 = line[5:8]
            imm = line[8:]
        
        elif (opcodeType == "C"):
            reg1 = line[10:13]
            reg2 = line[13:]
        
        elif (opcodeType == "D"):
            reg1 = line[5:8]
            memAddr = line[8:]
        
        elif (opcodeType == "E"):
            reg1 = line[10:13]
            reg2 = line[13:]
        
        elif (opcodeType == "F"):
            hltFlag = 1
            break
        

        
        
