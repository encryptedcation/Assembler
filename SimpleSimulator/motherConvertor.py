def binaryToInteger(binStr):
    """
    Converts a binary string binStr to corresponding integerVal.
    """
    return int(binStr, 2)


def integerToBinary(intVal, bitSize):
    """
    Converts an integer into corresponding binary string with given bit length.
    """
    binStr = bin(intVal)[2:]
    if bitSize > len(binStr):
        binStr = "0" * (bitSize - len(binStr)) + binStr
    else:
        binStr = binStr[(len(binStr) - bitSize) :]
    return
