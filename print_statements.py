from params import *

def make_8_bit(num):  # have to check for overflow?
    num=int(num)
    con_num=[]
    while num>=1:
        rem=num%2
        con_num.append(str(int(rem)))
        num=num//2
    con_num=con_num[::-1]
    bin = ''.join(con_num)
    if (len(bin) < 8):
        bin = '0'*(8-len(bin)) + bin
    return bin
    
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
 
    elif (code == 'mov'):
        if (lst[-1][0] == '$'):
            needed_num = lst[-1][1:]
            final_bin = make_8_bit(needed_num)
            val = opcode[code][0][0] +registers[code[1]] + final_bin

        else:
            val = opcode[code][1][0] + '00000' + registers[code[1]] + registers[code[2]]

    elif (code == 'div'):
        val = opcode[code][0] + '00000' + registers[code[1]] + registers[code[2]]

    elif (code == 'not'):
        val = opcode[code][0] + '00000' + registers[code[1]] + registers[code[2]]

    elif (code == 'cmp'):
        val = opcode[code][0] + '00000' + registers[code[1]] + registers[code[2]]

    elif (code == 'ls'):
        needed_num = lst[-1][1:]
        final_bin = make_8_bit(needed_num)
        val = opcode[code][0][0] +registers[code[1]] + final_bin

    #F
    elif (code=='hlt'):
        val = opcode[code][0] + '00000000000'

    #D
    elif (code == 'ld'):
        
        



# vals = ['hi', '&123']
# a = int(vals[1][1:])
# print(a)





    
    
    








