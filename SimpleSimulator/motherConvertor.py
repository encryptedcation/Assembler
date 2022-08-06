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
    return binStr


def floatValidity(imm: str):
    imm = list(imm)
    if imm[0] == "$":
        try:
            imm = float("".join(imm[1:]))
            if (
                type(imm) == float
            ):  # ADD and imm in range(), the range of mantissa and exponent
                return True
        except ValueError:
            print("Invalid immediate.")
            return False
    return False
