# Implements a recursive binary search approach to decode a given encoded value to readable form
# The encoding algorithm can be found in def encode.

from random import *


def encode(asciiCode, n):  # encodes .....x (n chars) where asciiCode represents x and all chars before are " "
    targetEncoding = 0
    for i in range(n-1):
        targetEncoding += (256 ** i) * (ord(" "))
    targetEncoding += (256 ** (n-1)) * (asciiCode)
    return targetEncoding


def encodeChar(asciiCode, n):  # encodes the value of a particular ascii code at position n
    return (256 ** n) * asciiCode


def translateAscii(asciiCodes):  # translates ascii codes (arr) to readable form
    decodedPhrase = ""
    for code in asciiCodes:
        decodedPhrase += str(chr(code))
    return decodedPhrase


# returns true if target encoding is bigger than or equal to temp encoding
def isDiffBigger(asciiCode, guessLength, targetEncoding):
    tempEncoding = encode(asciiCode, guessLength)
    if (targetEncoding - tempEncoding >= 0):
        return 1
    else:
        return 0


# finds the ascii code that minimises the encoding difference start : min ascii code, end: max ascii code, guessLength: length of encoded phrase
def decode(start, end, targetEncoding, guessLength):

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
            return decode(start, asciiCode-1, targetEncoding, guessLength)

        # should find the first ascii char that makes targetEncoding-tempEncoding positive
        if (isDiffBigger(asciiCode, guessLength, targetEncoding)):
            # need to check if asciiCode is the first positive diff
            if(isDiffBigger(asciiCode+1, guessLength, targetEncoding)):
                # diff needs to get bigger
                return decode(asciiCode+1, end, targetEncoding, guessLength)
            else:
                return asciiCode, targetEncoding - encodeChar(asciiCode, guessLength-1), guessLength-1
    else:
        return -1


def guessLength(targetEncoding):  # guesses the length of the decoded phrase
    i = 0
    guessEncoding = 0
    while (targetEncoding >= guessEncoding):
        i += 1
        guessEncoding = encode(ord(" "), i)
    return i-1


def main():

    # encoded value - 157709172775299964495191
    targetEncoding = int(input("Input the encoded value to be decoded: "))
    # guesses the length of the decoded phrase
    length = guessLength(targetEncoding)

    # min readable ascii code in decoded phrase
    start = ord(" ")
    # max readable ascii code in decoded phrase
    end = ord("~")
    # asciiChars to store the decoded asci codes in reverse order
    asciiChars = []

    # loop runs until all ascii codes are found. when a code is found, the length of  the to-be decoded phrase is decreased by one
    while (length > 0):
        # decode one of the ascii codes
        result = decode(start, end, targetEncoding, length)
        if(not result == -1):
            # recursively returns the decoded ascii code and remaining of targetEncoding and the length
            (asciiCode, targetEncoding, length) = result
            asciiChars.append(asciiCode)
        else:
            print("Exited with -1")

    print("Decoded phrase: ", translateAscii(asciiChars)[::-1])


if (__name__ == "__main__"):
    main()
