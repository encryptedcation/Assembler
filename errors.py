from params import registers
from params import opcode

flag = 1

# flag to check that the variables have been declared at the beginning of the program . The flag becomes zero when any other command is called.

def isValidCmd(line: str):
    cmd = line.split()[0]
    if cmd in opcode.keys():
        flag = 0
        return True
    if cmd == "var":
        return True
    return False

def varNameValidity(varName: str):
    if varName.isdigit():
        return False
    if flag == 0:
        return False
    return True

def regValidity(reg: str):
    if reg in registers.keys():
        return True
    return False

def immediateValidity(imm: str):
    imm = list(imm)
    if imm[0] == '$':
        imm = ''.join(imm[1:])
        if imm.isdigit() and (int(imm) in range(0,256)):
            return True
    return False

def lenChecker(line: str):
    if isValidCmd(line):
        line = line.split()
        cmd = line[0]
        if cmd == 'mov' and immediateValidity(line[2]):
            return True
        elif cmd == 'mov' and regValidity(line[2]):
            return True           
        elif opcode[cmd][1] == 'A' and len(line) == 4:
            return True
        elif opcode[cmd][1] == 'B' and len(line) == 3:
            return True
        elif opcode[cmd][1] == 'C' and len(line) == 3:
            return True
        elif opcode[cmd][1] == 'D' and len(line) == 3:
            return True
        elif opcode[cmd][1] == 'E' and len(line) == 2:
            return True
        elif opcode[cmd][1] == 'F' and len(line) == 1:
            return True
        return False

def isValidMemAddr(line: str):
	cmd = line.split()[0]
	jumpCommands = ['jmp', 'jlt', 'jgt', 'je']
	loadStore = ['ld', 'st']
	if cmd in jumpCommands:
        # memaddr should be a label
		pass
	if cmd in loadStore:
		if varNameValidity(line[2]):
			return True
	return False 

def isLineValid(line: str):
    if lenChecker(line):
        line = line.split()
        cmd = line[0]
        if cmd == 'mov' and immediateValidity(line[2]) and regValidity(line[1]):
            return True
        if cmd == 'mov' and regValidity(line[1]) and regValidity(line[2]):
            return True
        if opcode[cmd][1] == 'A':
            if (regValidity(line[1]) and regValidity(line[2]) and regValidity(line[3])):
                return True
        if opcode[cmd][1] == 'B':
            if (regValidity(line[1]) and immediateValidity(line[2])):
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

# sample input to test the above functions

# line = "mov R0 R2"
# imm = '$32'
# reg = 'R9'
# reg1 = 'R4'
# varName = 'valala'
# varNAme2 = '1232'

# print(isValidCmd(line))
# print(isLineValid(line))
# print(isValidMemAddr(line))
# print(lenChecker(line))
# print(immediateValidity(imm))
# print(regValidity(reg))
# print(varNameValidity(varName))