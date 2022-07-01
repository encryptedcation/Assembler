# CAUTION: need to adjust the code for mov instruction

from params import registers
from params import opcode

def isValidCmd(line: str):
    cmd = line.split()[0]
    if cmd in opcode.keys():
	    return True
    return False

def varNameValidity(varName: str):
    pass

def regValidity(reg: str):
    if reg in registers.keys():
	    return True
    return False

def immediateValidity(imm: str):
    if imm.isdigit() and (int(imm) in range(0,256)):
	    return True
    return False

def lenChecker(line: str):
    line = line.split()
    if isValidCmd(line):
        cmd = line[0]
        if opcode[cmd][1] == 'A' and len(line) == 4:
	        return True
        if opcode[cmd][1] == 'B' and len(line) == 3:
    	    return True
        if opcode[cmd][1] == 'C' and len(line) == 3:
    	    return True
        if opcode[cmd][1] == 'D' and len(line) == 3:
    	    return True
        if opcode[cmd][1] == 'E' and len(line) == 2:
    	    return True
        if opcode[cmd][1] == 'F' and len(line) == 1:
    	    return True
        return False

def isValidMemAddr(memAddr: str):
    pass

def isLineValid(line: str):
    if lenChecker(line):
        line = line.split()
        cmd = line[0]
        if opcode[cmd][1] == 'A':
            if (regValidity(line[1]) and regValidity(line[2]) and regValidity(line[3])):
                return True
        if opcode[cmd][1] == 'B':
            if (regValidity(line[1]) and immediateValidity(imm)):
                return True
        if opcode[cmd][1] == 'C':
            if (regValidity(line[1]) and regValidity(line[2])):
                return True
        if opcode[cmd][1] == 'D' or opcode[cmd][1] == 'E':
            if (regValidity(line[1]) and isValidMemAddr(line[2])):
                return True
        if opcode[cmd][1] == 'F':
            if len(line) == 1:
                return True
    return False
