from params import opcode
from params import registers

# not handling variables
# assuming input taken as string and split based on space into list
def printbin(lst):
    code = lst[0]
    val = ''
    #A
    if (code == 'add'):
        val = opcode[code][0] + '00' + registers[code[1]] + registers[code[2]] + registers[code[3]]
    
    elif (code == 'sub'):
        val = opcode[code][0] + '00' + registers[code[1]] + registers[code[2]] + registers[code[3]]
    
    elif (code == 'mul'):
        val = opcode[code][0] + '00' + registers[code[1]] + registers[code[2]] + registers[code[3]]

    elif (code == 'xor'):
        val = opcode[code][0] + '00' + registers[code[1]] + registers[code[2]] + registers[code[3]]
        
    elif (code == 'or'):
        val = opcode[code][0] + '00' + registers[code[1]] + registers[code[2]] + registers[code[3]]

    elif (code == 'and'):
        val = opcode[code][0] + '00' + registers[code[1]] + registers[code[2]] + registers[code[3]]

    #B,C
    # elif (code == 'mov'):
    #     val = opcode[code[0]] + registers[code[1]] 
    elif (code == 'mov'):
        if (lst[-1][0] == '$'):
            pass
            #add stuff
        else:
            val = opcode[code][1][0] + '00000' + registers[code[1]] + registers[code[2]]

    elif (code == 'div'):
        val = opcode[code][0] + '00000' + registers[code[1]] + registers[code[2]]

    elif (code == 'not'):
        val = opcode[code][0] + '00000' + registers[code[1]] + registers[code[2]]

    elif (code == 'cmp'):
        val = opcode[code][0] + '00000' + registers[code[1]] + registers[code[2]]



    
    
    








