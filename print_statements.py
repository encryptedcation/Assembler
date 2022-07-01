from params import *

instrn_count = 0  # counts number of instructions without variable declarations
var_lst = []   # stores variables
# lst has the contents of current instruction
# assuming input taken as string and split based on space into list

# if (lst[0] != 'var'):
#     instrn_count += 1
# else:
#     var_lst.append(lst[1])

# assuming 1st instruction is at memory address 1
#############################################



def make_8_bit(num):  # have to check for overflow?
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

def printbin(lst):
    code = lst[0]
    val = ''
    #A
    if (code == 'add'):
        val = opcode[code][0] + '00' + registers[lst[1]] + registers[lst[2]] + registers[lst[3]]
    
    elif (code == 'sub'):
        val = opcode[code][0] + '00' + registers[lst[1]] + registers[lst[2]] + registers[lst[3]]
    
    elif (code == 'mul'):
        val = opcode[code][0] + '00' + registers[lst[1]] + registers[lst[2]] + registers[lst[3]]

    elif (code == 'xor'):
        val = opcode[code][0] + '00' + registers[lst[1]] + registers[lst[2]] + registers[lst[3]]
        
    elif (code == 'or'):
        val = opcode[code][0] + '00' + registers[lst[1]] + registers[lst[2]] + registers[lst[3]]

    elif (code == 'and'):
        val = opcode[code][0] + '00' + registers[lst[1]] + registers[lst[2]] + registers[lst[3]]

    #B,C
 
    elif (code == 'mov'):
        if (lst[-1][0] == '$'):
            needed_num = int(lst[-1][1:])
            final_bin = make_8_bit(needed_num)
            val = opcode[code][0][0] +registers[lst[1]] + final_bin

        else:
            val = opcode[code][1][0] + '00000' + registers[lst[1]] + registers[lst[2]]

    elif (code == 'div'):
        val = opcode[code][0] + '00000' + registers[lst[1]] + registers[lst[2]]

    elif (code == 'not'):
        val = opcode[code][0] + '00000' + registers[lst[1]] + registers[lst[2]]

    elif (code == 'cmp'):
        val = opcode[code][0] + '00000' + registers[lst[1]] + registers[lst[2]]

    elif (code == 'ls'):
        needed_num = int(lst[-1][1:])
        final_bin = make_8_bit(needed_num)
        val = opcode[code][0][0] +registers[lst[1]] + final_bin

    elif (code == 'rs'):
        needed_num = int(lst[-1][1:])
        final_bin = make_8_bit(needed_num)
        val = opcode[code][0][0] +registers[lst[1]] + final_bin

    #F
    elif (code=='hlt'):
        val = opcode[code][0] + '00000000000'

    #D
    elif (code == 'ld'):
        if (lst[-1] in var_lst):
            for i in range(len(var_lst)):
                if (var_lst[i] == lst[-1]):
                    ind = i
                    break
            mem_addr = instrn_count + (ind+1)
            bin_mem_addr = make_8_bit(mem_addr)
            val = opcode[code][0] + registers[lst[1]] + bin_mem_addr
        else:
            pass # handle no variable declared error here?

    elif (code == 'st'):
        if (lst[-1] in var_lst):
            for i in range(len(var_lst)):
                if (var_lst[i] == lst[-1]):
                    ind = i
                    break
            mem_addr = instrn_count + (ind+1)
            bin_mem_addr = make_8_bit(mem_addr)
            val = opcode[code][0] + registers[lst[1]] + bin_mem_addr
        else:
            pass # handle no variable declared error here?

    # E


        



# vals = ['hi', '&123']
# a = int(vals[1][1:])
# print(a)





    
    
    








