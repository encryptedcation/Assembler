import sys
from motherConvertor import binaryToInteger, integerToBinary


class memHandler:
    MEM_SIZE = 256
    mem = ["0000000000000000"] * MEM_SIZE

    def load(self, inputFile):
        for idx, line in enumerate(inputFile):
            self.mem[idx] = line.rstrip("\n")

    def getInst(self, progCount):
        return self.mem[progCount]

    def getValueAtAdd(self, memAdd):
        return binaryToInteger(self.mem[binaryToInteger(memAdd)])

    def loadValueAtAdd(self, memAdd, val):
        self.mem[binaryToInteger(memAdd)] = integerToBinary(val, 16)

    def dump(self):
        for memAdd in self.mem:
            sys.stdout.write(memAdd + "\n")
