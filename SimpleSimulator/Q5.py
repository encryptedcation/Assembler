import math


def gets_key(value):
    for key, val in val_dict.items():
        if val == value:
            return key


# values in dictionaries are in bits
val_dict = {
    "KB": 2**13,
    "MB": 2**23,
    "GB": 2**33,
    "Kb": 2**10,
    "Mb": 2**20,
    "Gb": 2**30,
    "b": 1,
    "B": 8,
    "TB": 2 * 43,
    "Tb": 40,
}
char_space = input("Enter total memory space: ").split()
val_of_space = int(char_space[0]) * val_dict[char_space[1]]
address_mode = input("How is the memory addressed? ")

# isa and instructions related
len_of_instrn = int(input("Enter length of one instruction in bits: "))
len_of_reg = int(input("Enter length of register in bits: "))
if address_mode == "Bit":
    num_of_bits_addrs = math.ceil(math.log(val_of_space, 2))
    num_of_bits_op = len_of_instrn - len_of_reg - num_of_bits_addrs
    num_of_fill_bits = len_of_instrn - len_of_reg - len_of_reg - num_of_bits_op
    max_num_of_intrns = 2 ** (num_of_bits_op)
    max_num_of_regs = 2 ** (len_of_reg)

elif address_mode == "Nibble":
    num_of_bits_addrs = math.ceil(math.log(val_of_space / 4, 2))
    num_of_bits_op = len_of_instrn - len_of_reg - num_of_bits_addrs
    num_of_fill_bits = len_of_instrn - len_of_reg - len_of_reg - num_of_bits_op
    max_num_of_intrns = 2 ** (num_of_bits_op)
    max_num_of_regs = 2 ** (len_of_reg)

elif address_mode == "Byte":
    num_of_bits_addrs = math.ceil(math.log(val_of_space / 8, 2))
    num_of_bits_op = len_of_instrn - len_of_reg - num_of_bits_addrs
    num_of_fill_bits = len_of_instrn - len_of_reg - len_of_reg - num_of_bits_op
    max_num_of_intrns = 2 ** (num_of_bits_op)
    max_num_of_regs = 2 ** (len_of_reg)

# word addressable is not possible, so taking default as byte addressable
elif (
    address_mode == "Word"
    or address_mode != "Byte"
    or address_mode != "Nibble"
    or address_mode != "Bit"
):
    print("Used byte addressable here as no cpu data given")
    num_of_bits_addrs = math.ceil(math.log(val_of_space / 8, 2))
    num_of_bits_op = len_of_instrn - len_of_reg - num_of_bits_addrs
    num_of_fill_bits = len_of_instrn - len_of_reg - len_of_reg - num_of_bits_op
    max_num_of_intrns = 2 ** (num_of_bits_op)
    max_num_of_regs = 2 ** (len_of_reg)

print(f"Min bits for address = {num_of_bits_addrs}")
print(f"Bits for opcode = {num_of_bits_op}")
print(f"Number of filler bits = {num_of_fill_bits}")
print(f"Max number of instructions = {max_num_of_intrns}")
print(f"Max number of registers = {max_num_of_regs}")

# system enhancement related
# type 1
cpu_bits = int(input("How many bits is the cpu? "))
newAddressMode = input("Enter mode of address other than the previously entered one: ")
while newAddressMode == address_mode:
    newAddressMode = input("Type already used. Pick any other type: ")

if newAddressMode == "Bit":
    num_of_bit_newAddrs = math.ceil(math.log(val_of_space / 1, 2))

elif newAddressMode == "Nibble":
    num_of_bit_newAddrs = math.ceil(math.log(val_of_space / 4, 2))

elif newAddressMode == "Byte":
    num_of_bit_newAddrs = math.ceil(math.log(val_of_space / 8, 2))

elif newAddressMode == "Word":
    num_of_bit_newAddrs = math.ceil(math.log(val_of_space / cpu_bits, 2))
# if type not defined, default is byte
else:
    num_of_bit_newAddrs = math.ceil(math.log(val_of_space / 8, 2))

print(num_of_bit_newAddrs - num_of_bits_addrs)

# type 2
new_cpu_bits = int(input("Enter number of bits in cpu: "))
add_pins = int(input("Enter number of address pins: "))
type_of_addr = input("Enter type of addressable memory: ")
s
# output is in bytes
if type_of_addr == "Bit":
    mem_size = 2 ** (add_pins) / 8
elif type_of_addr == "Nibble":
    mem_size = ((2 ** (add_pins)) * 4) / 8
elif type_of_addr == "Byte":
    mem_size = 2 ** (add_pins)
elif type_of_addr == "Word":
    mem_size = mem_size = ((2 ** (add_pins)) * new_cpu_bits) / 8


mem_bits = math.log(mem_size, 2)
num = math.ceil(mem_bits) % 10  # number part
num_part = 2 ** (num)
val = gets_key((2 ** (mem_bits - num)) * 8)  # dictionary has value stored in bits
print(f"{num_part} {val}")
