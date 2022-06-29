# print("hello world")

# var errors

# opcodeDict = {add:("10000")}
# import params
from params import opcode

def isValidVar(line):
    reg2 = 32
    cmd = line.split()[0]
    if cmd == "mov":
        pass
        
    if cmd in opcode.keys():
        val = opcode[cmd][2]
        
        pass
        
    else:
        print("Invalid Command")
        return 69
        
isValidVar("mov")
for key, value in opcode.items():
    print(value[1])