from random import *


def encode(asciiCode, n):  # encodes x.....x (n times) where asciiCode represents x
    targetEncoding = 0

    for i in range(n-1):
        targetEncoding += (256 ** i) * (32)
    targetEncoding += (256 ** (n-1)) * (asciiCode)
    return targetEncoding


def encodeChar(asciiCode, n):  # encodes the value of a particular ascii code at particular position n
    return (256 ** n) * asciiCode


def translateAscii(asciiCodes):  # translates ascii codes to readable form
    decodedPhrase = ""
    for code in asciiCodes:
        decodedPhrase += str(chr(code))
    return decodedPhrase


# returns true if target encoding is bigger than temp encoding
def isDiffBigger(asciiCode, guessLength, targetEncoding):
    tempEncoding = encode(asciiCode, guessLength)
    if (targetEncoding - tempEncoding >= 0):
        return 1
    else:
        return 0


# finds the ascii code that minimises the encoding difference start : min ascii code, end: max ascii code, guessLength: length of encoded phrase
def find(start, end, targetEncoding, guessLength, asciiChars):

    if (end >= start and guessLength > 0):
        asciiCode = (end+start) // 2
        tempEncoding = encode(asciiCode, guessLength)

        # print("targetEncoding  : ", targetEncoding)
        # print("tempEncoding    : ", tempEncoding)
        # print("diff            : ", targetEncoding - tempEncoding)
        # print("start: ", start)
        # print("end  : ", end)
        # print("asciiCode  : ", asciiCode)
        # print("*******************************")

        # diff needs to get smaller
        if(not isDiffBigger(asciiCode, guessLength, targetEncoding)):
            return find(start, asciiCode-1, targetEncoding, guessLength, asciiChars)

        # should find the first ascii char that makes targetEncoding-tempEncoding positive
        if (isDiffBigger(asciiCode, guessLength, targetEncoding)):
            # need to check if asciiCode is the first positive diff
            if(isDiffBigger(asciiCode+1, guessLength, targetEncoding)):
                # diff needs to get bigger
                return find(asciiCode+1, end, targetEncoding, guessLength, asciiChars)
            else:
                asciiChars.append(asciiCode)
                return asciiCode, targetEncoding - encodeChar(asciiCode, guessLength-1), guessLength-1, asciiChars
    else:
        return -1


def main():

    start = 32  # ascii code
    end = 127  # ascii code
    # targetEncoding = 391565397484887
    # guessLength = 6  # number of letters encoded
    targetEncoding = 87
    guessLength = 1
    asciiChars = []  # store the decoded asci codes

    result = find(start, end, targetEncoding, guessLength, asciiChars)
    print("In main: ", result)

    if(not result == -1):
        (asciiCode, diff, left, arr) = result
        print("char: ", translateAscii(arr))


if (__name__ == "__main__"):
    main()
