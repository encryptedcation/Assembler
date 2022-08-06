import sys
from motherConvertor import binaryToInteger, integerToBinary


class memHandler:
    MEM_SIZE = 256
    mem = ["0000000000000000"] * MEM_SIZE

    def load(self, inputFile):
        for index, line in enumerate(inputFile):
            self.mem[index] = line.rstrip("\n")

    def getInst(self, pc):
        return self.mem[pc]

    def getValueAtAdd(self, memAdd):
        return binaryToInteger(self.mem[binaryToInteger(memAdd)])

    def loadValueAtAdd(self, memAdd, val):
        self.mem[binaryToInteger(memAdd)] = integerToBinary(val, 16)

    def dump(self):
        for Address in self.mem:
            sys.stdout.write(Address + "\n")
